from fastapi import FastAPI
import logging
import threading
from pydantic import BaseModel

from .streamdeck._funcs import update_button

logging.getLogger().setLevel(logging.DEBUG)

app = FastAPI()


class ButtonDown(BaseModel):
    page: int
    button: int


@app.post("/button_down")
def on_button_down(data: ButtonDown):
    t = threading.Thread(target=update_button, args=(data.page, data.button))
    t.start()
    # button_down(page=data.page, button=data.button)
