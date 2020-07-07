requested_toppings = ['mushrooms', 'green peppers','extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")
if requested_topping == 'green peppers':
    print("Sorry, we are out of green peppers right now")
else:
    print(f"Adding  {requested_topping}.")


for car in cars:
➊ if car == 'bmw':
print(car.upper())
else:
print(car.title())