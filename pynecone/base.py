"""Define the base class to be subclassed by all other classes."""
from __future__ import annotations

from typing import Any, TypeVar

import pydantic

# Type to define subclasses of Base.
PcType = TypeVar("PcType")


class Base(pydantic.BaseModel):
    """The base class subclassed by all other classes."""

    def json(self) -> str:
        """Convert the object to a json string.

        Returns:
            The object as a json string.
        """
        return self.__config__.json_dumps(self.dict())

    def set(self: PcType, **kwargs) -> PcType:
        """Set multiple fields and return the object.

        Args:
            **kwargs: The fields and values to set.

        Returns:
            The object with the fields set.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self

    @classmethod
    def get_fields(cls) -> dict[str, Any]:
        """Get the fields of the object.

        Returns:
            The fields of the object.
        """
        return cls.__fields__
