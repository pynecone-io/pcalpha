"""A button component."""

from typing import Callable

from pynecone import utils
from pynecone.action import ActionSpec
from pynecone.components.chakra import ChakraComponent
from pynecone.components.tag import Tag
from pynecone.property import BaseProperty, Property


class RangeSlider(ChakraComponent):
    """The RangeSlider is a multi thumb slider used to select a range of related values. A common use-case of this component is a price range picker that allows a user to set the minimum and maximum price."""

    tag = "RangeSlider"

    # State property to bind the the input.
    value: Property

    # The placeholder text.
    default_value: list | None = None

    # The type of input.
    type_: str = "array"

    # The function to trigger on change.
    on_change: Callable[[str], None] | None = None

    # The writing mode ("ltr" | "rtl")
    direction: str | None = None

    # If false, the slider handle will not capture focus when value changes.
    focus_thumb_on_change: bool = True

    # If true, the slider will be disabled
    is_disabled: bool | None = None

    # If true, the slider will be in `read-only` state.
    is_read_only: bool | None = None

    # If true, the value will be incremented or decremented in reverse.
    is_reversed: bool | None = None

    # The minimum value of the slider.
    min_: int | None = None

    # The maximum value of the slider.
    max_: int | None = None

    # The minimum distance between slider thumbs. Useful for preventing the thumbs from being too close together.
    min_steps_between_thumbs: int | None = None

    # Function called when the user is done selecting a new value (by dragging or clicking)
    on_changed_end: Callable[[str], None] | None = None

    # Function called when the user starts selecting a new value (by dragging or clicking)
    on_changed_start: Callable[[str], None] | None = None

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
                default_value=self.default_value
                if self.default_value is not None
                else [20, 80],
                on_change=self._get_action(),
                type=self.type_,
            )
        )


class RangeSliderTrack(ChakraComponent):
    """A button component."""

    tag = "RangeSliderTrack"


class RangeSliderFilledTrack(ChakraComponent):
    """A button component."""

    tag = "RangeSliderFilledTrack"


class RangeSliderThumb(ChakraComponent):
    """A button component."""

    tag = "RangeSliderThumb"

    index: int | None = None
