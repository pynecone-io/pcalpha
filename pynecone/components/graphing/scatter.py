"""Component for displaying a Scatter graph."""

import json

from pynecone import utils
from pynecone.components.library_component import LibraryComponent
from pynecone.components.tag import Tag


class NivoScatter(LibraryComponent):
    """A component that wraps a Rebass component."""

    library = "@nivo/scatterplot"


class Scatter(NivoScatter):
    """Display a Scatter graph."""

    tag = "ResponsiveScatterPlot"

    # Chart data.
    data: list[dict] | None = None

    # Chart width.
    width: int | None = None

    # Chart height.
    height: int | None = None

    # Chart margin.
    margin: dict | None = None
