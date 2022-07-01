"""Components that are based on Victory."""

from pynecone.components.library_component import LibraryComponent


class NivoComponent(LibraryComponent):
    """A component that wraps a Rebass component."""

    library = "victory"
