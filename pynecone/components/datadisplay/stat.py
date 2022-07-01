"""Statistics components."""

from pynecone.components.chakra import ChakraComponent
from pynecone.components.text_display import TextDisplay


class Stat(ChakraComponent):
    """As the name implies, the Stat component is used to display some statistics."""

    tag = "Stat"


class StatLabel(ChakraComponent):
    """A stat label component."""

    tag = "StatLabel"


class StatNumber(ChakraComponent):
    """A stat number component."""

    tag = "StatNumber"


class StatHelpText(ChakraComponent):
    """A stat help text component."""

    tag = "StatHelpText"


class StatArrow(ChakraComponent):
    """A stat arrow component."""

    tag = "StatArrow"

    # increase or decrease
    type_: str | None = None


class StatGroup(ChakraComponent):
    """A stat group component."""

    tag = "StatGroup"
