"""Component for displaying a Radar chart."""

import json

from pynecone import utils
from pynecone.components.library_component import LibraryComponent
from pynecone.components.tag import Tag


class NivoRadar(LibraryComponent):
    """A Nivo Radar component."""

    library = "@nivo/Radar"


class Radar(NivoRadar):
    """Display a bar graph."""

    tag = "ResponsiveRadar"

    # Chart data.
    data: list[dict] | None = None

    # Key to use to index the data.
    index_by: str | None = None

    # Keys to use to determine each serie.
    keys: list[str] | None = None

    # Maximum value.
    max_value: int | None = None

    # Chart width.
    width: int | None = None

    # Chart height.
    height: int | None = None

    # Chart margin.
    margin: dict | None = None
