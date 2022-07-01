"""Common utility functions used in the compiler."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Type

from pynecone import constants
from pynecone.action import ActionSpec
from pynecone.compiler import templates
from pynecone.components.component import ImportDict
from pynecone.components.tag import Attr
from pynecone.state import State

if TYPE_CHECKING:
    from pynecone.components.component import Component


def compile_import_statement(lib: str, fields: set[str]) -> str:
    """Compile an import statement.

    Args:
        lib: The library to import from.
        fields: The set of fields to import from the library.

    Returns:
        The compiled import statement.
    """
    # Check for default imports.
    defaults = {
        field
        for field in fields
        if field.lower() == lib.lower().replace("-", "").replace("/", "")
    }
    assert len(defaults) < 2

    # Get the default import, and the specific imports.
    default = next(iter(defaults), "")
    rest = fields - defaults
    return templates.format_import(lib=lib, default=default, rest=rest)


def compile_imports(imports: ImportDict) -> str:
    """Compile an import dict.

    Args:
        imports: The import dict to compile.

    Returns:
        The compiled import dict.
    """
    return templates.join(
        [compile_import_statement(lib, fields) for lib, fields in imports.items()]
    )


def compile_constant_declaration(name: str, value: Attr) -> str:
    """Compile a constant declaration.

    Args:
        name: The name of the constant.
        value: The value of the constant.

    Returns:
        The compiled constant declaration.
    """
    return templates.CONST(name=name, value=json.dumps(value))


def compile_constants() -> str:
    """Compile all the necessary constants.

    Returns:
        A string of all the compiled constants.
    """
    endpoints = {endpoint.name: endpoint.get_url() for endpoint in constants.Endpoint}
    return templates.join(
        [
            compile_constant_declaration(name=name, value=value)
            for name, value in sorted(endpoints.items())
        ]
    )


def compile_state(state: Type[State]) -> str:
    """Compile the state of the app.

    Args:
        state: The app state object.

    Returns:
        A string of the compiled state.
    """
    state_name = state.__name__.lower()
    synced_state = templates.format_state(
        state=state_name, initial_state=state().dict()
    )
    local_state = templates.format_state(
        state="localState",
        initial_state={
            "processing": False,
            "actions": [{"fn": f"{state_name}.hydrate"}],
        },
        inherit_state=state_name,
    )
    router = templates.ROUTER
    return templates.join([synced_state, local_state, router])


def compile_action_declaration(action: ActionSpec) -> str:
    """Compile the action declaration.

    Args:
        action: The action to compile.

    Returns:
        A string of the compiled action declaration.
    """
    return templates.format_action_declaration(fn=action.fn)


def compile_actions(component: Component) -> str:
    """Compile all the actions for a given component.

    Args:
        component: The component to compile the actions for.

    Returns:
        A string of the compiled actions for the component.
    """
    action_declarations = templates.join(
        compile_action_declaration(action) for action in sorted(component.get_actions())
    )
    return templates.ACTION_DECLARATIONS(
        action_declarations=action_declarations,
    )


def compile_effects() -> str:
    """Compile all the effects for a given component.

    Returns:
        A string of the compiled effects for the component.
    """
    return templates.USE_EFFECT


def compile_render(component: Component) -> str:
    """Compile the component's render method.

    Args:
        component: The component to compile the render method for.

    Returns:
        A string of the compiled render method.
    """
    return component.render()
