magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    print(f"Thank you, everyone. That was a great magic show!")

# Unnecessary indent after a loop

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print(f"Thank you, everyone. That was a great magic show!")


 # what happens when you forgot the colon (syntax error)

magicians = ['alice', 'david', 'carolina']
for magician in magicians
    print(magician)