"""Constants used throughout the package."""

import os
from enum import Enum

# App initialization config.

# The name of the library.
LIBRARY_NAME = "pynecone"

# The root directory of the pynecone library.
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The template files for pc init.
TEMPLATE_DIR = os.path.join(ROOT_DIR, LIBRARY_NAME, ".templates")
WEB_TEMPLATE_DIR = os.path.join(TEMPLATE_DIR, "web")
APP_TEMPLATE_DIR = os.path.join(TEMPLATE_DIR, "app")
APP_TEMPLATE_FILE = "hello.py"
APP_ASSETS_DIR = "assets"

# The frontend directory in the user's project.
WEB_DIR = ".web"
WEB_PAGES_DIR = os.path.join(WEB_DIR, "pages")
WEB_ASSETS_DIR = os.path.join(WEB_DIR, "public")
NODE_MODULES = "node_modules"
PACKAGE_LOCK = "package-lock.json"

# Frontend commands.
NODE_INSTALL = ["npm", "install"]
BUILD_FRONTEND = ["npm", "run", "build"]
RUN_FRONTEND = ["npm", "run", "dev"]

# Backend commands.
RUN_BACKEND = ["poetry", "run", "uvicorn", "--reload", "--host", "0.0.0.0"]

# The expected variable name where the pc.App is stored.
APP_VAR = "app"

# The api variable.
API_VAR = ".".join([APP_VAR, "api"])

# The name of the pynecone config module.
CONFIG_MODULE = "pcconfig"
CONFIG_FILE = f"{CONFIG_MODULE}.py"

# The attribute values that store text content.
TEXT_ATTRS = {"text"}


# Server config.

# The url to run the backend server on.
API_HOST = "http://0.0.0.0:8000"


class Endpoint(Enum):
    """Endpoints for the pynecone backend API."""

    PING = "ping"
    ACTION = "action"

    def __str__(self) -> str:
        """Get the string representation of the endpoint.

        Returns:
            The path for the endpoint.
        """
        return f"/{self.value}"

    def get_url(self) -> str:
        """Get the URL for the endpoint.

        Returns:
            The full URL for the endpoint.
        """
        return "".join([API_HOST, str(self)])


# Compiler constants.
INDEX = "index"
JS_EXT = ".js"
PY_EXT = ".py"
SETTER_PREFIX = "set_"

# Database constants.
DB_NAME = "pynecone.db"
