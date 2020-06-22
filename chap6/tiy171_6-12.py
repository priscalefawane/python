# Information about a particular alien
alien_0 = {
    'color': 'green',
    'points': 5,
    }
print(alien_0['color'])
print(alien_0['points'])

# adding items in dictionary
alien_0['year'] = 16
alien_0['name'] = "bialar"

# Checking if 'year' is present in dictionary
if 'year' in alien_0:
    print(f"\nWow! Bialar is now older.\n")

# changing the color
alien_0['color'] = 'yellow'
for key, value in alien_0.items():
    print(f"{key.title()}: \n\t{value}\n")

# deleting point from the dictionary
# Printing the dictionary
del alien_0['points']
print(alien_0)

# The number of items in dictionary
print("\nThe number of items is:")
print(len(alien_0))









