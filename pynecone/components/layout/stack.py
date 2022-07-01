"""Container to stack elements with spacing."""

from pynecone.components.chakra import ChakraComponent
from pynecone.components.component import Example


class Stack(ChakraComponent):
    """Display a square box."""

    tag = "Stack"

    # Shorthand for alignItems style prop
    align_items: str | None = None

    # The direction to stack the items.
    direction: str | None = None

    # If true the items will be stacked horizontally.
    is_inline: bool | None = None

    # Shorthand for justifyContent style prop
    justify_content: str | None = None

    # If true, the children will be wrapped in a Box, and the Box will take the spacing props
    should_wrap_children: bool | None = None

    # The space between each stack item
    spacing: str | None = None

    # Shorthand for flexWrap style prop
    wrap: str | None = None

    # Alignment of contents.
    justify: str | None = None


class Hstack(Stack):
    """The HStack component is a component which is only facing the horizontal direction. Additionally you can add a divider and horizontal spacing between the items."""

    tag = "HStack"

    # Usage examples
    _examples = [
        Example(
            description="An example a horizontal stack.",
            code="""
pc.hstack(
    pc.box('Example', bg = 'red', color = 'white', border_radius='md',  width = '10%'),
    pc.box('Example', bg = 'orange', color = 'white', border_radius='md',  width = '10%'),
    pc.box('Example', bg = 'yellow', color = 'white', border_radius='md',  width = '10%'),
    pc.box('Example', bg = 'lightblue', color = 'white', border_radius='md',  width = '10%'),
    pc.box('Example', bg = 'lightgreen', color = 'white', border_radius='md', width = '100%'),
    width = '100%'
)
""",
        )
    ]


class Vstack(Stack):
    """The VStack component is a component which is only facing the vertical direction. Additionally you can add a divider and vertical spacing between the items."""

    tag = "VStack"

    # Usage examples
    _examples = [
        Example(
            description="An example vertical stack.",
            code="""
pc.vstack(
    pc.box('Example', bg = 'red', color = 'white', border_radius='md',  width = '20%'),
    pc.box('Example', bg = 'orange', color = 'white', border_radius='md',  width = '40%'),
    pc.box('Example', bg = 'yellow', color = 'white', border_radius='md',  width = '60%'),
    pc.box('Example', bg = 'lightblue', color = 'white', border_radius='md',  width = '80%'),
    pc.box('Example', bg = 'lightgreen', color = 'white', border_radius='md', width = '100%'),
    width = '100%'
)
""",
        )
    ]
