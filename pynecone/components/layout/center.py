"""A box that centers its contents."""
from pynecone.components.component import Example

from pynecone.components.chakra import ChakraComponent


class Center(ChakraComponent):
    """Center is a layout component that centers its child within itself."""

    tag = "Center"

    # Usage examples
    _examples = [
        Example(
            description="An example of a variety of styled boxes.",
            code="""
pc.center('Example', bg = 'lightgreen', color = 'white', border_radius='md', width = '50%')
""",
        )
    ]


class Square(ChakraComponent):
    """Square centers its child given size (width and height)."""

    tag = "Square"

    # Usage examples
    _examples = [
        Example(
            description="An example of a variety of styled boxes.",
            code="""
pc.square('Example', bg = 'lightgreen', color = 'white', width='100px')
""",
        )
    ]


class Circle(ChakraComponent):
    """Circle a Square with round border-radius."""

    tag = "Circle"

    # Usage examples
    _examples = [
        Example(
            description="An example of a variety of styled boxes.",
            code="""
pc.center(
    pc.circle("1", bg = 'lightgreen', color = 'white'),
    width='100px',
    height='100px'
)
""",
        )
    ]
