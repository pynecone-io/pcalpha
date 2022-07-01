"""Menu components."""
from typing import Callable

from pynecone.components.chakra import ChakraComponent
from pynecone.components.typography.text import Text


class Menu(ChakraComponent):
    """The wrapper component provides context, state, and focus management."""

    tag = "Menu"

    # The padding required to prevent the arrow from reaching the very edge of the popper.
    arrow_padding: int | None = None

    # If true, the first enabled menu item will receive focus and be selected when the menu opens.
    auto_select: bool | None = None

    # The boundary area for the popper. Used within the preventOverflow modifier
    boundary: str | None = None

    # If true, the menu will close when you click outside the menu list
    close_on_blur: bool | None = None

    # If true, the menu will close when a menu item is clicked
    close_on_select: bool | None = None

    # If by default the menu is open.
    default_is_open: bool | None = None

    # If rtl, poper placement positions will be flipped i.e. 'top-right' will become 'top-left' and vice-verse ("ltr" | "rtl")
    direction: str | None = None

    # If true, the popper will change its placement and flip when it's about to overflow its boundary area.
    flip: bool | None = None

    # The distance or margin between the reference and popper. It is used internally to create an offset modifier. NB: If you define offset prop, it'll override the gutter.
    gutter: int | None = None

    # Performance 🚀: If true, the MenuItem rendering will be deferred until the menu is open.
    is_lazy: bool | None = None

    # Performance 🚀: The lazy behavior of menu's content when not visible. Only works when `isLazy={true}` - "unmount": The menu's content is always unmounted when not open. - "keepMounted": The menu's content initially unmounted, but stays mounted when menu is open.
    lazy_behavior: str | None = None

    # Determines if the menu is open or not.
    is_open: bool | None = None

    # If true, the popper will match the width of the reference at all times. It's useful for autocomplete, `date-picker` and select patterns.
    match_width: bool | None = None

    # Action when the menu is closed.
    on_close: Callable[[str], None] | None = None

    # Action when the menu is opened.
    on_open: Callable[[str], None] | None = None

    # The placement of the popper relative to its reference.
    placement: str | None = None

    # If true, will prevent the popper from being cut off and ensure it's visible within the boundary area.
    prevent_overflow: bool | None = None

    # The CSS positioning strategy to use. ("fixed" | "absolute")
    strategy: str | None = None


class MenuButton(ChakraComponent):
    """The trigger for the menu list. Must be a direct child of Menu."""

    tag = "MenuButton"

    variant: str | None = None

    as_: str = """{Button}"""


class MenuList(ChakraComponent):
    """The wrapper for the menu items. Must be a direct child of Menu."""

    tag = "MenuList"


class MenuItem(Menu):
    """The trigger that handles menu selection. Must be a direct child of a MenuList."""

    tag = "MenuItem"

    # Overrides the parent menu's closeOnSelect prop.
    close_on_select: bool | None = None

    # Right-aligned label text content, useful for displaying hotkeys.
    command: str | None = None

    # The spacing between the command and menu item's label.
    command_spacing: int | None = None

    # If true, the menuitem will be disabled.
    is_disabled: bool | None = None

    # If true and the menuitem is disabled, it'll remain keyboard-focusable
    is_focusable: bool | None = None


class MenuItemOption(Menu):
    """The checkable menu item, to be used with MenuOptionGroup."""

    tag = "MenuItemOption"

    # Overrides the parent menu's closeOnSelect prop.
    close_on_select: bool | None = None

    # Right-aligned label text content, useful for displaying hotkeys.
    command: str | None = None

    # The spacing between the command and menu item's label.
    command_spacing: int | None = None

    # Determines if menu item is checked.
    is_checked: bool | None = None

    # If true, the menuitem will be disabled.
    is_disabled: bool | None = None

    # If true and the menuitem is disabled, it'll remain keyboard-focusable
    is_focusable: bool | None = None

    # "checkbox" | "radio"
    type_: str | None = None

    # Value of the menu item.
    value: str | None = None


class MenuGroup(Menu):
    """A wrapper to group related menu items."""

    tag = "MenuGroup"


class MenuOptionGroup(Menu):
    """A wrapper for checkable menu items (radio and checkbox)."""

    tag = "MenuOptionGroup"

    # Action to handle on change.
    on_change: Callable[[str], None] | None = None

    # "checkbox" | "radio"
    type_: str | None = None

    # Value of the option group.
    value: str | None = None


class MenuDivider(Menu):
    """A visual separator for menu items and groups."""

    tag = "MenuDivider"
