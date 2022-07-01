"""Component for displaying a Line graph."""

import json

from pynecone import utils
from pynecone.components.library_component import LibraryComponent
from pynecone.components.tag import Tag


class NivoLine(LibraryComponent):
    """A component that wraps a Rebass component."""

    library = "@nivo/line"


class Line(NivoLine):
    """Display a Line graph."""

    tag = "ResponsiveLine"

    # Chart data.
    data: list[dict] | None = None

    # Chart width.
    width: int | None = None

    # Chart height.
    height: int | None = None

    # Chart margin.
    margin: dict | None = None
