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

