"""List components."""

from pynecone.components.chakra import ChakraComponent
from pynecone.components.typography.text import Text


class List(ChakraComponent):
    """List component is used to display list items. It renders a ul element by default."""

    tag = "List"

    # The space between each list item
    spacing: str | None = None

    # Shorthand prop for listStylePosition
    style_position: str | None = None

    # Shorthand prop for listStyleType
    style_type: str | None = None


class ListItem(ChakraComponent):
    """ListItem composes Box so you can pass all style and pseudo style props."""

    tag = "ListItem"


class ListIcon(ChakraComponent):
    """A list icon component."""

    tag = "ListIcon"


class OrderedList(ChakraComponent):
    """An ordered list component."""

    tag = "OrderedList"


class UnorderedList(ChakraComponent):
    """An unordered list component."""

    tag = "UnorderedList"
