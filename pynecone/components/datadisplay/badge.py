"""Badge component."""

from pynecone.components.text_display import TextDisplay


class Badge(TextDisplay):
    """A badge component."""

    tag = "Badge"

    # Variant of the badge ("solid" | "subtle" | "outline")
    variant: str | None = None

    # The color of the badge
    color_scheme: str | None = None
