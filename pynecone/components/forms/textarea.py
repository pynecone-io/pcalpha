"""A textarea component."""
from typing import Callable

from pynecone import utils
from pynecone.action import ActionSpec
from pynecone.components.chakra import ChakraComponent
from pynecone.components.tag import Tag
from pynecone.property import BaseProperty, Property


class TextArea(ChakraComponent):
    """A text area component."""

    tag = "Textarea"

    # State property to bind the the input.
    value: Property

    # The placeholder text.
    placeholder: str | None = None

    # The type of input.
    type_: str = "text"

    # The function to trigger on change.
    on_change: Callable[[str], None] | None = None

    # The border color when the input is invalid.
    error_border_color: str | None = None

    # The border color when the input is focused.
    focus_border_color: str | None = None

    # If true, the form control will be disabled.
    is_disabled: bool | None = None

    # If true, the form control will be invalid.
    is_invalid: bool | None = None

    # If true, the form control will be readonly.
    is_read_only: bool | None = None

    # If true, the form control will be required.
    is_required: bool | None = None

    # "outline" | "filled" | "flushed" | "unstyled"
    variant: str | None = None

    @property
    def default_placeholder(self) -> str:
        """Get the default placeholder text.

        Returns:
            The default placeholder text.
        """
        return utils.to_title(self.value.name)

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
            args=((self.value.name, "e.target.value"),),
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
                placeholder=self.placeholder
                if self.placeholder is not None
                else self.default_placeholder,
                on_change=self._get_action(),
                type=self.type_,
            )
        )
