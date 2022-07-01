"""Components that are based on Chakra-UI."""

from pynecone.components.library_component import LibraryComponent


class ChakraComponent(LibraryComponent):
    """A component that wraps a Rebass component."""

    library = "@chakra-ui/react"
