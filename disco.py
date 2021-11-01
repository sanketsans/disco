import requests
import logging
import argparse

from requests.api import head
from radio import get_songs
from spotify_cred import PAYLOAD, DC_CLIENT_ID, DC_SECRET_KEY

import base64

API_ENDPOINT = 'https://discord.com/api/v8'

def get_token():
  data = {
    'grant_type': 'client_credentials',
    'scope': 'identify connections'
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers, auth=(DC_CLIENT_ID, DC_SECRET_KEY))
  r.raise_for_status()
  return r.json()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--artist", default=None, help="select artist")
    parser.add_argument("--album", default=None, help="select album")
    parser.add_argument("--song", default=None, help="select song")
    parser.add_argument("--clone", type=int, default=1, help="no. of copies album")
    args = parser.parse_args()

    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.warning('This will get logged to a file')

    logger.info('Authentication done')

    link = get_songs(args, logger)

    payload = {"content": '.play ' + link}
    disc = 'https://discord.com/api/v8/channels/904505626409959507/messages/'
    header = {'authorization': 'S8w2zCekk1CM1cpU9nFKIFyLhFPSlU0I1CgaRCxaMu4JQbsLKhqG8ZDVUJxqgtKQrQNk'}
    response = requests.post(disc, json=payload, headers=header)


    print(response.content)