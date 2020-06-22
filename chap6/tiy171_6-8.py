# making a list of dictionaries
pet_0 = {
    'kind': 'dog',
    'owner': 'phil',
    'color': 'brown',
    }

pet_1 = {
    'kind': 'rabbit',
    'owner': 'loyd',
    'color': 'white',
    }

pet_2 = {
    'kind': 'hamster',
    'owner': 'callie',
    'color': 'gray & white',
    }

pet_3 = {
    'kind': 'cat',
    'owner': 'joyce',
    'color': 'black',
    }
pets = [pet_0, pet_1, pet_2, pet_3]
for pet in pets:
    print(pet)
