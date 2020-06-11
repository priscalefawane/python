cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)
print(cubes)

for value in cubes:
    print(value)

print("\n\nThe first three items in the list are:")
print(cubes[:3])
print("\nThree items from the middle of the list are:")
print(cubes[4:7])
print("\nThe last three items from the list are:")
print(cubes[7:])