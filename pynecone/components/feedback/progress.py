"""Container to stack elements with spacing."""

from pynecone.components.chakra import ChakraComponent
from pynecone.components.component import Example


class Progress(ChakraComponent):
    """A bar to display progress."""

    tag = "Progress"

    # If true, the progress bar will show stripe
    has_striped: bool | None = None

    # If true, and hasStripe is true, the stripes will be animated
    is_animated: bool | None = None

    # If true, the progress will be indeterminate and the value prop will be ignored
    is_indeterminate: bool | None = None

    # The maximum value of the progress
    max_: int | None = None

    # The minimum value of the progress
    min_: int | None = None

    # The value of the progress indicator. If undefined the progress bar will be in indeterminate state
    value: int | None = None

    # The color scheme of the progress bar.
    color_scheme: str | None = None
