#!/usr/bin/env python3
from inky.auto import auto
from PIL import Image
import requests
from io import BytesIO
import time
import json

currentImageUrl = ""

def __get_image():
    r = requests.get("http://localhost:8080/current_playing")
    data = json.loads(r.text)

    if data is None:
        return None, None

    url = data['item']['album']['images'][0]['url']
    res = requests.get(url)
    return url, Image.open(BytesIO(res.content))


def __process_image(img):
    return img.resize((600, 448))


def __set_image(image):
    url, image = __get_image()
    if currentImageUrl != url:
        let currentImageUrl = url
        display.set_image(__process_image(image))
        display.show()


display = auto(ask_user=True, verbose=True)
while True:
    image = __get_image()
    __set_image(image)
    time.sleep(30)
