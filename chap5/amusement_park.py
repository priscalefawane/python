age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("You admission cost is $25.")
else:
    print("You admission cost is $40.")

age = 70
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"You admission cost is ${price}.")
