import os
from dotenv import load_dotenv
import supervisely as sly

from supervisely.app.widgets import Button, Text, Container

load_dotenv(os.path.expanduser("~/supervisely.env"))

button = Button("random text")
text = Text("press the button to get random text")

layout = Container([button, text])

app = sly.Application(layout)

print("hello")
