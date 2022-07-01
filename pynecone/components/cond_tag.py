"""Tag to conditionally render components."""

from pynecone import utils
from pynecone.components.tag import Tag


class CondTag(Tag):
    """A conditional tag."""

    # The code to render if the condition is true.
    true_value: str

    # The code to render if the condition is false.
    false_value: str

    def __str__(self) -> str:
        """Render the tag as a React string.

        Returns:
            The React code to render the tag.
        """
        assert self.condition is not None, "The condition must be set."
        return utils.format_conditional(
            condition=self.condition.full_name,
            true_value=self.true_value,
            false_value=self.false_value,
        )
