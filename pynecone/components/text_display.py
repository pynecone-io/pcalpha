"""Components that are based on Chakra-UI."""
from __future__ import annotations

from typing import Any

from pynecone.components.chakra import ChakraComponent
from pynecone.components.typography.text import Text


class TextDisplay(ChakraComponent):
    """A component that only has text as a child."""

    @classmethod
    def create(cls, text: Any, **attrs) -> TextDisplay:
        """Create a text display component.

        Args:
            text: The text to display.
            **attrs: The attributes to pass to the component.

        Returns:
            The text display component.
        """
        return cls(children=[Text(text=str(text))], **attrs)
