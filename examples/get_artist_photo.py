import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import sys
from spotify_cred import CLIENT_ID, SECRET_KEY

## Get all albums from artist 
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                           client_secret=SECRET_KEY))
## enter artist name as args
if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Radiohead'

results = sp.search(q='artist:' + name, type='artist')
items = results['artists']['items']
print(items[0])
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])


## get album info 

# from spotipy.oauth2 import SpotifyClientCredentials
# import spotipy
# import sys
# from pprint import pprint

# if len(sys.argv) > 1:
#     urn = sys.argv[1]
# else:
#     urn = 'spotify:album:5yTx83u3qerZF7GRJu7eFk'

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
#                                                            client_secret=SECRET_KEY))
# album = sp.album(urn)
# pprint(album)