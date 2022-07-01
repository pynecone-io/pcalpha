"""Create a list of components from an iterable."""
from __future__ import annotations

from typing import Iterable, Protocol, runtime_checkable

import pydantic

from pynecone.components.component import Component
from pynecone.components.iter_tag import IterTag
from pynecone.components.tag import Tag
from pynecone.property import Property


@runtime_checkable
class RenderFn(Protocol):
    """A function that renders a component."""

    def __call__(self, *args, **kwargs) -> Component:
        """Render a component.

        Args:
            *args: The positional arguments.
            **kwargs: The keyword arguments.

        Returns: # noqa: DAR202
            The rendered component.
        """
        ...


class Foreach(Component):
    """Display a foreach."""

    # The iterable to create components from.
    iterable: Property

    # A function from the render args to the component.
    render_fn: RenderFn

    @pydantic.validator("iterable")
    def validate_iterable(cls, iterable: Property) -> Property:
        """Validate that the iterable is really iterable.

        Args:
            iterable: The iterable to validate.

        Returns:
            The validated iterable.
        """
        assert issubclass(
            iterable.type_.__origin__, Iterable
        ), "The property must be an iterable."
        return iterable

    @classmethod
    def create(cls, iterable: Property, render_fn: RenderFn, **attrs) -> Foreach:
        """Create a foreach component.

        Args:
            iterable: The iterable to create components from.
            render_fn: A function from the render args to the component.
            **attrs: The attributes to pass to each child component.

        Returns:
            The foreach component.
        """
        return cls(
            iterable=iterable, render_fn=render_fn, children=[render_fn("_")], **attrs
        )

    def _render(self) -> Tag:
        return IterTag(iterable=self.iterable, render_fn=self.render_fn)
