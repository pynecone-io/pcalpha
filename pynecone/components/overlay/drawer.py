"""Container to stack elements with spacing."""

from typing import Callable

from pynecone.components.chakra import ChakraComponent
from pynecone.property import BaseProperty, Property
from pynecone.components.component import Example
from pynecone.components.tag import Tag


class Drawer(ChakraComponent):
    """Display a square box."""

    tag = "Drawer"

    # If true, the modal will be open.
    is_open: Property | None = None

    # Callback invoked to close the modal.
    on_close: Callable[[str], None] | None = None

    # Handle zoom/pinch gestures on iOS devices when scroll locking is enabled. Defaults to false.
    allow_pinch_zoom: bool | None = None

    # If true, the modal will autofocus the first enabled and interactive element within the ModalContent
    auto_focus: bool | None = None

    # If true, scrolling will be disabled on the body when the modal opens.
    block_scroll_on_mount: bool | None = None

    # If true, the modal will close when the Esc key is pressed
    close_on_esc: bool | None = None

    # If true, the modal will close when the overlay is clicked
    close_on_overlay_click: bool | None = None

    # If true, the modal will be centered on screen.
    is_centered: bool | None = None

    # If true and drawer's placement is top or bottom, the drawer will occupy the viewport height (100vh)
    is_full_height: bool | None = None

    # Enables aggressive focus capturing within iframes. - If true: keep focus in the lock, no matter where lock is active - If false: allows focus to move outside of iframe
    lock_focus_across_frames: bool | None = None

    # Fires when all exiting nodes have completed animating out
    on_close_complete: Callable[[str], None] | None = None

    # Callback fired when the escape key is pressed and focus is within modal
    on_esc: Callable[[str], None] | None = None

    # Callback fired when the overlay is clicked.
    on_overlay_click: Callable[[str], None] | None = None

    # The placement of the drawer
    placement: str | None = None

    # If true, a `padding-right` will be applied to the body element that's equal to the width of the scrollbar. This can help prevent some unpleasant flickering effect and content adjustment when the modal opens
    preserve_scroll_bar_gap: bool | None = None

    # If true, the modal will return focus to the element that triggered it when it closes.
    return_focus_on_close: bool | None = None

    # "xs" | "sm" | "md" | "lg" | "xl" | "full"
    size: str | None = None

    # A11y: If true, the siblings of the modal will have `aria-hidden` set to true so that screen readers can only see the modal. This is commonly known as making the other elements **inert**
    use_intert: bool | None = None

    # Variant of drawer
    variant: str | None = None

    def _render(self) -> Tag:
        return super()._render().add_attrs(is_open=str(self.is_open))


class DrawerBody(Drawer):
    """Drawer body."""

    tag = "DrawerBody"


class DrawerHeader(Drawer):
    """Drawer header."""

    tag = "DrawerHeader"


class DrawerFooter(Drawer):
    """Drawer footer."""

    tag = "DrawerFooter"


class DrawerOverlay(Drawer):
    """Drawer overlay."""

    tag = "DrawerOverlay"


class DrawerContent(Drawer):
    """Drawer content."""

    tag = "DrawerContent"


class DrawerCloseButton(Drawer):
    """Drawer close button."""

    tag = "DrawerCloseButton"
