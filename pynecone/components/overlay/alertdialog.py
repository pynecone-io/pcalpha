"""Alert dialog components."""
from typing import Callable

from pynecone.components.chakra import ChakraComponent
from pynecone.components.text_display import TextDisplay
from pynecone.property import BaseProperty, Property
from pynecone.components.component import Example
from pynecone.components.tag import Tag


class AlertDialog(ChakraComponent):
    """Provides context and state for the dialog."""

    tag = "AlertDialog"

    # If true, the modal will be open.
    is_open: Property | None = None

    # The least destructive element to focus when the dialog opens.
    least_destructive_ref: str | None = None

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

    # Enables aggressive focus capturing within iframes. If true, keep focus in the lock, no matter where lock is active. If false, allows focus to move outside of iframe.
    lock_focus_across_frames: bool | None = None

    # Fires when all exiting nodes have completed animating out
    on_close_complete: Callable[[str], None] | None = None

    # Callback fired when the escape key is pressed and focus is within modal
    on_esc: Callable[[str], None] | None = None

    # Callback fired when the overlay is clicked.
    on_overlay_click: Callable[[str], None] | None = None

    # If true, a `padding-right` will be applied to the body element that's equal to the width of the scrollbar. This can help prevent some unpleasant flickering effect and content adjustment when the modal opens
    preserve_scroll_bar_gap: bool | None = None

    # If true, the modal will return focus to the element that triggered it when it closes.
    return_focus_on_close: bool | None = None

    # "xs" | "sm" | "md" | "lg" | "xl" | "2xl" | "3xl" | "4xl" | "5xl" | "6xl" | "full"
    size: str | None = None

    # If true, the siblings of the modal will have `aria-hidden` set to true so that screen readers can only see the modal. This is commonly known as making the other elements **inert**
    use_intert: bool | None = None

    def _render(self) -> Tag:
        return super()._render().add_attrs(is_open=str(self.is_open))


class AlertDialogBody(ChakraComponent):
    """Should contain the description announced by screen readers."""

    tag = "AlertDialogBody"


class AlertDialogHeader(ChakraComponent):
    """Should contain the title announced by screen readers."""

    tag = "AlertDialogHeader"


class AlertDialogFooter(ChakraComponent):
    """Should contain the actions of the dialog."""

    tag = "AlertDialogFooter"


class AlertDialogContent(ChakraComponent):
    """The wrapper for the alert dialog's content."""

    tag = "AlertDialogContent"


class AlertDialogOverlay(ChakraComponent):
    """The dimmed overlay behind the dialog."""

    tag = "AlertDialogOverlay"


class AlertDialogCloseButton(ChakraComponent):
    """The button that closes the dialog."""

    tag = "AlertDialogCloseButton"
