"""Avatar components."""

from typing import Callable

from pynecone.components.chakra import ChakraComponent


class Avatar(ChakraComponent):
    """The image that represents the user."""

    tag = "Avatar"

    # Function to get the initials to display.
    get_initials: str | None = None

    # The default avatar used as fallback when name, and src is not specified.
    icon: str | None = None

    # The label of the icon.
    icon_label: str | None = None

    # If true, opt out of the avatar's fallback logic and renders the img at all times.
    ignore_fallback: bool | None = None

    # Defines loading strategy ("eager" | "lazy")
    loading: str | None = None

    # The name of the person in the avatar. - if src has loaded, the name will be used as the alt attribute of the img - If src is not loaded, the name will be used to create the initials
    name: str | None = None

    # Function called when image failed to load
    on_error: Callable[[str], None] | None = None

    # If true, the Avatar will show a border around it. Best for a group of avatars.
    show_border: bool | None = None

    # The image url of the Avatar.
    src: str | None = None

    # List of sources to use for different screen resolutions
    src_set: str | None = None

    # "2xs" | "xs" | "sm" | "md" | "lg" | "xl" | "2xl" | "full"
    size: str | None = None


class AvatarBadge(ChakraComponent):
    """A wrapper that displays its content on the right corner of the avatar."""

    tag = "AvatarBadge"


class AvatarGroup(ChakraComponent):
    """A wrapper to stack multiple Avatars together."""

    tag = "AvatarGroup"

    # The maximum number of visible avatars
    max_: int | None = None

    # The space between the avatars in the group.
    spacing: int | None = None
