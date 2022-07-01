"""Component for displaying a bar graph."""

import json

from pynecone import utils
from pynecone.components.library_component import LibraryComponent
from pynecone.components.tag import Tag


class NivoBar(LibraryComponent):
    """A component that wraps a Rebass component."""

    library = "@nivo/bar"


class Bar(NivoBar):
    """Display a bar graph."""

    tag = "ResponsiveBar"

    # Chart data.
    data: list[dict] | None = None

    # Keys to use to determine each serie.
    keys: list[str] | None = None

    # Key to use to index the data.
    index_by: str | None = None

    # How to group bars. ('grouped' | 'stacked')
    group_mode: str | None = None

    # How to display bars. ('horizontal' | 'vertical')
    layout: str | None = None

    # Value scale configuration. ('linear')
    value_scale: str | None = None

    # Index scale configuration.
    index_scale: str | None = None

    # Reverse bars, starts on top instead of bottom for vertical layout and right instead of left for horizontal one.
    reverse: bool | None = None

    # Minimum value.
    min_value: int | None = None

    # Maximum value.
    max_value: int | None = None
