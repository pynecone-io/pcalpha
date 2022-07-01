"""Keyboard shortcut components."""

from pynecone.components.chakra import ChakraComponent


class Kbd(ChakraComponent):
    """The keyboard key component exists to show which key or combination of keys performs a given action. The action itself should be further explained in accompanying content. It renders a <kbd> element."""

    tag = "Kbd"
