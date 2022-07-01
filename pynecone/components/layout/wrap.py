"""Container to stack elements with spacing."""

from pynecone.components.chakra import ChakraComponent
from pynecone.components.component import Example


class Wrap(ChakraComponent):
    """Wrap composes the Box component and renders a ul tag"""

    tag = "Wrap"


class WrapItem(ChakraComponent):
    """WrapItem composes the Box component and renders the HTML li tag"""

    tag = "WrapItem"
