# Defining a function.
def display_message():
    """Display message about
    what I'm leaning in this chapter."""
    print(f"I'm leaning to write functions.")

display_message()


def make_sandwich(*items):
    """Making sandwiches with items."""
    print("\nMaking a delicious sandwich "
          "with the following items:")
    for item in items:
        print(f"-{item}")
    print("You sandwich is ready for collection!")

make_sandwich('cucumber', 'tomato', 'lettuce')
make_sandwich('tuna', 'mayonise')
make_sandwich('cheese', 'tomato', 'egg', 'bacon')


# Using a function with a while loop.
print("\n")
def make_album(artist_name, title):
    """Return a dictionary describing a music album"""
    music_album = {'artist': artist_name.title(),
                   'album': title.title()}
    return music_album

artist_name_prompt = "\nWhich artist do you know? "
title_prompt = "Name one of that artist's album. "

# letting the user when to quit
print("Enter 'q' at any time to quit.")

while True:
    a_name = input(artist_name_prompt)
    if a_name == 'q':
        break
    title = input(title_prompt)
    if title == 'q':
        break
    album = make_album(a_name, title )
    print(album)

