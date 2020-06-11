# Using for loop to print tuple items

buffet_foods = ('ribs', 'nuggets', 'sandwich', 'fruit salad', 'chips')
for food in buffet_foods:
    print(food.title())

# Replacing tuple items

print("\nOriginal buffet_foods:")
for food in buffet_foods:
    print(food.title())

buffet_foods = ('ribs', 'nuggets', 'buns', 'vegetable salad', 'chips')
print("\nModified buffet_foods:")
for food in buffet_foods:
    print(food)

# Trying to modify one of the items, and making sure that python rejects the change

buffet_foods[3] = ('rice',)
for food in buffet_foods:
    print(food.title())
