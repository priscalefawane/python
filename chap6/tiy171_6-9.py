# Making a list in a dictionary
favorite_places = {
    'neo': ['school', 'mall', 'library'],
    'callie': ['mall', 'tavern', 'casino' ],
    'tshia': ['cinema', 'home', 'theatre'],
    'mpho': ['gym', 'work', 'home'],
    'lisa': ['pub', 'club', 'tavern'],
    }
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"{place.title()}")