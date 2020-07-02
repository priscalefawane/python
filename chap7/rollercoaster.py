# Using int() to Accept Numerical Input
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print(f"\nYou're tall enough to ride!")
else:
    print(f"\n You'll be able to ride when you're a little older.")