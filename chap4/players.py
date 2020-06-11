# Slicing a list (to output element from the list)

players =['charles', 'martina', 'michael', 'florance', 'eli']
print(players[0:3])
print(players[:5])
print(players[2:])
print(players[-3:])
print(players[:-2])
print(players[0:5])

# Using slice in a for loop

players =['charles', 'martina', 'michael', 'florance', 'eli']
print("\nHere are my three players on my team:")
for player in players[:3]:
    print(player.title())

print("\nMy last two players on my team:")
for player in players[3:]:
    print(player.title())