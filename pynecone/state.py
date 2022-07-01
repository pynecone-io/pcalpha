"""Define the pynecone state specification."""
from __future__ import annotations

from abc import ABC
from typing import Any, ClassVar, Type

from pynecone import utils
from pynecone.base import Base
from pynecone.property import BaseProperty, ComputedProperty, Property


class State(Base, ABC):
    """The state of the app."""

    # A map from the property name to the property.
    properties: ClassVar[dict[str, Property]] = {}

    # The base properties of the class.
    base_properties: ClassVar[set[BaseProperty]] = set()

    # The computed properties of the class.
    computed_properties: ClassVar[set[ComputedProperty]] = set()

    # Properties inherited by the parent state.
    inherited_properties: ClassVar[set[BaseProperty]] = set()

    # The substates of the state.
    substates: dict[str, State] = {}

    # The current page.
    page: str = ""

    @classmethod
    def __init_subclass__(cls, **kwargs):
        """Do some magic for the subclass initialization.

        Args:
            **kwargs: The kwargs to pass to the pydantic init_subclass method.
        """
        super().__init_subclass__(**kwargs)

        # Get the parent properties.
        if (parent_state := cls.get_parent_state()) is not None:
            cls.inherited_properties = (
                parent_state.inherited_properties | parent_state.base_properties
            )

        # Set the base and computed properties.
        skip_properties = {prop.name for prop in cls.inherited_properties} | {
            "substates"
        }
        cls.base_properties = {
            BaseProperty(name=f.name, type_=f.type_).set_state(cls)
            for f in cls.get_fields().values()
            if f.name not in skip_properties
        }
        cls.computed_properties = {
            v.set_state(cls)
            for v in cls.__dict__.values()
            if isinstance(v, ComputedProperty)
        }
        cls.properties = {
            prop.name: prop for prop in cls.base_properties | cls.computed_properties
        }

        # Setup the base properties at the class level.
        for prop in cls.base_properties:
            cls._set_property(prop)
            cls._create_setter(prop)
            cls._set_default_value(prop)

    @classmethod
    def get_parent_state(cls) -> State | None:
        """Get the parent state.

        Returns:
            The parent state.
        """
        parent_states = [
            base
            for base in cls.__bases__
            if issubclass(base, State) and base is not State
        ]
        assert len(parent_states) < 2, "Only one parent state is allowed."
        return parent_states[0] if len(parent_states) == 1 else None

    @classmethod
    def get_substates(cls) -> set[Type[State]]:
        """Get the substates of the state.

        Returns:
            The substates of the state.
        """
        return {subclass for subclass in cls.__subclasses__()}

    @classmethod
    def get_name(cls) -> str:
        """Get the name of the state.

        Returns:
            The name of the state.
        """
        name = utils.to_snake_case(cls.__name__)
        if (parent := cls.get_parent_state()) is not None:
            name = ".".join((parent.get_name(), name))
        return name

    def __init__(self, *args, **kwargs):
        """Initialize the state.

        Args:
            *args: The args to pass to the pydantic init method.
            **kwargs: The kwargs to pass to the pydantic init method.
        """
        super().__init__(*args, **kwargs)

        # Setup the substates.
        for substate in self.get_substates():
            self.substates[utils.to_snake_case(substate.__name__)] = substate()

    def __getattribute__(self, name: str) -> Any:
        """Get the attribute.

        Args:
            name: The name of the attribute.

        Returns:
            The attribute.
        """
        try:
            return super().__getattribute__(name)
        except Exception as e:
            # Check if the attribute is a substate.
            if name in self.substates:
                return self.substates[name]
            raise e

    def get_substate(self, path: list[str]) -> State | None:
        """Get the substate.

        Args:
            path: The path to the substate.

        Returns:
            The substate.
        """
        if len(path) == 0:
            return self
        if path[0] == utils.to_snake_case(type(self).__name__):
            if len(path) == 1:
                return self
            path = path[1:]
        return self.substates[path[0]].get_substate(path[1:])

    def get_property(self, path: list[str]) -> Any:
        """Get the property.

        Args:
            path: The path to the property.

        Returns:
            The property.
        """
        path, name = path[:-1], path[-1]
        substate = self.get_substate(path)
        return getattr(substate, name)

    @classmethod
    def get_class_substate(cls, path: list[str]) -> Type[State]:
        """Get the class substate.

        Args:
            name: The name of the substate.

        Returns:
            The class substate.
        """
        if len(path) == 0:
            return cls
        if path[0] == utils.to_snake_case(cls.__name__):
            if len(path) == 1:
                return cls
            path = path[1:]
        for substate in cls.get_substates():
            #print(path[0], substate.__name__, utils.to_snake_case(substate.__name__))
            if path[0] == utils.to_snake_case(substate.__name__):
                return substate.get_class_substate(path[1:])
        raise ValueError(f"Invalid path: {path}")

    @classmethod
    def get_class_property(cls, path: list[str]) -> Any:
        """Get the class property.

        Args:
            path: The path to the property.

        Returns:
            The class property.
        """
        path, name = path[:-1], path[-1]
        substate = cls.get_class_substate(path)
        return getattr(substate, name)

    @classmethod
    def _set_property(cls, prop: BaseProperty):
        """Set the property as a class member.

        Args:
            prop: The property instance to set.
        """
        setattr(cls, prop.name, prop)

    @classmethod
    def _create_setter(cls, prop: BaseProperty):
        """Create a setter for the property.

        Args:
            prop: The property to create a setter for.
        """
        setter_name = prop.get_setter_name().split(".")[-1]
        if setter_name not in cls.__dict__:
            setattr(cls, setter_name, prop.get_setter())

    @classmethod
    def _set_default_value(cls, prop: BaseProperty):
        """Set the default value for the property.

        Args:
            prop: The property to set the default value for.
        """
        # Get the pydantic field for the property.
        field = cls.get_fields()[prop.name]
        if field.required and ((default_value := prop.get_default_value()) is not None):
            field.required = False
            field.default = default_value

    def dict(self, include_computed: bool = True, **kwargs) -> dict[str, Any]:
        """Convert the object to a dictionary.

        Args:
            include_computed: Whether to include computed properties.
            **kwargs: Kwargs to pass to the pydantic dict method.

        Returns:
            The object as a dictionary.
        """
        return dict(
            sorted(
                (
                    {
                        prop.name: getattr(self, prop.name)
                        for prop in self.base_properties
                    }
                    | (
                        {
                            # Include the computed properties.
                            prop.name: getattr(self, prop.name)
                            for prop in self.computed_properties
                        }
                        if include_computed
                        else {}
                    )
                    | {
                        # Add the substates.
                        k: v.dict(include_computed=include_computed, **kwargs)
                        for k, v in self.substates.items()
                    }
                ).items()
            )
        )

    def hydrate(self):
        """Do nothing."""
        pass
