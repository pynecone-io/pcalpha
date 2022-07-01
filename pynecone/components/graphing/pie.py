"""Component for displaying a pie chart."""

import json

from pynecone import utils
from pynecone.components.library_component import LibraryComponent
from pynecone.components.tag import Tag


class NivoPie(LibraryComponent):
    """A Nivo Pie component."""

    library = "@nivo/pie"


class Pie(NivoPie):
    """Display a bar graph."""

    tag = "ResponsivePie"

    # Chart data.
    data: list[dict] | None = None

    # ID accessor which should return a unique value for the whole dataset.
    id_: str | None = None

    # Value accessor.
    value: str | None = None

    # Chart width.
    width: int | None = None

    # Chart height.
    height: int | None = None

    # Start angle (in degrees), useful to make gauges for example.
    start_angle: int | None = None

    # End angle (in degrees), useful to make gauges for example.
    end_angle: int | None = None

    # Donut chart if greater than 0. Value should be between 0~1 as it's a ratio from original radius.
    inner_radius: int | None = None

    # Padding between each pie slice.
    pad_angle: int | None = None

    # Rounded slices.
    corner_radius: int | None = None

    # If 'true', arcs will be ordered according to their associated value.
    sort_by_value: bool | None = None

    # Chart margin.
    margin: dict | None = None
