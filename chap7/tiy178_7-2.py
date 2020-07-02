# Using int() to Accept Numerical Input
restaurant_seating = input("How many people are in you dinner group? ")
restaurant_seating = int(restaurant_seating)
if restaurant_seating > 8:
    print(f"\nSorry, you'll have to wait for a table.")
else:
    print(f"\nYour table is ready!")
