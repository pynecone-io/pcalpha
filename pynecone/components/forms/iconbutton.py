"""A button component."""

from pynecone.components.chakra import ChakraComponent
from pynecone.components.typography.text import Text


class IconButton(Text):
    """A button that can be clicked."""

    tag = "IconButton"

    # The type of button.
    type: str | None = None

    #  A label that describes the button
    aria_label: str | None = None

    # The icon to be used in the button.
    icon: str | None = None

    # If true, the button will be styled in its active state.
    is_active: bool | None = None

    # If true, the button will be disabled.
    is_disabled: bool | None = None

    # If true, the button will show a spinner.
    is_loading: bool | None = None

    # If true, the button will be perfectly round. Else, it'll be slightly round
    is_round: bool | None = None

    # Replace the spinner component when isLoading is set to true
    spinner: str | None = None
