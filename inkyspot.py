from inky import Inky7Colour as Inky
from PIL import Image
import requests
from io import BytesIO
import time
import json


def __get_image():
    r = requests.get("http://localhost:8080/current_playing")
    data = json.loads(r.text)
    url = data['item']['album']['images'][0]['url']
    res = requests.get(url)
    return Image.open(BytesIO(res.content))


def __process_image(img):
    img.resize((600, 448))
    return img


def __set_image(image):
    image = __get_image()
    display.set_image(__process_image(image))
    display.show()


display = Inky()
while True:
    image = __get_image()
    __set_image(image)
    time.sleep(30000)
