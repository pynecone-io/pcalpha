"""A line to divide parts of the layout."""

from pynecone.components.chakra import ChakraComponent


class Divider(ChakraComponent):
    """Dividers are used to visually separate content in a list or group."""

    tag = "Divider"

    # Pass the orientation prop and set it to either horizontal or vertical. If the vertical orientation is used, make sure that the parent element is assigned a height.
    orientation: str | None = None

    # Variant of the divider ("solid" | "dashed")
    variant: str | None = None
