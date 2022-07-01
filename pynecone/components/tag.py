"""A React tag."""

from __future__ import annotations

import json
import os
from typing import Callable

import pydantic

from pynecone import utils
from pynecone.action import ActionSpec
from pynecone.base import Base
from pynecone.property import Property
from pynecone.style import Style

# The valid types for a tag attribute.
Attr = int | float | str | Callable | ActionSpec | Style | None


class Tag(Base):
    """A React tag."""

    # The name of the tag.
    name: str = ""

    # The attributes of the tag.
    attrs: dict[str, Attr] = {}

    # The inner contents of the tag.
    contents: str = ""

    # The condition that must be True for the tag to render.
    condition: Property | None = None

    class Config:
        """Pydantic config."""

        arbitrary_types_allowed = True

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

    @staticmethod
    def format_attr_value(value: Attr) -> int | float | str:
        """Format an attribute value.

        Args:
            value: The value of the attribute

        Returns:
            The formatted value to display within the tag.
        """
        # Handle string attributes.
        if isinstance(value, str):
            # For string variables, keep enclosing braces.
            if utils.is_wrapped(value, "{"):
                return value

            # Wrap string literals in quotes.
            return json.dumps(value)

        # Handle function attributes.
        if isinstance(value, Callable):
            value = ActionSpec(fn=value)

        # Handle actions.
        if isinstance(value, ActionSpec):
            local_args = ",".join(value.local_args)
            args = ",".join([":".join((name, val)) for name, val in value.args])
            value = f"({local_args}) => {utils.format_action_fn(fn=value.fn)}({utils.wrap(args, '{')})"
        else:
            value = json.dumps(value)

        # Wrap the variable in braces.
        return utils.wrap(value, "{", check_first=False)

    def format_attrs(self) -> str:
        """Format a dictionary of attributes.

        Returns:
            The formatted attributes.
        """
        # If there are no attributes, return an empty string.
        if len(self.attrs) == 0:
            return ""

        # Get the string representation of all the attributes joined.
        # We need a space at the beginning for formatting.
        return os.linesep.join(
            f"{name}={self.format_attr_value(value)}"
            for name, value in self.attrs.items()
            if value is not None
        )

    def __str__(self) -> str:
        """Render the tag as a React string.

        Returns:
            The React code to render the tag.
        """
        # Get the tag attributes.
        attrs_str = self.format_attrs()
        if len(attrs_str) > 0:
            attrs_str = " " + attrs_str

        if len(self.contents) == 0:
            # If there is no inner content, we don't need a closing tag.
            tag_str = utils.wrap(f"{self.name}{attrs_str}/", "<")
        else:
            # Otherwise wrap it in opening and closing tags.
            open = utils.wrap(f"{self.name}{attrs_str}", "<")
            close = utils.wrap(f"/{self.name}", "<")
            tag_str = utils.wrap(utils.indent(self.contents), open, close)

        # If there is a condition, we must conditionally render the tag.
        if self.condition is not None:
            tag_str = utils.format_conditional(self.condition.full_name, tag_str)

        return tag_str

    def add_attrs(self, **kwargs: Attr | None) -> Tag:
        """Add attributes to the tag.

        Args:
            **kwargs: The attributes to add.

        Returns:
            The tag with the attributes added.
        """
        self.attrs.update(
            {
                utils.to_camel_case(name): attr
                for name, attr in kwargs.items()
                if self.is_valid_attr(attr)
            }
        )
        return self

    @staticmethod
    def is_valid_attr(attr: Attr | None) -> bool:
        """Check if the attr is valid.

        Args:
            attr: The value to check.

        Returns:
            Whether the value is valid.
        """
        return attr is not None and not (isinstance(attr, dict) and len(attr) == 0)
