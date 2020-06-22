# Making a list in a dictionary
favorite_numbers = {"tshiamo": [5, 6, 9],
                    'lesego': [1, 2],
                    'neo': [3, 7],
                    'mpho': [4, 6, 8, 11],
                    'caspri': [1, 2, 12],
                    'grace': [9, 13, 20],
                    'tumi': [2, 7],
                    }
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
