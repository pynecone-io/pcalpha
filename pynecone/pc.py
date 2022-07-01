"""Pynecone CLI to create, run, and deploy apps."""

import os
import shutil
import signal
import subprocess
import sys
import types
from distutils import dir_util

import typer

from pynecone import constants
from pynecone.compiler import templates

# Create the app.
app = typer.Typer()


@app.command()
def init():
    """Initialize a new Pynecone app."""
    # The app name is the same as the name of the current directory.
    app_name = os.getcwd().split(os.path.sep)[-1]
    typer.echo(f"Initializing {app_name}")

    # Create a configureation file.
    with open(constants.CONFIG_FILE, "w") as f:
        f.write(templates.PCCONFIG.format(app_name=app_name))

    # Initialize the app directory.
    cp(constants.APP_TEMPLATE_DIR, app_name)
    mv(
        os.path.join(app_name, constants.APP_TEMPLATE_FILE),
        os.path.join(app_name, app_name + constants.PY_EXT),
    )
    mkdir(constants.APP_ASSETS_DIR)

    # Initialize the web directory.
    rm(os.path.join(constants.WEB_TEMPLATE_DIR, constants.NODE_MODULES))
    rm(os.path.join(constants.WEB_TEMPLATE_DIR, constants.PACKAGE_LOCK))
    cp(constants.WEB_TEMPLATE_DIR, constants.WEB_DIR)


@app.command()
def run():
    """Run the app."""
    # Get the app config.
    sys.path.append(os.getcwd())
    pcconfig = __import__(constants.CONFIG_MODULE)
    module = ".".join([pcconfig.APP_NAME, pcconfig.APP_NAME])

    # Get the app.
    app = __import__(module, fromlist=(constants.APP_VAR,))

    # Launch the app.
    run_frontend(app)
    run_backend(app)


def run_frontend(app: types.ModuleType):
    """Run the frontend for the Pynecone app.

    Args:
        app: The user's app module.
    """
    # Initialize the web directory if it doesn't exist.
    cp(constants.WEB_TEMPLATE_DIR, constants.WEB_DIR, overwrite=False)

    # Install the frontend dependencies.
    subprocess.call(constants.NODE_INSTALL, cwd=constants.WEB_DIR)

    # Link the assets folder.
    ln(src=f"../{constants.APP_ASSETS_DIR}", dest=constants.WEB_ASSETS_DIR)

    # Compile the frontend.
    app.app.compile()

    # Run the development server in the background.
    frontend_process = subprocess.Popen(constants.RUN_FRONTEND, cwd=constants.WEB_DIR)

    def stop_frontend(*_):
        """Stop the frontend.

        Args:
            _: Ignored arguments passed to the signal handler.
        """
        kill(frontend_process.pid)

    # Add signal handlers to stop the frontend.
    signal.signal(signal.SIGINT, stop_frontend)
    signal.signal(signal.SIGTERM, stop_frontend)


def run_backend(app: types.ModuleType):
    """Run the backend for the Pynecone app.

    Args:
        app: The user's app module.
    """
    subprocess.call(constants.RUN_BACKEND + [f"{app.__name__}:{constants.API_VAR}"])


def rm(path: str):
    """Remove a file or directory.

    Args:
        path: The path to the file or directory.
    """
    if os.path.isdir(path):
        dir_util.remove_tree(path)
    elif os.path.isfile(path):
        os.remove(path)


def cp(src: str, dest: str, overwrite: bool = True) -> bool:
    """Copy a file or directory.

    Args:
        src: The path to the file or directory.
        dest: The path to the destination.
        overwrite: Whether to overwrite the destination.

    Returns:
        Whether the copy was successful.
    """
    if src == dest:
        return False
    if not overwrite and os.path.exists(dest):
        return False
    if os.path.isdir(src):
        rm(dest)
        dir_util.copy_tree(src, dest)
    else:
        shutil.copyfile(src, dest)
    return True


def mv(src: str, dest: str, overwrite: bool = True) -> bool:
    """Move a file or directory.

    Args:
        src: The path to the file or directory.
        dest: The path to the destination.
        overwrite: Whether to overwrite the destination.

    Returns:
        Whether the move was successful.
    """
    if src == dest:
        return False
    if not overwrite and os.path.exists(dest):
        return False
    rm(dest)
    shutil.move(src, dest)
    return True


def mkdir(path: str):
    """Create a directory.

    Args:
        path: The path to the directory.
    """
    if not os.path.exists(path):
        os.makedirs(path)


def ln(src: str, dest: str, overwrite: bool = False) -> bool:
    """Create a symbolic link.

    Args:
        src: The path to the file or directory.
        dest: The path to the destination.
        overwrite: Whether to overwrite the destination.

    Returns:
        Whether the link was successful.
    """
    if src == dest:
        return False
    if not overwrite and (os.path.exists(dest) or os.path.islink(dest)):
        return False
    if os.path.isdir(src):
        rm(dest)
        os.symlink(src, dest, target_is_directory=True)
    else:
        os.symlink(src, dest)
    return True


def kill(pid):
    """Kill a process.

    Args:
        pid: The process ID.
    """
    os.kill(pid, signal.SIGTERM)


def main():
    """Run the CLI app."""
    app()


if __name__ == "__main__":
    main()
