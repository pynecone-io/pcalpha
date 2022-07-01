"""A flexbox container."""

from pynecone.components.chakra import ChakraComponent
from pynecone.components.component import Example


class Container(ChakraComponent):
    """Container composes Box so you can pass all Box related props in addition to this."""

    tag = "Container"

    # If true, container will center its children regardless of their width.
    center_content: bool | None = None
