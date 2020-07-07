# Test using equality and inequality
animal = 'Lion'
print("\nIs animal.lower() == 'lion'? I predict True.")
print(animal.lower() == 'lion')
print("Is animal.lower == 'Lion'? I predict False.")
print(animal == 'lion')

print("\nIs animal.lower() != 'Lion'? I predict True.")
print(animal.lower() != 'Lion')
print("Is animal.lower != 'lion'? I predict False.")
print(animal == 'lion')

# Numerical test using equality and inequality
year = 2020
print("\nIs year == 2020? That's True.")
print(year == 2020)
print("Is year == 2002? I predict false.")
print(year == 2002)

print("\nIs year != 2002? That's True.")
print(year == 2020)
print("Is year != 2020? I predict false.")
print(year == 2002)

# Numerical test using greater than and less than
digit = 5
print("\nIs digit > 3? That's True.")
print(digit > 3)
print("Is digit > 7? I predict false.")
print(digit > 7)

print("\nIs digit < 9? That's True.")
print(digit < 9)
print("Is digit < 1? I predict false.")
print(digit < 1)

# Numerical test using greater than or equal to
age = 33
print("\nIs age >= 33? That's True.")
print(age >= 33)
print("Is age >= 48? I predict false.")
print(age >= 48)

# Numerical test using less than or equal to
print("\nIs age <= 33? That's True.")
print(age <= 33)
print("Is age <= 25? I predict false.")
print(age <= 25)

# Checking weather both boxes have 10 items, using and keyword
box_1 = 12
box_2 = 5
print("\nIs box_1 >= 10 and box_2 >=10?")
print(box_1 >= 10 and box_2 >= 10)
box_2 = 12
print("Is box_1 >= 10 and box_2 >=10?")
print(box_1 >= 10 and box_2 >= 10)

# Checking weather both boxes have 10 items, using or keyword
box_1 = 12
box_2 = 5
print("\nIs box_1 >= 10 or box_2 >=10?")
print(box_1 >= 10 or box_2 >= 10)
box_1 = 5
print("Is box_1 >= 10 or box_2 >=10?")
print(box_1 >= 10 or box_2 >= 10)

# Testing weather an item is not in the list
first_teams = ['orange',
               'blue',
               'red']
team = 'green'
if team not in first_teams:
    print(f"\nTeam {team}, you are not going to the semi final.")

