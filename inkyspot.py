from inky import Inky7Colour as Inky
from PIL import Image
import requests
from io import BytesIO
import time


def __get_image():
    r = requests.get("localhost:8080/current_playing")
    url = r['item']['album']['images'][0]['url']
    print(url)
    res = requests.get(url)
    return Image.open(BytesIO(res.content))


def __set_image(image):
    image = __get_image()
    display.set_image(image)
    display.show()


display = Inky()
while True:
    image = __get_image()
    __set_image(image)
    time.sleep(30000)
