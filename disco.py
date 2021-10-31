import requests
import logging
import argparse
from discord import Webhook, RequestsWebhookAdapter
from radio import get_songs
from spotify_cred import PAYLOAD

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

    webhook = Webhook.from_url(PAYLOAD, adapter=RequestsWebhookAdapter())
    link = get_songs(args, logger)
    webhook.send(".play " + link)