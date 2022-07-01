"""A link component."""

from pynecone.components.text_display import TextDisplay
from pynecone.components.library_component import LibraryComponent


class NextLinkLib(LibraryComponent):
    """A component that wraps a Rebass component."""

    library = "next/link"


class NextLink(NextLinkLib):
    """Links are accessible elements used primarily for navigation. This component is styled to resemble a hyperlink and semantically renders an <a>."""

    tag = "NextLink"

    # The page to link to.
    href: str | None = None

    # The page to link to.
    pass_href: bool = True
