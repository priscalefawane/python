# Copy,add food to the list and print using for loop

my_pizzas = ['chicken & pine', 'pepperoni', 'supreme']
friend_pizzas = my_pizzas[:]
my_pizzas.append('chicken & mushroom')
friend_pizzas.append('something meaty')

# My favorite pizzas

print("\nMy favorite pizzas are:")
for pizza in my_pizzas:
    print(my_pizzas)

# My friend's favorite pizzas.

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(friend_pizzas)


