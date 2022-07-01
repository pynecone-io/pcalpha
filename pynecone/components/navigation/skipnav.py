"""An image component."""

from pynecone.components.chakra import ChakraComponent


class SkipNavLink(ChakraComponent):
    """Skip Navigation link and destination container for screen readers and keyboard users. The SkipNavLink component composes the Box component."""

    tag = "SkipNavLink"


class SkipNavContent(ChakraComponent):
    """Display a skip navigation content. The SkipNavContent component composes the Box component and renders a div."""

    tag = "SkipNavContent"
