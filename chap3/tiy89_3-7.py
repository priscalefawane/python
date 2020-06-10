# People to invite for dinner

guests = ['grace', 'john', 'lisa']
print(guests)
message = f"Hi {guests[0].title()}, you are kindly invited for dinner at my place this Friday 19:30."
print(message)
message = f"Hello {guests[1].title()}! you are kindly invited for dinner, \n\tDay: Friday \n\tVaneu: 479 Umfuyaneni Sec \n\tTime: 19:30"
print(message)
message = f"Hi {guests[2].title()} my friend!! I'm inviting you for dinner on Friday 19:30 at my place."
print(message)
# Guest who can't make it

print(f"Unfortunately {guests[1].title()} can't make it.")

# replacing the name of the guest who can't make it

guests[1] = 'joe'
print(guests)

# invitation messages for people on the new list

message = f"Hi {guests[0].title()}, you are kindly invited for dinner at my place this Friday 19:30."
print(message)
message = f"Hi {guests[1].title()}, you are kindly invited for dinner at my place this Friday 19:30."
print(message)
message = f"Hi {guests[2].title()}, you are kindly invited for dinner at my place this Friday 19:30."
print(message)

print(f"Hello {guests[0].title()}! I found a bigger dinner table.")
print(f"Hello {guests[1].title()}! I found a bigger dinner table.")
print(f"Hello {guests[2].title()}! I found a bigger dinner table.")

# Three more people to add on my guest list

guests.insert(0, 'neo')
print(guests)
guests.insert(2, 'linah')
print(guests)
guests.insert(5, 'sam')
print(guests)

# Invitation messages for all in the list

message = f"Hi {guests[0].title()}, you are kindly invited for dinner at my place this Friday 19:30."
print(message)
message = f"Hi {guests[1].title()}, you are kindly invited for dinner at my place this Friday 19:30."
print(message)
message = f"Hi {guests[2].title()}, you are kindly invited for dinner at my place this Friday 19:30."
print(message)
message = f"Hi {guests[3].title()}, you are kindly invited for dinner at my place this Friday 19:30."
print(message)
message = f"Hi {guests[4].title()}, you are kindly invited for dinner at my place this Friday 19:30."
print(message)
message = f"Hi {guests[5].title()}, you are kindly invited for dinner at my place this Friday 19:30."
print(message)

# Dinner table won't arrive  in time for dinner

message = f"\nBecause of space,I can invite only two people."
print(message)

# People that I have to cancel the invite with because of the space

message = f"I'm really sorry {guests[5].title()}, I can't invite you to the dinner."
print(message)
guests.pop(5)
print(guests)
message = f"I'm really sorry {guests[0].title()}, I can't invite you to the dinner."
print(message)
guests.pop(0)
print(guests)
message = f"I'm really sorry {guests[1].title()}, I can't invite you to the dinner."
print(message)
guests.pop(1)
print(guests)
message = f"I'm really sorry {guests[1].title()}, I can't invite you to the dinner."
print(message)
guests.pop(1)
print(guests)
message = f"Hi {guests[0].title()}, you are still invited to dinner."
print(message)
message = f"Hi {guests[1].title()}, you are still invited to dinner."
print(message)
del guests[0]
print(guests)
del guests[0]
print(guests)

print(guests)
