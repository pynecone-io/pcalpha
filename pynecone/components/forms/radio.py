"""A button component."""


from typing import Callable

from pynecone import utils
from pynecone.action import ActionSpec
from pynecone.components.chakra import ChakraComponent
from pynecone.components.tag import Tag
from pynecone.components.typography.text import Text
from pynecone.property import BaseProperty, Property


class RadioGroup(ChakraComponent):
    """A grouping of individual radio options."""

    tag = "RadioGroup"

    # State property to bind the the input.
    value: Property

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
            )
        )


class Radio(Text):
    """Radios are used when only one choice may be selected in a series of options."""

    tag = "Radio"

    # Value of button.
    value: str | None = None

    # If true, the radio will be initially checked.
    default_checked: bool | None = None

    # If true, the radio will be checked. You'll need to pass onChange to update its value (since it is now controlled)
    is_checked: bool | None = None

    # If true, the radio will be disabled.
    is_disabled: bool | None = None

    # If true, the radio button will be invalid. This also sets `aria-invalid` to true.
    is_invalid: bool | None = None

    # If true, the radio will be read-only
    is_read_only: bool | None = None

    # If true, the radio button will be required. This also sets `aria-required` to true.
    is_required: bool | None = None
