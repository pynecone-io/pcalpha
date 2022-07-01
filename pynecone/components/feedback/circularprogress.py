"""Container to stack elements with spacing."""

from pynecone.components.chakra import ChakraComponent
from pynecone.components.text_display import TextDisplay
from pynecone.components.component import Example


class CircularProgress(ChakraComponent):
    """The CircularProgress component is used to indicate the progress for determinate and indeterminate processes."""

    tag = "CircularProgress"

    # If true, the cap of the progress indicator will be rounded.
    cap_is_round: bool | None = None

    # If true, the progress will be indeterminate and the value prop will be ignored
    is_indeterminate: bool | None = None

    # Maximum value defining 100% progress made (must be higher than 'min')
    max_: int | None = None

    # Minimum value defining 'no progress' (must be lower than 'max')
    min_: int | None = None

    # This defines the stroke width of the svg circle.
    thickness: int | None = None

    # The color name of the progress track. Use a color key in the theme object
    track_color: str | None = None

    # Current progress (must be between min/max).
    value: int | None = None

    # The desired valueText to use in place of the value.
    value_text: str | None = None


class CircularProgressLabel(TextDisplay):
    """Label of CircularProcess."""

    tag = "CircularProgressLabel"
