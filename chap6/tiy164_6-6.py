# Looping through the Keys in a Dictionary
favorite_languages = {
    'john': 'python',
    'sarah': 'c',
    'lisa': 'ruby',
    'phil': 'python',
    'james': 'sql'
    }
learners = [
    'james',
    'sarah',
    'paul',
    ]
for name in favorite_languages.keys():
    print(name.title())

    if name in learners:
        print(f"\t{name.title()}, thank you for responding.")
if 'paul' not in favorite_languages.keys():
    print(f"Paul, you are welcome to take our poll.")