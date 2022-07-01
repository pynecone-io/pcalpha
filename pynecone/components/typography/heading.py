"""A heading component."""

from pynecone.components.tag import Tag
from pynecone.components.typography.text import Text
from pynecone.components.component import Example


class Heading(Text):
    """Heading composes Box so you can use all the style props and add responsive styles as well. It renders an h2 tag by default."""

    tag = "Heading"

    # Orientation of text. ("horizontal" | "vertical")
    orientation: str | None = None

    # "4xl" | "3xl" | "2xl" | "xl" | "lg" | "md" | "sm" | "xs"
    size: str | None = None

    # Usage examples
    _examples = [
        Example(
            description="An example of an unstyled heading component.",
            code="""
pc.heading("Example")
""",
        )
    ]
