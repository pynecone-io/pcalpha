"""Tooltip components."""

from typing import Callable

from pynecone.components.chakra import ChakraComponent


class Tooltip(ChakraComponent):
    """A tooltip message to appear."""

    tag = "Tooltip"

    # The padding required to prevent the arrow from reaching the very edge of the popper.
    arrow_padding: int | None = None

    # The color of the arrow shadow.
    arrow_shadow_color: str | None = None

    # Size of the arrow.
    arrow_size: int | None = None

    # Delay (in ms) before hiding the tooltip
    delay: int | None = None

    # If true, the tooltip will hide on click
    close_on_click: bool | None = None

    # If true, the tooltip will hide on pressing Esc key
    close_on_esc: bool | None = None

    # If true, the tooltip will hide while the mouse is down
    close_on_mouse_down: bool | None = None

    # If true, the tooltip will be initially shown
    default_is_open: bool | None = None

    # Theme direction ltr or rtl. Popper's placement will be set accordingly
    direction: str | None = None

    # The distance or margin between the reference and popper. It is used internally to create an offset modifier. NB: If you define offset prop, it'll override the gutter.
    gutter: int | None = None

    # If true, the tooltip will show an arrow tip
    has_arrow: bool | None = None

    # If true, th etooltip with be disabled.
    is_disabled: bool | None = None

    # If true, the tooltip will be open.
    is_open: bool | None = None

    # The label of the tooltip
    label: str | None = None

    # Callback to run when the tooltip hides
    on_close: Callable[[str], None] | None = None

    # Callback to run when the tooltip shows
    on_open: Callable[[str], None] | None = None

    # Delay (in ms) before showing the tooltip
    open_delay: int | None = None

    # The placement of the popper relative to its reference.
    placement: str | None = None

    # If true, the tooltip will wrap its children in a `<span/>` with `tabIndex=0`
    should_wrap_children: bool | None = None
