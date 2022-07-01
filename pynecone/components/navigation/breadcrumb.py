"""Breadcrumb components."""

from pynecone.components.chakra import ChakraComponent
from pynecone.components.text_display import TextDisplay


class Breadcrumb(ChakraComponent):
    """The parent container for breadcrumbs."""

    tag = "Breadcrumb"

    # The visual separator between each breadcrumb item
    separator: str | None = None

    # The left and right margin applied to the separator
    separator_margin: str | None = None


class BreadcrumbItem(ChakraComponent):
    """Individual breadcrumb element containing a link and a divider."""

    tag = "BreadcrumbItem"

    # Is the current page of the breadcrumb.
    is_current_page: bool | None = None

    # Is the last child of the breadcrumb.
    is_last_child: bool | None = None

    # The visual separator between each breadcrumb item
    separator: str | None = None

    # The left and right margin applied to the separator
    spacing: str | None = None

    # The href of the item.
    href: str | None = None


class BreadcrumbSeparator(ChakraComponent):
    """The visual separator between each breadcrumb."""

    tag = "BreadcrumbSeparator"


class BreadcrumbLink(ChakraComponent):
    """The breadcrumb link."""

    tag = "BreadcrumbLink"

    # Is the current page of the breadcrumb.
    is_current_page: bool | None = None
