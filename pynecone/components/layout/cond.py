"""Create a list of components from an iterable."""
from __future__ import annotations

import pydantic

from pynecone.components.component import Component
from pynecone.components.cond_tag import CondTag
from pynecone.components.tag import Tag
from pynecone.property import Property


class Cond(Component):
    """Display a conditional render."""

    # The condition to determine which component to render.
    condition: Property

    # The component to render if the condition is true.
    comp1: Component

    # The component to render if the condition is false.
    comp2: Component

    @pydantic.validator("condition")
    def validate_condition(cls, condition: Property) -> Property:
        """Validate that the condition is a boolean.

        Args:
            condition: The condition to validate.

        Returns:
            The validated condition.
        """
        assert issubclass(condition.type_, bool), "The property must be a boolean."
        return condition

    @classmethod
    def create(cls, condition: Property, comp1: Component, comp2: Component) -> Cond:
        """Create a conditional component.

        Args:
            condition: The condition to determine which component to render.
            comp1: The component to render if the condition is true.
            comp2: The component to render if the condition is false.

        Returns:
            The conditional component.
        """
        return cls(condition=condition, comp1=comp1, comp2=comp2)

    def _render(self) -> Tag:
        return CondTag(
            condition=self.condition,
            true_value=self.comp1.render(),
            false_value=self.comp2.render(),
        )
