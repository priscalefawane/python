# Returning a dictionary.
def make_album(artist_name, title):
    """Return a dictionary describing a music album"""
    music_album = {'artist': artist_name.title(), 'album': title.title()}
    return music_album

album = make_album('luther vandross', 'never too much', )
print(album)
album = make_album('Celine dion', 'Power of love')
print(album)
album = make_album('maria carey', 'caution')
print(album)


print("\n")
# Dictionary with number of songs.
def make_album(artist_name, title, tracks=None):
    """Return a dictionary describing a music album"""
    music_album = {'artist': artist_name.title(), 'album': title.title()}
    if tracks:
        music_album['tracks'] = tracks
    return music_album
album = make_album('Brenda fassie', 'amadlozi', 8)
print(album)
album = make_album('toni braxton', 'the final frontier')
print(album)
album = make_album('oleseng shuping', 'afrika')
print(album)
