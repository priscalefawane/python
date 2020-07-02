# Starting with sandwiched that has been ordered,
# and an empty list to hold finished sandwiches.
sandwich_orders = [
    'chicken & mayo',
    'pastrami',
    'egg & tomato',
    'cheese & tomato',
    'pastrami',
    'bacon & egg',
    'pastrami',
    ]
finished_sandwiches = []

print(f"Sorry, we are out of pastrami today.\n")

# Removing pastrami from the order list.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Verify each ordered sandwich until there are no more sandwich orders.
# Move each ordered sandwich into the list of finished sandwiches.
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Display all finished sandwiches.
print("\n")
for finished_sandwich in finished_sandwiches:
    print(f"I made a {finished_sandwich} sandwich.")


