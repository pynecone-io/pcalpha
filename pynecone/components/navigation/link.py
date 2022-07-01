"""A link component."""

from pynecone.components.text_display import TextDisplay


class Link(TextDisplay):
    """Component the provides a link."""

    tag = "Link"

    # The page to link to.
    href: str | None = None

    # The text to display.
    text: str | None = None

    # If true, the link will open in new tab.
    is_external: bool = False
