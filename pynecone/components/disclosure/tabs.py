"""Tab components."""

from typing import Callable

from pynecone.components.chakra import ChakraComponent


class Tabs(ChakraComponent):
    """An accessible tabs component that provides keyboard interactions and ARIA attributes described in the WAI-ARIA Tabs Design Pattern. Tabs, provides context and state for all components."""

    tag = "Tabs"

    # The alignment of the tabs ("center" | "end" | "start")
    align: str | None = None

    # The initial index of the selected tab (in uncontrolled mode)
    default_index: int | None = None

    # The id of the tab
    id_: str | None = None

    # If true, tabs will stretch to width of the tablist.
    is_fitted: bool | None = None

    # Performance booster: If true, rendering of the tab panel's will be deferred until it is selected.
    is_lazy: bool | None = None

    # If true, the tabs will be manually activated and display its panel by pressing Space or Enter. If false, the tabs will be automatically activated and their panel is displayed when they receive focus.
    is_manual: bool | None = None

    # The orientation of the tab list.
    orientation: str | None = None

    # Callback when the index (controlled or un-controlled) changes.
    on_change: Callable[[int], None] | None = None

    # "line" | "enclosed" | "enclosed-colored" | "soft-rounded" | "solid-rounded" | "unstyled"
    variant: str | None = None


class Tab(ChakraComponent):
    """An element that serves as a label for one of the tab panels and can be activated to display that panel.."""

    tag = "Tab"

    # If true, the Tab won't be toggleable
    is_disabled: bool | None = None

    # If true, the Tab will be selected
    is_selected: bool | None = None

    # The id of the tab
    id_: str | None = None

    # The id of the panel.
    panel_id: str | None = None


class TabList(ChakraComponent):
    """Wrapper for the Tab components."""

    tag = "TabList"


class TabPanels(ChakraComponent):
    """Wrapper for the Tab components."""

    tag = "TabPanels"


class TabPanel(ChakraComponent):
    """An element that contains the content associated with a tab."""

    tag = "TabPanel"
