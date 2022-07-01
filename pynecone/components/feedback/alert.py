"""Alert components."""

from pynecone.components.chakra import ChakraComponent
from pynecone.components.text_display import TextDisplay
from pynecone.components.component import Example


class Alert(ChakraComponent):
    """Container to stack elements with spacing."""

    tag = "Alert"

    # The status of the alert ("success" | "info" | "warning" | "error")
    status: str | None = None

    # "subtle" | "left-accent" | "top-accent" | "solid"
    variant: str | None = None

    _examples = [
        Example(
            description="Different status examples.",
            code="""
pc.vstack(
    pc.alert(
        pc.alert_icon(),
        pc.alert_title("Error Pynecone version is out of date."),
        status = 'error'
    ),
    pc.alert(
        pc.alert_icon(),
        pc.alert_title("Warning Pynecone version is out of date."),
        status = 'warning'
    ),
    pc.alert(
        pc.alert_icon(),
        pc.alert_title("Pynecone version is up to date."),
        status = 'success'
    ),
    pc.alert(
        pc.alert_icon(),
        pc.alert_title("Pynecone version is 1.0.0."),
        status = 'info'
    ),
    width = '100%'
)
""",
        ),
        Example(
            description="Different variant examples.",
            code="""
pc.vstack(
    pc.alert(
        pc.alert_icon(),
        pc.alert_title("Pynecone version is up to date."),
        status = 'success',
        variant= 'subtle'
    ),
    pc.alert(
        pc.alert_icon(),
        pc.alert_title("Pynecone version is up to date."),
        status = 'success',
        variant = 'solid'

    ),
    pc.alert(
        pc.alert_icon(),
        pc.alert_title("Pynecone version is up to date."),
        status = 'success',
        variant = 'top-accent'
    ),
    width = '100%'
)
""",
        ),
    ]


class AlertIcon(ChakraComponent):
    """AlertIcon composes Icon and changes the icon based on the status prop."""

    tag = "AlertIcon"


class AlertTitle(ChakraComponent):
    """AlertTitle composes the Box component."""

    tag = "AlertTitle"


class AlertDescription(ChakraComponent):
    """AlertDescription composes the Box component."""

    tag = "AlertDescription"

    _examples = [
        Example(
            description="Different status examples.",
            code="""
pc.vstack(
    pc.alert(
        pc.alert_icon(),
        pc.alert_title("Pynecone version is up to date."),
        pc.alert_description("No need to update."),
        status = 'success'
    ),
    width = '100%'
)
""",
        )
    ]
