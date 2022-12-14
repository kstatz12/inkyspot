#!/usr/bin/env python3
from inky.auto import auto
from PIL import Image
import requests
from io import BytesIO
import time
import json
import sys

currentImageUrl = ""
currentImage = None
baseUrl = "http://localhost:8080"


def __get_image():
    global currentImageUrl
    global currentImage

    r = requests.get(baseUrl + "/current_playing")

    if r.text is None:
        return currentImageUrl, currentImage

    data = json.loads(r.text)
    url = data['item']['album']['images'][0]['url']
    if url != currentImageUrl:
        res = requests.get(url)
        return url, Image.open(BytesIO(res.content))
    else:
        return currentImageUrl, currentImage


def __process_image(img):
    return img.resize((600, 448))


def __set_image(image):
    global currentImageUrl
    global currentImage
    url, image = __get_image()
    if currentImageUrl != url:
        currentImageUrl = url
        currentImage = image
        display.set_image(__process_image(image))
        display.show()


if sys.argv[1] is not None:
    baseUrl = sys.argv[1]

display = auto(ask_user=True, verbose=True)
while True:
    image = __get_image()
    __set_image(image)
    time.sleep(30)
