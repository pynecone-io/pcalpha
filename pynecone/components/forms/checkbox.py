"""A checkbox component."""

from typing import Callable

from pynecone import utils
from pynecone.action import ActionSpec
from pynecone.components.chakra import ChakraComponent
from pynecone.components.tag import Tag
from pynecone.components.typography.text import Text
from pynecone.property import BaseProperty, Property
from pynecone.components.component import Example


class Checkbox(ChakraComponent):
    """The Checkbox component is used in forms when a user needs to select multiple values from several options."""

    tag = "Checkbox"

    # Color scheme for checkbox.
    color_scheme: str | None = None

    # "sm" | "md" | "lg"
    size: str | None = None

    # If true, the checkbox will be checked.
    is_checked: Property | None = None

    # If true, the checkbox will be disabled
    is_disabled: bool | None = None

    # If true and is_disabled is passed, the checkbox will remain tabbable but not interactive
    is_focusable: bool | None = None

    # If true, the checkbox will be indeterminate. This only affects the icon shown inside checkbox and does not modify the is_checked property.
    is_indeterminate: bool | None = None

    # If true, the checkbox is marked as invalid. Changes style of unchecked state.
    is_invalid: bool | None = None

    # If true, the checkbox will be readonly
    is_read_only: bool | None = None

    # If true, the checkbox input is marked as required, and required attribute will be added
    is_required: bool | None = None

    # The name of the input field in a checkbox (Useful for form submission).
    name: str | None = None

    # The callback invoked when the checkbox is focused
    on_focus: Callable[[str], None] | None = None

    # The spacing between the checkbox and its label text (0.5rem)
    spacing: str | None = None

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


class CheckboxGroup(ChakraComponent):
    """A group of checkboxes."""

    tag = "CheckboxGroup"

    # The initial value of the checkbox group
    default_value: str | None = None

    # If true, all wrapped checkbox inputs will be disabled
    is_disabled: bool | None = None

    # If true, input elements will receive checked attribute instead of isChecked. This assumes, you're using native radio inputs
    is_native: bool | None = None

    # The callback fired when any children Checkbox is checked or unchecked
    on_change: Callable[[str], None] | None = None

    # The value of the checkbox group
    value: str | None = None
