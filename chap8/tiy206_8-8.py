# Using a function with a while loop.
def make_album(artist_name, title):
    """Return a dictionary describing a music album"""
    music_album = {'artist': artist_name.title(), 'album': title.title()}
    return music_album

artist_name_prompt = "\nWhich artist do you know? "
title_prompt = "Name one of that artist's album. "
print("Enter 'q' at any time to quit.")

while True:
    a_name = input(artist_name_prompt)
    if a_name == 'q':
        break
    title = input(title_prompt)
    if title == 'q':
        break
    album = make_album(a_name, title, )
    print(album)


