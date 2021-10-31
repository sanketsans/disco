import warnings

def get_songs_uri(args, sp, logger):
    album_name = args.album
    artist_name = args.artist 
    song_name = args.song
    album_urn =None
    song_urn = []
    clone = 0
    if args.artist != None:
        artist_name = args.artist

        results = sp.search(q='artist:' + artist_name, type='artist')
        items = results['artists']['items']
        artist_uri = items[0]['uri']

        logger.info('Artist found : ' + items[0]['name'])

        results = sp.artist_albums(artist_uri, album_type='album')
        albums = results['items']
        while results['next']:
            results = sp.next(results)
            albums.extend(results['items'])

        logger.info('Total Albums found : ' + str(len(albums)))

        if args.album is not None or args.song is not None:
            for album in albums:
                try:
                    if album_name in album['name'].lower():
                        print('Album NAME: >> ', album['name'], )
                        logger.info('Matching Album found : ' + str(album['name']))

                        clone += 1
                except:
                    pass

                album_urn = album['uri']
                album_tracks = sp.album(album_urn)
                # logger.info('Album Name >>>> : ' + str(album['name']))
                if album_tracks['total_tracks'] > 0:
                    for track in album_tracks['tracks']['items']:
                        # logger.info('All song : ' + str(track['name']))
                        if song_name != None and song_name in track['name'].lower():
                            logger.info('Matching Song found : ' + str(track['name']))

                            song_urn.append(track['uri'])
                
                if clone > 0:
                    break

        if album_urn is None:
            warnings.warn("WARNING: ALBUM NOT FOUND ! playing the artist")
            logger.info('No Matching Album found for : ' + str(args.album))

        if len(song_urn) == 0 :
            warnings.warn("WARNING: SONG NOT FOUND ! playing the album")
            logger.info('No Matching Song found for : ' + str(args.song))

        return artist_uri, album_urn, song_urn