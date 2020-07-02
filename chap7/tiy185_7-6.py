# Using while statement to stop the loop
prompt = "Enter pizza_topping:"
prompt += "\nEnter 'quit' when done. "

pizza_topping = ""
while pizza_topping != 'quit':
    pizza_topping = input(prompt)
    if pizza_topping != 'quit':
        print(f"\n\tI'll add {pizza_topping} to the pizza!\n")

# Using an active variable to control
# how long the loop runs.
active = True
while active:
    pizza_topping = input(prompt)
    if pizza_topping == 'quit':
        active = False
    else:
        print(f"\n\t{pizza_topping.title()} is horrible!\n")

# Use a break statement to exit the loop
# when the user enters a 'quit' value.
while True:
    pizza_topping = input(prompt)
    if pizza_topping == 'quit':
        break
    else:
        print(f"\n\tWow, {pizza_topping} is so delicious!\n")




