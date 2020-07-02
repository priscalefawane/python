# Starting with sandwiched that has been ordered,
# and an empty list to hold finished sandwiches.
sandwich_orders = [
    'chicken & mayo',
    'egg & tomato',
    'cheese & tomato',
    'bacon & egg',
    ]
finished_sandwiches = []

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

