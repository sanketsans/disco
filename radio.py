import warnings
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import argparse
from pprint import pprint
import logging
from utils.song_library import get_radio_station
from spotify_cred import SP_CLIENT_ID, SP_SECRET_KEY
import sys

def get_songs(args, logger):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SP_CLIENT_ID,
                                                            client_secret=SP_SECRET_KEY))

    artist_uri, album_urn, song_urn = get_radio_station(args, sp, logger)
    link = None
    if len(song_urn) > 0:
        link = 'https://open.spotify.com/track/' + song_urn[0].split(":")[-1]
    elif album_urn is not None :
        link = 'https://open.spotify.com/album/' + album_urn.split(":")[-1]
    elif artist_uri is not None:
        link = 'https://open.spotify.com/artist/' + artist_uri.split(":")[-1]
    else:
        warnings.warn('type -h for help')

    return link

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--artist", default=None, help="select artist")
    parser.add_argument("--album", default=None, help="select album")
    parser.add_argument("--song", default=None, help="select song")
    # parser.add_argument("--clone", type=int, default=1, help="no. of copies album")
    args = parser.parse_args()

    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.warning('This will get logged to a file')

    logger.info('Authentication done')

    get_songs(args, logger)
    



        