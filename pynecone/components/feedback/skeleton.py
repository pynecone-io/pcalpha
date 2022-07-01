"""Container to stack elements with spacing."""

from pynecone.components.chakra import ChakraComponent
from pynecone.components.component import Example


class Skeleton(ChakraComponent):
    """Skeleton is used to display the loading state of some components. You can use it as a standalone component. Or to wrap another component to take the same height and width."""

    tag = "Skeleton"

    # The color at the animation end
    end_color: str | None = None

    # The fadeIn duration in seconds
    fade_duration: float | None = None

    # If true, it'll render its children with a nice fade transition
    is_loaded: bool | None = None

    # The animation speed in seconds
    speed: float | None = None

    # The color at the animation start
    start_color: str | None = None


class SkeletonCircle(ChakraComponent):
    """SkeletonCircle is used to display the loading state of some components."""

    tag = "SkeletonCircle"

    # The color at the animation end
    end_color: str | None = None

    # The fadeIn duration in seconds
    fade_duration: float | None = None

    # If true, it'll render its children with a nice fade transition
    is_loaded: bool | None = None

    # The animation speed in seconds
    speed: float | None = None

    # The color at the animation start
    start_color: str | None = None


class SkeletonText(ChakraComponent):
    """SkeletonText is used to display the loading state of some components."""

    tag = "SkeletonText"

    # The color at the animation end
    end_color: str | None = None

    # The fadeIn duration in seconds
    fade_duration: float | None = None

    # If true, it'll render its children with a nice fade transition
    is_loaded: bool | None = None

    # The animation speed in seconds
    speed: float | None = None

    # The color at the animation start
    start_color: str | None = None

    # Number is lines of text.
    no_of_lines: int | None = None
