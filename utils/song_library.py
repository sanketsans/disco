from logging import warn
import warnings

def get_artist(args, sp, logger):
    artist_uri = None
    if args.artist is not None:
        artist_name = args.artist 
        results = sp.search(q='artist:' + artist_name, type='artist')
        items = results['artists']['items']
        try:
            artist_uri = items[0]['uri']

            logger.info('Specific Artist found : ' + items[0]['name'])
        except:
            logger.info('Specific Artist Not found : ' + args.artist)
            results = sp.search(q=artist_name, limit=5)
            items = results['tracks']['items']
            artist_uri = items[0]['artists'][0]['uri']
            logger.info('Related Artist Not found : ' + items[0]['artists'][0]['name'])
    

    return artist_uri

def get_albums(args, sp, logger, artist_uri=None):
    album_name = args.album
    album_uri = None
    if artist_uri is not None and album_name is not None:
        results = sp.artist_albums(artist_uri, album_type='album')
        albums = results['items']
        while results['next']:
            results = sp.next(results)
            albums.extend(results['items'])

        logger.info('Total Albums found : ' + str(len(albums)))
        if args.album is not None or args.song is not None:
            for album in albums:
                if album_name in album['name'].lower():
                    album_uri = album['uri']
                    logger.info('Matching Album found : ' + str(album['name']))
                    break

    if (artist_uri is None or album_uri is None) and album_name is not None:
        results = sp.search(q=album_name, limit=5)
        items = results['tracks']['items']
        album_uri = items[0]['album']['uri']
        print(album_uri)
        logger.info('Most relatable Album found : ' + items[0]['album']['name'])

    return album_uri

def get_songs(args, sp, logger, album_uri):
    song_name = args.song
    song_uris = []
    if album_uri is not None and song_name is not None:
        album_tracks = sp.album(album_uri)
        # logger.info('Album Name >>>> : ' + str(album['name']))
        if album_tracks['total_tracks'] > 0:
            for track in album_tracks['tracks']['items']:
                # logger.info('All song : ' + str(track['name']))
                if song_name != None and song_name in track['name'].lower():
                    logger.info('Matching Song found : ' + str(track['name']))

                    song_uris.append(track['uri'])
                    break

    if (album_uri is None or len(song_uris) == 0 ) and song_name is not None:
        results = sp.search(q=song_name, limit=5)
        items = results['tracks']['items']
        song_uris.append(items[0]['uri'])
        logger.info('Most relatable song found : ' + items[0]['name'])
        
    return song_uris


def get_radio_station(args, sp, logger):

    artist_uri = get_artist(args, sp, logger)
    album_uri = get_albums(args, sp, logger, artist_uri)
    song_uris = get_songs(args, sp, logger, album_uri)


    if album_uri is None and args.album is not None:
        warnings.warn("WARNING: ALBUM NOT FOUND ! playing the artist")
        logger.info('No Matching Album found for : ' + str(args.album))

    if len(song_uris) == 0 and args.song is not None :
        warnings.warn("WARNING: SONG NOT FOUND ! playing the album")
        logger.info('No Matching Song found for : ' + str(args.song))

    return artist_uri, album_uri, song_uris

