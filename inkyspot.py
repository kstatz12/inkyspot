#!/usr/bin/env python3
from inky.auto import auto
from PIL import Image
import requests
from io import BytesIO
import time
import json
import sys

currentImageUrl = ""
baseUrl = "http://localhost:8080"


def __get_image():
    r = requests.get(baseUrl + "/current_playing")
    data = json.loads(r.text)

    if data is None:
        return None, None

    url = data['item']['album']['images'][0]['url']
    res = requests.get(url)
    return url, Image.open(BytesIO(res.content))


def __process_image(img):
    return img.resize((600, 448))


def __set_image(image):
    global currentImageUrl
    url, image = __get_image()
    if currentImageUrl != url:
        currentImageUrl = url
        display.set_image(__process_image(image))
        display.show()


if sys.argv[1] is not None:
    baseUrl = sys.argv[1]

display = auto(ask_user=True, verbose=True)
while True:
    image = __get_image()
    __set_image(image)
    time.sleep(30)
