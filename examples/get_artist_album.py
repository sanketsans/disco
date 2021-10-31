import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

from spotify_cred import CLIENT_ID, SECRET_KEY

## Get all albums from artist 
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                           client_secret=SECRET_KEY))

results = sp.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print((album['name']))
    