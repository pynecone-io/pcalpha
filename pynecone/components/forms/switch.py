"""A switch component."""
from typing import Callable

from pynecone.action import ActionSpec
from pynecone.components.chakra import ChakraComponent
from pynecone.components.tag import Tag
from pynecone.property import BaseProperty, Property


class Switch(ChakraComponent):
    """Togglable switch component."""

    tag = "Switch"

    # If true, the switch will be checked. You'll need to pass onChange to update its value (since it is now controlled)
    is_checked: Property

    # If true, the switch will be disabled
    is_disabled: Property | None = None

    # If true and isDisabled is passed, the switch will remain tabbable but not interactive
    is_focusable: Property | None = None

    # If true, the switch is marked as invalid. Changes style of unchecked state.
    is_invalid: Property | None = None

    # If true, the switch will be readonly
    is_read_only: Property | None = None

    # If true, the switch will be required
    is_required: Property | None = None

    # The name of the input field in a switch (Useful for form submission).
    name: str | None = None

    # The callback invoked when the switch is focused
    on_focus: Callable[[str], None] | None = None

    # The spacing between the switch and its label text (0.5rem)
    spacing: str | None = None

    # The placeholder text.
    placeholder: str | None = None

    # The function to trigger on change.
    on_change: Callable[[str], None] | None = None

    def _get_actions(self) -> set[ActionSpec]:
        action = self._get_action()
        if action is None:
            return set()
        return {action}

    def _get_action(self) -> ActionSpec | None:
        """Get the action for the on_change function.

        Returns:
            The action for the on_change function.
        """
        on_change = self._get_on_change()
        if on_change is None:
            return None
        return ActionSpec(
            fn=on_change,
            local_args=("e",),
            args=((self.is_checked.name, "e.target.checked"),),
        )

    def _get_on_change(self) -> Callable[[str], None] | None:
        if self.on_change is None and isinstance(self.is_checked, BaseProperty):
            return self.state.get_class_property(
                self.is_checked.get_setter_name().split(".")
            )
        return self.on_change

    def _render(self) -> Tag:
        return (
            super()
            ._render()
            .add_attrs(is_checked=str(self.is_checked), on_change=self._get_action())
        )
