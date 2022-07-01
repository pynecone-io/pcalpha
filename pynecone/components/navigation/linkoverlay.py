"""Link overlay components."""

from pynecone.components.chakra import ChakraComponent
from pynecone.components.text_display import TextDisplay


class LinkOverlay(TextDisplay):
    """Wraps cild componet in a link."""

    tag = "LinkOverlay"

    # If true, the link will open in new tab
    is_external: bool | None = None

    # Href of the link overlay.
    href: str | None = None


class LinkBox(ChakraComponent):
    """The LinkBox lifts any nested links to the top using z-index to ensure proper keyboard navigation between links."""

    tag = "LinkBox"
