# making a list of dictionaries
my_friend = {
    'first_name': 'mpho',
    'last_name': 'mafanyolle',
    'age': 38,
    'city': 'cape town',
    'kids': 3,
    }
print(my_friend['first_name'].title())
print(my_friend['last_name'].title())
print(my_friend['age'])
print(my_friend['city'].title())
print(my_friend['kids'])

my_kid = {
    'first_name': 'neo',
    'last_name': 'lefawane',
    'age': 12,    'gender': 'female',
    'grade': 7,
    }

my_sister = {
    'first_name': 'maggy',
    'last_name': 'lefawane',
    'age': 41,
    'city': 'lephalale',
    'kids': 2,
    }

people = [my_friend, my_kid, my_sister]
for person in people:
    print(person)