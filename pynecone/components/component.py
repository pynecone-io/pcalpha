"""Basic component definitions."""

from __future__ import annotations

import os
from abc import ABC
from collections import defaultdict
from typing import Any, ClassVar, Type

from pynecone import utils
from pynecone.action import ActionSpec
from pynecone.base import Base
from pynecone.components.tag import Tag
from pynecone.property import Property
from pynecone.state import State
from pynecone.style import Style

ImportDict = dict[str, set[str]]


class Component(Base, ABC):
    """The base class for all other pynecone components."""

    # The children nested within the component.
    children: list[Component] = []

    # An optional condition that must be True for the component to render.
    condition: Property | None = None

    # The style of the component.
    style: Style = Style()

    # The function to call when the component is clicked.
    on_click: ActionSpec | None = None

    # A unique key for the component.
    key: Any = None

    # The app state.
    state: Type[State] = State

    # Examples for how to use the component.
    _examples: ClassVar[list[Example]] = []

    class Config:
        """Pydantic config."""

        arbitrary_types_allowed = True

    def __init__(self, *args, **kwargs):
        """Initialize the component.

        Args:
            *args: Args to initialize the component.
            **kwargs: Kwargs to initialize the component.
        """
        # Find the style attributes.
        if "style" not in kwargs:
            kwargs["style"] = Style()
        if "on_click" in kwargs and not isinstance(kwargs["on_click"], ActionSpec):
            kwargs["on_click"] = ActionSpec(fn=kwargs["on_click"])
        kwargs["style"].update(
            {
                utils.to_camel_case(attr): value
                for attr, value in kwargs.items()
                if attr not in self.get_fields().keys()
            }
        )
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        """Represent the component in React.

        Returns:
            The code to render the component.
        """
        return self.render()

    def __str__(self) -> str:
        """Represent the component in React.

        Returns:
            The code to render the component.
        """
        return self.render()

    def _render(self) -> Tag:
        """Define how to render the component in React."""
        raise NotImplementedError

    def _get_actions(self) -> set[ActionSpec]:
        return set()

    @classmethod
    def create(cls, *children, **attrs) -> Component:
        """Create the component.

        Args:
            *children: The children of the component.
            **attrs: The attributes of the component.

        Returns:
            The component.
        """
        from pynecone.components.typography.text import Text

        children = [
            Text(text=child) if isinstance(child, str) else child for child in children
        ]
        return cls(children=children, **attrs)

    def add_style(self, style: ComponentStyle) -> Component:
        """Add additional style to the component and its children.

        Args:
            style: A dict from component to styling.

        Returns:
            The component with the additional style.
        """
        if type(self) in style:
            self.style = style[type(self)] | self.style
        for child in self.children:
            child.add_style(style)
        return self

    def set_state(self, state: Type[State]) -> Component:
        """Set the state of the component.

        Args:
            state: The state to set.

        Returns:
            The component with the state set.
        """
        self.state = state
        for child in self.children:
            child.set_state(state)
        return self

    def render(self) -> str:
        """Render the component.

        Returns:
            The code to render the component.
        """
        tag = self._render()
        return str(
            tag.add_attrs(on_click=self.on_click, key=self.key, sx=self.style).set(
                condition=self.condition,
                contents=os.linesep.join(
                    [tag.contents] + [child.render() for child in self.children]
                ),
            )
        )

    def _get_imports(self) -> ImportDict:
        return {}

    def get_imports(self) -> ImportDict:
        """Get all the libraries and fields that are used by the component.

        Returns:
            The import dict with the required imports.
        """
        return merge_imports(
            self._get_imports(), *[child.get_imports() for child in self.children]
        )

    def get_actions(self) -> set[ActionSpec]:
        """Get all the actions that are used by the component.

        Returns:
            The set of actions used by the component.
        """
        # Get the actions for just this component.
        actions = self._get_actions()

        # Add default actions for this component.
        if self.on_click is not None:
            actions.add(self.on_click)

        # Recursively get the actions for the children.
        for child in self.children:
            actions |= child.get_actions()

        # Return the actions for this component and all its children.
        return actions


def merge_imports(*imports) -> ImportDict:
    """Merge two import dicts together.

    Args:
        *imports: The list of import dicts to merge.

    Returns:
        The merged import dicts.
    """
    all_imports = defaultdict(set)
    for import_dict in imports:
        for lib, fields in import_dict.items():
            for field in fields:
                all_imports[lib].add(field)
    return all_imports


# Map from component to styling.
ComponentStyle = dict[Type[Component], Style]


class Example(Base):
    """An example of how to use a component."""

    # A description of the example.
    description: str

    # The code to run to show the example.
    code: str
