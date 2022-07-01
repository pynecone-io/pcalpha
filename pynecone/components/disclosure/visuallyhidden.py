"""Components that can be hidden."""

from pynecone.components.chakra import ChakraComponent


class VisuallyHidden(ChakraComponent):
    """Visually hidden span component used to hide elements on screen."""

    tag = "VisuallyHidden"


class VisuallyHiddenInput(ChakraComponent):
    """Visually hidden input component used for designing custom input components using the html input as a proxy."""

    tag = "VisuallyHiddenInput"
