import spotipy
from inky.auto import auto
from spotipy.oauth2 import SpotifyOAuth
from PIL import Image
import requests
from io import BytesIO


def __get_image(sp):
    r = sp.currently_playing()
    url = r['item']['album']['images'][0]['url']
    print(url)
    res = requests.get(url)
    return Image.open(BytesIO(res.content))


display = auto()
scope = "user-read-currently-playing"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

image = __get_image(sp)
display.set_image(image)
display.show()
