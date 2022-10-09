import spotipy
from spotipy import oauth2
from bottle import route, run, request

SCOPE = "user-read-currently-playing"

sp_auth = oath2.SpotifyOAuth(scope=SCOPE)

@route('/login')
def login():
    access_token = __auth_guard()
    if access_token:
        return "ok"
    else:
        return __login_form()

@route('current_playing')
def current_playing()
    access_token = __auth_guard()
    if access_token:
       sp = spotipy.Spotify(access_token)
       return sp.current_playback()
    else:
        return __login_form()


def __auth_guard():
    access_token = ""
    token_info = sp_auth.get_cached_token()
    if token_info:
        access_token = token_info['access_token']
    else:
        url = request.url
        code = sp_auth.get_access_token(url)
        if code != url:
            token_info = sp_auth.get_access_token()
            access_token = token_info['access_token']
    return access_token


def __login_form():
    auth_url = sp_auth.get_authorize_url()
    return "<a href='"+auth_url+"'>Login</a>"


run(host='')
