"""Templates to use in the pynecone compiler."""

import json
from typing import Any, Callable

from pynecone import constants, utils
from pynecone.utils import join

# Template for the Pynecone config file.
PCCONFIG = """# The Pynecone configuration file.

APP_NAME = "{app_name}"
"""

# Javascript formatting.
CONST = "const {name} = {value}".format
PROP = "{object}.{property}".format
IMPORT_LIB = 'import "{lib}"'.format
IMPORT_FIELDS = 'import {default}{others} from "{lib}"'.format


def format_import(lib: str, default: str = "", rest: set[str] | None = None) -> str:
    """Format an import statement.

    Args:
        lib: The library to import from.
        default: The default field to import.
        rest: The set of fields to import from the library.

    Returns:
        The compiled import statement.
    """
    # Handle the case of direct imports with no libraries.
    if lib == "":
        assert default == "", "No default field allowed for empty library."
        assert rest is not None and len(rest) > 0, "No fields to import."
        return join([IMPORT_LIB(lib=lib) for lib in sorted(rest)])

    # Handle importing from a library.
    rest = rest or set()
    if len(default) == 0 and len(rest) == 0:
        # Handle the case of importing a library with no fields.
        return IMPORT_LIB(lib=lib)
    else:
        # Handle importing specific fields from a library.
        others = f'{{{", ".join(sorted(rest))}}}' if len(rest) > 0 else ""
        if len(default) > 0 and len(rest) > 0:
            default += ", "
        return IMPORT_FIELDS(default=default, others=others, lib=lib)


# Code to render a single NextJS component.
COMPONENT = join(
    [
        "{imports}",
        "",
        "{constants}",
        "",
        "export default function Component() {{",
        "",
        "{state}",
        "",
        "{actions}",
        "",
        "{effects}",
        "",
        "return (",
        "{render}",
        ")",
        "}}",
    ]
).format

# React state declarations.
USE_STATE = CONST(
    name="[{state}, {set_state}]", value="useState({initial_state})"
).format


def format_state_setter(state: str) -> str:
    """Format a state setter.

    Args:
        state: The name of the state variable.

    Returns:
        The compiled state setter.
    """
    return f"set{state[0].upper() + state[1:]}"


def format_state(
    state: str,
    initial_state: dict[str, Any] | None = None,
    inherit_state: str | None = None,
) -> str:
    """Format a state declaration.

    Args:
        state: The name of the state variable.
        initial_state: The initial state of the state variable.
        inherit_state: The name of the state variable to inherit from.

    Returns:
        The compiled state declaration.
    """
    initial = json.dumps(initial_state or {})
    if inherit_state is not None:
        initial = f"{{...{inherit_state}, {initial[1:-1]}}}"
    set_state = format_state_setter(state)
    return USE_STATE(state=state, set_state=set_state, initial_state=initial)


# Actions.
ACTION_ENDPOINT = constants.Endpoint.ACTION.name
ACTION_DECLARATIONS = join(
    [
        "const Action = fn => args => setLocalState({{",
        "    ...localState,",
        "    actions: [...localState.actions, {{fn, args}}],",
        "}})",
        "{action_declarations}",
    ]
).format


def format_action_declaration(fn: Callable) -> str:
    """Format an action declaration.

    Args:
        fn: The function to declare.

    Returns:
        The compiled action declaration.
    """
    name = utils.format_action_fn(fn=fn)
    action = utils.to_snake_case(fn.__qualname__)
    return f"const {name} = Action('{action}')"


# Effects.
USE_EFFECT = join(
    [
        "useEffect(async () => {",
        "   if (!localState.processing && localState.actions.length > 0) {",
        "       const action = localState.actions.pop()",
        "       if (window) {",
        "           if (!window.sessionStorage.getItem('token')) {",
        "               window.sessionStorage.setItem('token', crypto.randomUUID())",
        "           }",
        "           action.token = window.sessionStorage.getItem('token')",
        "       }",
        "       setLocalState({...localState, processing: true})",
        f"       const result = await axios.post({ACTION_ENDPOINT}, action)",
        "       setState(result.data)",
        "       setLocalState({",
        "           ...result.data,",
        "           actions: localState.actions,",
        "           processing: false",
        "       })",
        "   }",
        '   if (state.page != "" && state.page != router.pathname) {',
        "       router.push(state.page)",
        "   }",
        "})",
    ]
)

# Routing
ROUTER = "const router = useRouter()"
