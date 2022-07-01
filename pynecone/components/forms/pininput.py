"""A button component."""

from typing import Callable

from pynecone import utils
from pynecone.action import ActionSpec
from pynecone.components.chakra import ChakraComponent
from pynecone.components.tag import Tag
from pynecone.components.typography.text import Text
from pynecone.property import BaseProperty, Property


class PinInput(ChakraComponent):
    """The component that provides context to all the pin-input fields."""

    tag = "PinInput"

    # State property to bind the the input.
    value: Property

    # The function to trigger on change.
    on_change: Callable[[str], None] | None = None

    # Function called when all inputs have valid values
    on_complete: Callable[[str], None] | None = None

    # If true, the pin input receives focus on mount
    auto_focus: bool | None = None

    # The default value of the pin input
    default_value: str | None = None

    # The border color when the input is invalid.
    error_border_color: str | None = None

    # The border color when the input is focused.
    focus_border_color: str | None = None

    # The top-level id string that will be applied to the input fields. The index of the input will be appended to this top-level id.
    id_: str | None = None

    # If true, the pin input component is put in the disabled state
    is_disabled: bool | None = None

    # If true, the pin input component is put in the invalid state
    is_invalid: bool | None = None

    # If true, focus will move automatically to the next input once filled
    manage_focus: bool | None = None

    # If true, the input's value will be masked just like `type=password`
    mask: bool | None = None

    # The placeholder for the pin input
    placeholder: str | None = None

    # The type of values the pin-input should allow ("number" | "alphanumeric").
    type_: str | None = None

    # State property to bind the the input.
    value: Property

    # "outline" | "flushed" | "filled" | "unstyled"
    variant: str | None = None

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
            local_args=("val",),
            args=((self.value.name, "val"),),
        )

    def _get_on_change(self) -> Callable[[str], None] | None:
        if self.on_change is None and isinstance(self.value, BaseProperty):
            return self.state.get_class_property(
                self.value.get_setter_name().split(".")
            )
        return self.on_change

    def _render(self) -> Tag:
        return (
            super()
            ._render()
            .add_attrs(
                value=str(self.value),
                on_change=self._get_action(),
                type=self.type_,
            )
        )



class PinInputField(ChakraComponent):
    """The text field that user types in - must be a direct child of PinInput."""

    tag = "PinInputField"
