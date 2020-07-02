# Using break to exit a loop
prompt = "\nPlease enter the name of the city you have visited:"
prompt += "\nEnter 'quit' when you are finished. "
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'll like to go to {city.title()}!")