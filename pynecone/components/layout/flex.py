"""A reflexive container component."""

from pynecone.components.chakra import ChakraComponent
from pynecone.components.component import Example


class Flex(ChakraComponent):
    """Flex is Box with display, flex and comes with helpful style shorthand. It renders a div element."""

    tag = "Flex"

    # How to align items in the flex.
    align: str | None = None

    # Shorthand for flexBasis style prop
    basis: str | None = None

    # Shorthand for flexDirection style prop
    direction: str | None = None

    # Shorthand for flexGrow style prop
    grow: str | None = None

    # The way to justify the items.
    justify: str | None = None

    # Shorthand for flexWrap style prop
    wrap: str | None = None

    # Shorthand for flexShrink style prop
    shrink: str | None = None
