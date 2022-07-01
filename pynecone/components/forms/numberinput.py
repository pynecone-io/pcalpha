"""A button component."""

from typing import Callable

from pynecone import utils
from pynecone.action import ActionSpec
from pynecone.components.chakra import ChakraComponent
from pynecone.components.tag import Tag
from pynecone.property import BaseProperty, Property


class NumberInput(ChakraComponent):
    """The wrapper that provides context and logic to the components."""

    tag = "NumberInput"

    # State property to bind the the input.
    value: Property

    # The placeholder text.
    default_value: int | None = None

    # The type of input.
    type_: str = "text"

    # The function to trigger on change.
    on_change: Callable[[str], None] | None = None

    # If true, the input's value will change based on mouse wheel.
    allow_mouse_wheel: bool | None = None

    # This controls the value update when you blur out of the input. - If true and the value is greater than max, the value will be reset to max - Else, the value remains the same.
    clamped_value_on_blur: bool | None = None

    # The initial value of the counter. Should be less than max and greater than min
    default_value: int | None = None

    # The border color when the input is invalid.
    error_border_color: str | None = None

    # The border color when the input is focused.
    focus_border_color: str | None = None

    # If true, the input will be focused as you increment or decrement the value with the stepper
    focus_input_on_change: bool | None = None

    # Hints at the type of data that might be entered by the user. It also determines the type of keyboard shown to the user on mobile devices ("text" | "search" | "none" | "tel" | "url" | "email" | "numeric" | "decimal")
    input_mode: str | None = None

    # Whether the input should be disabled.
    is_disabled: bool | None = None

    # If true, the input will have `aria-invalid` set to true
    is_invalid: bool | None = None

    # If true, the input will be in readonly mode
    is_read_only: bool | None = None

    # Whether the input is required
    is_required: bool | None = None

    # Whether the pressed key should be allowed in the input. The default behavior is to allow DOM floating point characters defined by /^[Ee0-9+\-.]$/
    is_valid_character: str | None = None

    # This controls the value update behavior in general. - If true and you use the stepper or up/down arrow keys, the value will not exceed the max or go lower than min - If false, the value will be allowed to go out of range.
    keep_within_range: bool | None = None

    # The maximum value of the counter
    max_: int | None = None

    # The minimum value of the counter
    min_: int | None = None

    # "outline" | "filled" | "flushed" | "unstyled"
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


class NumberInputField(ChakraComponent):
    """The input field itself."""

    tag = "NumberInputField"


class NumberInputStepper(ChakraComponent):
    """The wrapper for the input's stepper buttons."""

    tag = "NumberInputStepper"


class NumberIncrementStepper(ChakraComponent):
    """The button to increment the value of the input."""

    tag = "NumberIncrementStepper"


class NumberDecrementStepper(ChakraComponent):
    """The button to decrement the value of the input."""

    tag = "NumberDecrementStepper"
