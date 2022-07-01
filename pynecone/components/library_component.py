"""Base class for components based on a library."""

from pynecone import constants
from pynecone.components.component import Component, ImportDict
from pynecone.components.tag import Tag


class LibraryComponent(Component):
    """A component that is based on a library."""

    # The library that the component is based on.
    library: str = ""

    # The tag from the library.
    tag: str = ""

    def _render(self) -> Tag:
        return Tag(name=self.tag).add_attrs(
            **{
                attr: getattr(self, attr)
                for attr in set(self.get_fields()) - set(LibraryComponent.get_fields())
                if attr not in constants.TEXT_ATTRS
            }
        )

    def _get_imports(self) -> ImportDict:
        return {self.library: {self.tag}}
