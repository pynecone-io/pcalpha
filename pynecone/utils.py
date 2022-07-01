"""General utility functions."""

import os
import re
from typing import Callable

join = os.linesep.join


def to_snake_case(text: str) -> str:
    """Convert a string to snake case.

    The words in the text are converted to lowercase and
    separated by underscores.

    Args:
        text: The string to convert.

    Returns:
        The snake case string.
    """
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", text)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def to_camel_case(text: str) -> str:
    """Convert a string to camel case.

    The first word in the text is converted to lowercase and
    the rest of the words are converted to title case, removing underscores.

    Args:
        text: The string to convert.

    Returns:
        The camel case string.
    """
    return "".join(
        word.capitalize() if i > 0 else word.lower()
        for i, word in enumerate(text.split("_"))
    )


def to_title(text: str) -> str:
    """Convert a string from snake case to a title.

    Each word is converted to title case and separated by a space.

    Args:
        text: The string to convert.

    Returns:
        The title case string.
    """
    return " ".join(word.capitalize() for word in text.split("_"))


WRAP_MAP = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">",
    '"': '"',
    "'": "'",
}


def get_close_char(open: str, close: str | None = None) -> str:
    """Check if the given character is a valid brace.

    Args:
        open: The open character.
        close: The close character if provided.

    Returns:
        The close character.
    """
    if close is not None:
        return close
    if open not in WRAP_MAP:
        raise ValueError(f"Invalid wrap open: {open}, must be one of {WRAP_MAP.keys()}")
    return WRAP_MAP[open]


def is_wrapped(text: str, open: str, close: str | None = None) -> bool:
    """Check if the given text is wrapped in the given open and close characters.

    Args:
        text: The text to check.
        open: The open character.
        close: The close character.

    Returns:
        Whether the text is wrapped.
    """
    close = get_close_char(open, close)
    return text.startswith(open) and text.endswith(close)


def wrap(
    text: str,
    open: str,
    close: str | None = None,
    check_first: bool = True,
    num: int = 1,
) -> str:
    """Wrap the given text in the given open and close characters.

    Args:
        text: The text to wrap.
        open: The open character.
        close: The close character.
        check_first: Whether to check if the text is already wrapped.
        num: The number of times to wrap the text.

    Returns:
        The wrapped text.
    """
    close = get_close_char(open, close)

    # If desired, check if the text is already wrapped in braces.
    if check_first and is_wrapped(text=text, open=open, close=close):
        return text

    # Wrap the text in braces.
    return f"{open * num}{text}{close * num}"


def indent(text: str, indent_level: int = 2) -> str:
    """Indent the given text by the given indent level.

    Args:
        text: The text to indent.
        indent_level: The indent level.

    Returns:
        The indented text.
    """
    lines = text.splitlines()
    if len(lines) < 2:
        return text
    return os.linesep.join(f"{' ' * indent_level}{line}" for line in lines) + os.linesep


def format_conditional(condition: str, true_value: str, false_value: str = '""') -> str:
    """Format a conditional expression.

    Args:
        condition: The condition.
        true_value: The value to return if the condition is true.
        false_value: The value to return if the condition is false.

    Returns:
        The formatted conditional expression.
    """
    return f"{{{condition} ? {true_value} : {false_value}}}"


def format_action_fn(fn: Callable) -> str:
    """Format a function as an action.

    Args:
        fn: The function to format.

    Returns:
        The formatted function.
    """
    return fn.__qualname__.replace(".", "_")
