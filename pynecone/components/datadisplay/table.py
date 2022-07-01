"""Table components."""

from pynecone.components.chakra import ChakraComponent


class Table(ChakraComponent):
    """A table component."""

    tag = "Table"


class Thead(Table):
    """A table header component."""

    tag = "Thead"


class Tbody(Table):
    """A table body component."""

    tag = "Tbody"


class Tfoot(Table):
    """A table footer component."""

    tag = "Tfoot"


class Tr(Table):
    """A table row component."""

    tag = "Tr"


class Th(ChakraComponent):
    """A table header cell component."""

    tag = "Th"

    # Aligns the cell content to the right.
    is_numeric: bool | None = None


class Td(ChakraComponent):
    """A table data cell component."""

    tag = "Td"

    # Aligns the cell content to the right.
    is_numeric: bool | None = None


class TableCaption(ChakraComponent):
    """A table caption component."""

    tag = "TableCaption"

    # The placement of the table caption. This sets the `caption-side` CSS attribute.
    placement: str | None = None


class TableContainer(ChakraComponent):
    """The table container component renders a div that wraps the table component."""

    tag = "TableContainer"
