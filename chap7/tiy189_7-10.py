# Filling a Dictionary with user input
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    # prompt for user name and response.
    name = input("what is your name? ")
    place = input("If you could visit one place in the world,"
                  "where would you go? ")

    # Store the response in the dictionary.
    responses[name] = place

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? "
                   "(yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print(f"\n---Poll Results---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")