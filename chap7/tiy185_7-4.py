# Using while loop to let the user choose when to quit
prompt = "Enter pizza_topping:"
prompt += "\nEnter 'quit' when done. "

pizza_topping = ""
while pizza_topping != 'quit':
    pizza_topping = input(prompt)
    if pizza_topping != 'quit':
        print(f"\nI'll add {pizza_topping} to the pizza!\n")
    else:
        break





