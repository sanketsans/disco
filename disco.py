import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from spotify_cred import CLIENT_ID, SECRET_KEY

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                           client_secret=SECRET_KEY))

results = sp.search(q=' great spirit armin', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
    