"""A code component."""

import json

import black

from pynecone import utils
from pynecone.components.library_component import LibraryComponent
from pynecone.components.tag import Tag


class Code(LibraryComponent):
    """A code block."""

    library = "react-syntax-highlighter"

    tag = "ReactSyntaxHighlighter"

    # The source code to display.
    text: str

    # The language to use.
    language: str | None = None

    # If this is enabled line numbers will be shown next to the code block.
    show_line_numbers: bool | None = None

    # A custon style for the code block.
    custom_style: dict | None = None

    @classmethod
    def create(cls, code: str, **attrs):
        """Create a text component.

        Args:
            code: The code to display.
            **attrs: The attributes to pass to the component.

        Returns:
            The text component.
        """
        if attrs.get("language") == "python":
            code = black.format_str(code, mode=black.FileMode())
        return cls(text=code, **attrs)

    def _render(self) -> Tag:
        return super()._render().set(contents=utils.wrap(json.dumps(self.text), "{"))
