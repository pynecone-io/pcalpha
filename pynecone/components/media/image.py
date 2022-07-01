"""An image component."""
from __future__ import annotations

from typing import Callable

from pynecone.components.chakra import ChakraComponent
from pynecone.components.tag import Tag


class Image(ChakraComponent):
    """The Image component is used to display images. Image composes Box so you can use all the style props and add responsive styles as well."""

    tag = "Image"

    # How to align the image within its bounds. It maps to css `object-position` property.
    align: str | None = None

    # The key used to set the crossOrigin on the HTMLImageElement into which the image will be loaded. This tells the browser to request cross-origin access when trying to download the image data.
    cross_origin: str | None = None

    # Fallback element to show if image is loading or image fails.
    fallback: Tag | None = None

    # Fallback image src to show if image is loading or image fails. Note 🚨: We recommend you use a local image
    fallback_src: str | None = None

    # How the image to fit within its bounds. It maps to css `object-fit` property.
    fit: str | None = None

    # The native HTML height attribute to the passed to the img
    html_height: str | None = None

    # The native HTML width attribute to the passed to the img
    html_width: str | None = None

    # If true, opt out of the fallbackSrc logic and use as img
    ignore_fallback: bool | None = None

    # "eager" | "lazy"
    loading: str | None = None

    # A callback for when there was an error loading the image src
    on_error: Callable[[str], None] | None = None

    # A callback for when the image src has been loaded
    on_load: Callable[[], None] | None = None

    # The image src attribute
    src: str | None = None

    # The image srcset attribute
    src_set: str | None = None

    @classmethod
    def create(cls, src: str, **attrs) -> Image:
        """Create an image component.

        Args:
            src: The image source.
            **attrs: The attributes to pass to the component.

        Returns:
            The image component.
        """
        return Image(src=src, **attrs)
