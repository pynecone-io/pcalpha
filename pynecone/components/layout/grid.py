"""Container to stack elements with spacing."""

from pynecone.components.chakra import ChakraComponent
from pynecone.components.component import Example


class Grid(ChakraComponent):
    """The main wrapper of th egrid component."""

    tag = "Grid"

    # Shorthand prop for gridAutoColumns
    auto_columns: str | None = None

    # Shorthand prop for gridAutoFlow
    auto_flow: str | None = None

    # Shorthand prop for gridAutoRows
    auto_rows: str | None = None

    # Shorthand prop for gridColumn
    column: str | None = None

    # Shorthand prop for gridRow
    row: str | None = None

    # Shorthand prop for gridTemplateColumns
    template_columns: str | None = None

    # Shorthand prop for gridTemplateRows
    template_rows: str | None = None


class GridItem(ChakraComponent):
    """Used as a child of Grid to control the span, and start positions within the grid."""

    tag = "GridItem"

    # Shorthand prop for gridArea
    area: str | None = None

    # Shorthand prop for gridColumnEnd
    col_end: str | None = None

    # The column number the grid item should start.
    col_start: int | None = None

    # The number of columns the grid item should span.
    col_span: int | None = None

    # Shorthand prop for gridRowEnd
    row_end: str | None = None

    # The row number the grid item should start.
    row_start: int | None = None

    # The number of rows the grid item should span.
    row_span: int | None = None
