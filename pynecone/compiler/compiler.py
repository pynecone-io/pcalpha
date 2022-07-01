"""Compiler for the pynecone apps."""

from typing import Type

from pynecone.base import Base
from pynecone.compiler import templates, utils
from pynecone.components.component import Component, ImportDict, merge_imports
from pynecone.state import State

# Imports to be included in every Pynecone app.
DEFAULT_IMPORTS: ImportDict = {
    "axios": {"axios"},
    "react": {"useEffect", "useState"},
    "next/router": {"useRouter"},
}


class Compiler(Base):
    """Class to compile the pynecone application."""

    @classmethod
    def compile(cls, component: Component, state: Type[State]) -> str:
        """Compile the component given the app state.

        Args:
            component: The component to compile.
            state: The app state.

        Returns:
            The compiled component.
        """
        # Merge the default imports with the app-specific imports.
        imports = merge_imports(DEFAULT_IMPORTS, component.get_imports())

        # Compile the code to render the component.
        return templates.COMPONENT(
            imports=utils.compile_imports(imports),
            constants=utils.compile_constants(),
            state=utils.compile_state(state),
            actions=utils.compile_actions(component),
            effects=utils.compile_effects(),
            render=component.render(),
        )
