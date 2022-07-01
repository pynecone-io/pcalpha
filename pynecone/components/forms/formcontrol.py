"""Form components."""

from pynecone.components.chakra import ChakraComponent
from pynecone.components.component import Example


class FormControl(ChakraComponent):
    """FormControl provides context such as isInvalid, isDisabled, and isRequired to form elements."""

    tag = "FormControl"

    # If true, the form control will be disabled.
    is_disabled: bool | None = None

    # If true, the form control will be invalid.
    is_invalid: bool | None = None

    # If true, the form control will be readonly
    is_read_only: bool | None = None

    # If true, the form control will be required.
    is_required: bool | None = None

    # The label text used to inform users as to what information is requested for a text field.
    label: str | None = None

    # Usage examples
    _examples = [
        Example(
            description="A basic button.",
            code="""
pc.form_control(
    pc.form_label("First Name", html_for = 'email'),
    pc.form_helper_text("This is a help text"),
    is_required=True
)
""",
        )
    ]


class FormHelperText(ChakraComponent):
    """A form helper text component."""

    tag = "FormHelperText"


class FormLabel(ChakraComponent):
    """A form label component."""

    tag = "FormLabel"

    # Link
    html_for: str | None = None


class FormErrorMessage(ChakraComponent):
    """A form error message component."""

    tag = "FormErrorMessage"
