"""Handle styling."""

from enum import Enum
from typing import Any


class StyleEnum(str, Enum):
    """An enum over a set of styles."""


TEXT_ALIGN = "textAlign"
BACKGROUND = "bg"
BG = BACKGROUND
COLOR = "color"


class TextAlign(StyleEnum):
    """Text alignment."""

    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"
    JUSTIFY = "justify"


Style = dict[str, Any]
