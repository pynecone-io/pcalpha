"""A text component."""
from __future__ import annotations

from typing import Any

from pynecone.components.chakra import ChakraComponent
from pynecone.components.tag import Tag
from pynecone.components.component import Example


class Text(ChakraComponent):
    """Text component is the used to render text and paragraphs within an interface. It renders a p tag by default."""

    tag = "Text"

    # The text to display.
    text: str

    # The CSS `text-align` property
    text_align: str | None = None

    # The CSS `text-transform` property
    casing: str | None = None

    # The CSS `text-decoration` property
    decoration: str | None = None

    # Orientation of text. ("horizontal" | "vertical")
    orientation: str | None = None

    # Override the text element. Tpyes are b, strong, i, em, mark, small, del, ins, sub, and sup.
    as_: str | None = None

    @classmethod
    def create(cls, text: Any, **attrs) -> Text:
        """Create a text component.

        Args:
            text: The text to display.
            **attrs: The attributes to pass to the component.

        Returns:
            The text component.
        """
        return cls(text=str(text), **attrs)

    def _render(self) -> Tag:
        return super()._render().set(contents=self.text)
