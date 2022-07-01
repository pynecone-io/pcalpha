"""Let's make our first pynecone app!

This file shows the steps to create a basic static application.
"""

# Import pynecone.
import pynecone as pc

# Create an app.
app = pc.App()

# Define a view.
def hello():
    return pc.text("Hello world test!")


# Add the view to the app.
app.add_view("/", hello)
