"""Popover components."""

from typing import Callable

from pynecone.components.chakra import ChakraComponent
from pynecone.components.text_display import TextDisplay


class Popover(ChakraComponent):
    """The wrapper that provides props, state, and context to its children."""

    tag = "Popover"

    # The padding required to prevent the arrow from reaching the very edge of the popper.
    arrow_padding: int | None = None

    # The `box-shadow` of the popover arrow
    arrow_shadow_color: str | None = None

    # The size of the popover arrow
    arrow_size: int | None = None

    # If true, focus will be transferred to the first interactive element when the popover opens
    auto_focus: bool | None = None

    # The boundary area for the popper. Used within the preventOverflow modifier
    boundary: str | None = None

    # If true, the popover will close when you blur out it by clicking outside or tabbing out
    close_on_blur: bool | None = None

    # If true, the popover will close when you hit the Esc key
    close_on_esc: bool | None = None

    # If true, the popover will be initially opened.
    default_is_open: bool | None = None

    # Theme direction ltr or rtl. Popper's placement will be set accordingly
    direction: str | None = None

    # If true, the popper will change its placement and flip when it's about to overflow its boundary area.
    flip: bool | None = None

    # The distance or margin between the reference and popper. It is used internally to create an offset modifier. NB: If you define offset prop, it'll override the gutter.
    gutter: int | None = None

    # The html id attribute of the popover. If not provided, we generate a unique id. This id is also used to auto-generate the `aria-labelledby` and `aria-describedby` attributes that points to the PopoverHeader and PopoverBody
    id_: str | None = None

    # Performance 🚀: If true, the PopoverContent rendering will be deferred until the popover is open.
    is_lazy: bool | None = None

    # Performance 🚀: The lazy behavior of popover's content when not visible. Only works when `isLazy={true}` - "unmount": The popover's content is always unmounted when not open. - "keepMounted": The popover's content initially unmounted, but stays mounted when popover is open.
    lazy_behavior: str | None = None

    # If true, the popover will be opened in controlled mode.
    is_open: bool | None = None

    # If true, the popper will match the width of the reference at all times. It's useful for autocomplete, `date-picker` and select patterns.
    match_width: bool | None = None

    # Action when the popover is closed.
    on_close: Callable[[str], None] | None = None

    # Action when the popover is opened.
    on_open: Callable[[str], None] | None = None

    # The placement of the popover. It's used internally by Popper.js.
    placement: str | None = None

    # If true, will prevent the popper from being cut off and ensure it's visible within the boundary area.
    prevent_overflow: bool | None = None

    # If true, focus will be returned to the element that triggers the popover when it closes
    return_focus_on_close: bool | None = None

    # The CSS positioning strategy to use. ("fixed" | "absolute")
    strategy: str | None = None

    # The interaction that triggers the popover. hover - means the popover will open when you hover with mouse or focus with keyboard on the popover trigger click - means the popover will open on click or press Enter to Space on keyboard ("click" | "hover")
    trigger: str | None = None


class PopoverContent(Popover):
    """The popover itself."""

    tag = "PopoverContent"


class PopoverHeader(TextDisplay):
    """The header of the popover."""

    tag = "PopoverHeader"


class PopoverFooter(TextDisplay):
    """Display a popover footer."""

    tag = "PopoverFooter"


class PopoverBody(TextDisplay):
    """The body of the popover."""

    tag = "PopoverBody"


class PopoverArrow(Popover):
    """A visual arrow that points to the reference (or trigger)."""

    tag = "PopoverArrow"


class PopoverCloseButton(Popover):
    """A button to close the popover."""

    tag = "PopoverCloseButton"


class PopoverAnchor(Popover):
    """Used to wrap the position-reference element."""

    tag = "PopoverAnchor"


class PopoverTrigger(Popover):
    """Used to wrap the reference (or trigger) element."""

    tag = "PopoverTrigger"
