"""Define the action specification."""
from __future__ import annotations

from typing import Any, Callable

from pynecone.base import Base


class ActionSpec(Base):
    """An action specification."""

    # The function linked to the action.
    fn: Callable

    # The local arguments on the frontend.
    local_args: tuple[str, ...] = ()

    # The arguments to pass to the function.
    args: tuple[Any, ...] = ()

    class Config:
        """The Pydantic config."""

        frozen = True

    def __lt__(self, other: ActionSpec) -> bool:
        """Compare two actions.

        Args:
            other: The other action to compare.

        Returns:
            True if this action is less than the other action.
        """
        return self.fn.__name__ < other.fn.__name__


class Action(Base):
    """An action that describes any state change in the app."""

    # The client token to specify the caller.
    token: str

    # The name of the function linked to the action.
    fn: str

    # The arguments to pass to the function.
    args: dict[str, Any] = {}
