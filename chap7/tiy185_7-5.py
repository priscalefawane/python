# Write a loop in which you ask users their age,
# and then tell them the cost of their movie ticket.
prompt = "How old are you? "
prompt += "\nEnter 'quit' when you are done. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print(f"Your ticket is free!")
    elif age < 13:
        print(f"Your ticket is $10!")
    else:
        print(f"Your ticket is $15!")