"""Tag to loop through a list of components."""

from typing import Callable, Iterable

import pydantic

from pynecone import utils
from pynecone.components.tag import Tag
from pynecone.property import Property


class IterTag(Tag):
    """An iterator tag."""

    # The property to iterate over.
    iterable: Property

    # The component render function for each item in the iterable.
    render_fn: Callable

    @pydantic.validator("iterable")
    def validate_iterable(cls, iterable) -> Property:
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

    def __str__(self) -> str:
        """Render the tag as a React string.

        Returns:
            The React code to render the tag.
        """
        type_ = self.iterable.type_.__args__[0]
        arg = type_.__name__.lower()
        component = self.render_fn(type_)
        index = "i"
        if component.key is None:
            component.key = utils.wrap(index, "{")
        return utils.wrap(
            f"{self.iterable.full_name}.map(({arg}, {index}) => {component})",
            "{",
        )
