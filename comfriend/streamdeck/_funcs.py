import logging
import requests
import time

_STREAM_DECK_URL = "http://localhost:8888/"
logger = logging.getLogger(__name__)


def update_button(page: int, button: int):
    time.sleep(1)
    logger.debug(f"button_down({page}, {button}")
    # f"style/bank/{page}/{button}/?text=Happy&bgcolor=#ffffff&color#000000&size=28px"
    url = f"http://localhost:8888/style/bank/{page}/{button}/"
    response = requests.get(url, params=dict(text="Happy", bgcolor="#123456"))
    response.raise_for_status()
    print("INPUT:", page, button, url)
    print(response)
