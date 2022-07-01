"""Typography components."""

from .heading import Heading
from .text import Text

__all__ = [f for f in dir() if f[0].isupper()]  # type: ignore
