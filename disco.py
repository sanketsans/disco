import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import argparse
from pprint import pprint
import logging
from utils.get_songs import get_songs_uri

parser = argparse.ArgumentParser()


from spotify_cred import CLIENT_ID, SECRET_KEY

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
#                                                            client_secret=SECRET_KEY))
parser.add_argument("--artist", default=None, help="select artist")
parser.add_argument("--album", default=None, help="select album")
parser.add_argument("--song", default=None, help="select song")
parser.add_argument("--clone", type=int, default=1, help="no. of copies album")
args = parser.parse_args()

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.warning('This will get logged to a file')

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                           client_secret=SECRET_KEY))

logger.info('Authentication done')

artist_uri, album_urn, song_urn = get_songs_uri(args, sp, logger)
link = None
if len(song_urn) > 0:
    link = 'https://open.spotify.com/track/' + song_urn[0].split(":")[-1]
elif album_urn is not None :
    link = 'https://open.spotify.com/album/' + album_urn.split(":")[-1]
elif artist_uri is not None:
    link = 'https://open.spotify.com/artist/' + artist_uri.split(":")[-1]

print(song_urn, album_urn, artist_uri)
print(link)

        