import sys
import requests
import json
from io import BytesIO
from PIL import Image

def __get_image():
    r = requests.get("http://localhost:8080/current_playing")
    data = json.loads(r.text)
    url = data['item']['album']['images'][0]['url']
    res = requests.get(url)
    return Image.open(BytesIO(res.content))


def __process_image(image):
    width, height = image.size

    aspect_ratio = height/width

    new_width = 120
    new_height = aspect_ratio * new_width * 0.55

    image = image.resize((new_width, int(new_height)))

    image = image.convert('L')

    pixels = image.getdata()


    chars = ["B","S","#","&","@","$","%","*","!",":","."]
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    new_pixels_count = len(new_pixels)

    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    print(ascii_image)


img = __get_image()

__process_image(img)
