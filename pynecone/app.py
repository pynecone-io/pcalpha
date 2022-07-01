"""High level access to define a pynecone app."""

import os
from collections import defaultdict
from typing import Any, Callable, Coroutine, Type

import fastapi
from fastapi.middleware import cors

from pynecone import constants, utils
from pynecone.action import Action
from pynecone.base import Base
from pynecone.compiler.compiler import Compiler
from pynecone.components.component import Component, ComponentStyle
from pynecone.state import State

# Define custom types.
View = Component | Callable[[], Component]
Reducer = Callable[[Action], Coroutine[Any, Any, State]]


class App(Base):
    """Base class for a pynecone application."""

    # The directory to output the compiled components to.
    pages_root: str = constants.WEB_PAGES_DIR

    # A map from the path to the view.
    views: dict[str, View] = {}

    # The backend api object.
    api: fastapi.FastAPI = None  # type: ignore

    # The state class to use for the app.
    state: Type[State] = State

    # The map from the client session token to the state.
    states: dict[str, State] = {}

    # The styling to apply to each component.
    style: ComponentStyle = {}

    # The compiler to use.
    compiler: Compiler = Compiler()

    class Config:
        """Config to satisfy pydantic type checking."""

        arbitrary_types_allowed = True

    def __init__(self, *args, **kwargs):
        """Initialize the app.

        Args:
            *args: Args to initialize the app with.
            **kwargs: Kwargs to initialize the app with.
        """
        super().__init__(*args, **kwargs)
        self.states = defaultdict(self.state)
        self.api = fastapi.FastAPI()
        self.add_cors()
        self.add_default_endpoints()

    def add_default_endpoints(self):
        """Add the default endpoints."""
        # To test the server.
        self.get(constants.Endpoint.PING)(_ping)

        # To make state changes.
        self.post(constants.Endpoint.ACTION)(_action(states=self.states))

    def add_cors(self):
        """Add CORS middleware to the app."""
        self.api.add_middleware(
            cors.CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def get(self, path: str | constants.Endpoint, *args, **kwargs) -> Callable:
        """Register a get request.

        Args:
            path: The endpoint path to link to the request.
            *args: Args to pass to the request.
            **kwargs: Kwargs to pass to the request.

        Returns:
            A decorator to handle the request.
        """
        if isinstance(path, constants.Endpoint):
            path = str(path)
        return self.api.get(path, *args, **kwargs)

    def post(self, path: str | constants.Endpoint, *args, **kwargs) -> Callable:
        """Register a post request.

        Args:
            path: The endpoint path to link to the request.
            *args: Args to pass to the request.
            **kwargs: Kwargs to pass to the request.

        Returns:
            A decorator to handle the request.
        """
        if isinstance(path, constants.Endpoint):
            path = str(path)
        return self.api.post(path, *args, **kwargs)

    def add_view(self, path: str, view: View):
        """Add a view to the app.

        Args:
            path: The path to add the view to.
            view: The view to add.
        """
        # Format the path.
        path = path.strip(os.path.sep)
        if path == "":
            path = constants.INDEX
        self.views[path] = view

    def compile(self):
        """Compile the app and output it to the pages folder."""
        for path, view in self.views.items():
            # Generate the view if necessary.
            component = view if isinstance(view, Component) else view()
            assert isinstance(component, Component), "Expected a Component."

            # Add the style and state to the component.
            component.add_style(self.style).set_state(self.state)

            # Get the path for the output file.
            output_path = os.path.join(self.pages_root, path) + constants.JS_EXT
            code = self.compiler.compile(component=component, state=self.state)
            with open(output_path, "w") as f:
                f.write(code)


async def _ping() -> str:
    """Test API endpoint.

    Returns:
        The response.
    """
    return "pong"


def _action(states: dict[str, State]) -> Reducer:
    """Create an action reducer to modify the state.

    Args:
        states: The map from the token to the user state.

    Returns:
        A reducer that takes in an action and modifies the state.
    """

    async def reducer(action: Action) -> State:
        state = states[action.token]

        # Call the reducer.
        fn = state.get_property(action.fn.split("."))
        fn(**action.args)

        # Return the original state.
        return state

    return reducer
