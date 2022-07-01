"""A box component that can contain other components."""

from pynecone.components.chakra import ChakraComponent
from pynecone.components.tag import Tag
from pynecone.components.component import Example


class Box(ChakraComponent):
    """Renders a box component that can contain other components."""

    tag = "Box"

    # The element to render.
    element: str | None = None

    def _render(self) -> Tag:
        return (
            super()
            ._render()
            .add_attrs(
                **{
                    "as": self.element,
                }
            )
        )
