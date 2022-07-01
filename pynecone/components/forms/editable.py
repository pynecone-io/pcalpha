"""An editable component."""

from typing import Callable

from pynecone import utils
from pynecone.action import ActionSpec
from pynecone.components.chakra import ChakraComponent
from pynecone.components.tag import Tag
from pynecone.property import BaseProperty, Property


class Editable(ChakraComponent):
    """The wrapper component that provides context value."""

    tag = "Editable"

    # If true, the Editable will be disabled.
    is_disabled: bool | None = None

    # If true, the read only view, has a tabIndex set to 0 so it can receive focus via the keyboard or click.
    is_preview_focusable: bool | None = None

    # The placeholder text when the value is empty.
    placeholder: str | None = None

    # If true, the input's text will be highlighted on focus.
    select_all_on_focus: bool | None = None

    # If true, the Editable will start with edit mode by default.
    start_with_edit_view: bool | None = None

    # If true, it'll update the value onBlur and turn off the edit mode.
    submit_on_blur: bool | None = None

    # The value of the Editable in both edit & preview mode
    value: Property | None = None

    # The type of Editable.
    type_: str = "text"

    # The initial value of the Editable in both edit and preview mode.
    default_value: str | None = None

    # Callback invoked when user cancels input with the Esc key. It provides the last confirmed value as argument.
    on_cancel: Callable[[str], None] | None = None

    # Callback invoked when user changes input.
    on_change: Callable[[str], None] | None = None

    # Callback invoked once the user enters edit mode.
    on_edit: Callable[[str], None] | None = None

    # Callback invoked when user confirms value with enter key or by blurring input.
    on_submit: Callable[[str], None] | None = None

        
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



    

class EditableInput(ChakraComponent):
    """The edit view of the component. It shows when you click or focus on the text."""

    tag = "EditableInput"


class EditableTextarea(ChakraComponent):
    """Use the textarea element to handle multi line text input in an editable context."""

    tag = "EditableTextarea"


class EditablePreview(ChakraComponent):
    """The read-only view of the component."""

    tag = "EditablePreview"
