"""Define a state property."""
from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, Any, Callable, Type

from pynecone import constants, utils
from pynecone.base import Base

if TYPE_CHECKING:
    from pynecone.state import State


class Property(ABC):
    """An abstract property."""

    # The name of the property.
    name: str

    # The type of the property.
    type_: Type

    # The name of the enclosing state.
    state: str = ""

    def __hash__(self) -> int:
        """Define a hash function for a property.

        Returns:
            The hash of the property.
        """
        return hash((self.name, str(self.type_)))

    def __str__(self) -> str:
        """Wrap the property so it can be used in templates.

        Returns:
            The wrapped property, i.e. {state.property}.
        """
        return utils.wrap(self.full_name, "{")

    @property
    def full_name(self) -> str:
        """Get the full name of the property.

        Returns:
            The full name of the property.
        """
        if self.state == "":
            return self.name
        return ".".join([self.state, self.name])

    def set_state(self, state: State) -> Property:
        """Set the state of the property.

        Args:
            state: The state to set.
        """
        self.state = state.get_name()
        return self


class BaseProperty(Property, Base):
    """A base (non-computed) property of the app state."""

    # The name of the property.
    name: str

    # The type of the property.
    type_: Type

    # The name of the enclosing state.
    state: str = ""

    def __hash__(self) -> int:
        """Define a hash function for a property.

        Returns:
            The hash of the property.
        """
        return hash((self.name, str(self.type_)))

    def get_default_value(self) -> Any:
        """Get the default value of the property.

        Returns:
            The default value of the property.
        """
        if issubclass(self.type_, str):
            return ""
        if issubclass(self.type_, int | float):
            return 0
        if issubclass(self.type_, bool):
            return False
        if issubclass(self.type_, list):
            return []
        if issubclass(self.type_, dict):
            return {}
        if issubclass(self.type_, tuple):
            return ()
        if issubclass(self.type_, set):
            return set()
        return None

    def get_setter_name(self) -> str:
        """Get the name of the property's generated setter function.

        Returns:
            The name of the setter function.
        """
        setter = constants.SETTER_PREFIX + self.name
        if self.state == "":
            return setter
        return ".".join((self.state, setter))

    def get_setter(self) -> Callable[[State], None]:
        """Get the property's setter function.

        Returns:
            A function that that creates a setter for the property.
        """

        def setter(state: State, **kwargs):
            """Get the setter for the property.

            Args:
                state: The state within which we add the setter function.
                **kwargs: The values to set - the kwargs should have length 1.
            """
            setattr(state, self.name, next(iter(kwargs.values())))

        setter.__qualname__ = self.get_setter_name()

        return setter

    def json(self) -> str:
        """Convert the object to a json string.

        Returns:
            The object as a json string.
        """
        return self.__config__.json_dumps(self.dict())


class ComputedProperty(property, Property):
    """A field with computed getters."""

    @property
    def name(self) -> str:
        """Get the name of the property.

        Returns:
            The name of the property.
        """
        assert self.fget is not None, "Property must have a getter."
        return self.fget.__name__

    @property
    def type_(self):
        """Get the type of the property.

        Returns:
            The type of the property.
        """
        return self.fget.__annotations__["return"]
