"""Container to stack elements with spacing."""

from typing import Callable

from pynecone.components.chakra import ChakraComponent
from pynecone.components.component import Example


class Accordion(ChakraComponent):
    """The wrapper that uses cloneElement to pass props to AccordionItem children."""

    tag = "Accordion"

    # If true, multiple accordion items can be expanded at once.
    allow_multiple: bool | None = None

    # If true, any expanded accordion item can be collapsed again.
    allow_toggle: bool | None = None

    # The initial index(es) of the expanded accordion item
    default_index: int | list[int] | None = None

    # The index(es) of the expanded accordion item
    index: int | list[int] | None = None

    # If true, height animation and transitions will be disabled.
    reduce_motion: bool | None = None

    # The callback invoked when accordion items are expanded or collapsed.
    on_change: Callable[[int], None] | None = None


class AccordionItem(ChakraComponent):
    """A single accordion item."""

    tag = "AccordionItem"

    # A unique id for the accordion item.
    id_: str | None = None

    # If true, the accordion item will be disabled.
    is_disabled: bool | None = None

    # If true, the accordion item will be focusable.
    is_focusable: bool | None = None


class AccordionButton(ChakraComponent):
    """The button that toggles the expand/collapse state of the accordion item. This button must be wrapped in an element with role heading."""

    tag = "AccordionButton"


class AccordionPanel(ChakraComponent):
    """The container for the details to be revealed."""

    tag = "AccordionPanel"


class AccordionIcon(ChakraComponent):
    """A chevron-down icon that rotates based on the expanded/collapsed state."""

    tag = "AccordionIcon"
