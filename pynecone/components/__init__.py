"""Import all the components."""

from pynecone import utils
from pynecone.components.tag import Attr
from pynecone.property import Property

from .component import Component
from .datadisplay import *
from .disclosure import *
from .feedback import *
from .forms import *
from .graphing import *
from .layout import *
from .media import *
from .navigation import *
from .overlay import *
from .typography import *

# Add the convenience methods for all the components.
locals().update(
    {
        utils.to_snake_case(name): value.create
        for name, value in locals().items()
        if isinstance(value, type) and issubclass(value, Component)
    }
)
