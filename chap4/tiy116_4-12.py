# Using for loop to print doesn't save space

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
for food in my_foods:
    print(my_foods)
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\nMy favorite foods are:")
for food in my_foods:
    print(my_foods)

print("\nMy friend's favorite foods are:")
for food in my_foods:
    print(friend_foods)