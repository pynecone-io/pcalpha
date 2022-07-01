"""A button component."""

from pynecone.components.chakra import ChakraComponent
from pynecone.components.component import Example


class Button(ChakraComponent):
    """The Button component is used to trigger an action or event, such as submitting a form, opening a dialog, canceling an action, or performing a delete operation."""

    tag = "Button"

    # The type of button.
    type: str | None = None

    # The space between the button icon and label.
    icon_spacing: int | None = None

    # If true, the button will be styled in its active state.
    is_active: bool | None = None

    # If true, the button will be styled in its disabled state.
    is_disabled: bool | None = None

    # If true, the button will take up the full width of its container.
    is_full_width: bool | None = None

    # If true, the button will show a spinner.
    is_loading: bool | None = None

    # The label to show in the button when isLoading is true If no text is passed, it only shows the spinner.
    loading_text: str | None = None

    #  "lg" | "md" | "sm" | "xs"
    size: str | None = None

    # "ghost" | "outline" | "solid" | "link" | "unstyled"
    variant: str | None = None

    # Built in color scheme for ease of use.
    color_scheme: str | None = None


class ButtonGroup(ChakraComponent):
    """A group of buttons."""

    tag = "ButtonGroup"

    # If true, the borderRadius of button that are direct children will be altered to look flushed together.
    is_attached: bool | None = None

    # If true, all wrapped button will be disabled.
    is_disabled: bool | None = None

    # The spacing between the buttons.
    spacing: int | None = None
