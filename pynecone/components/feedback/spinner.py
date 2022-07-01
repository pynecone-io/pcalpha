"""Container to stack elements with spacing."""

from pynecone.components.chakra import ChakraComponent
from pynecone.components.component import Example


class Spinner(ChakraComponent):
    """The component that spins."""

    tag = "Spinner"

    # The color of the empty area in the spinner
    empty_color: str | None = None

    # For accessibility, it is important to add a fallback loading text. This text will be visible to screen readers.
    label: str | None = None

    # The speed of the spinner must be as a string and in seconds '1s'. Default is '0.45s'.
    speed: str | None = None

    # The thickness of the spinner.
    thickness: int | None = None

    # "xs" | "sm" | "md" | "lg" | "xl"
    size: str | None = None
