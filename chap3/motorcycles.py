motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles[2] = 'kawasaki'
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)
motorcycles.insert(2, 'kawasaki')
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[2]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
motorcycles.append('suzuki')
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"the last motorcycle I owned was a {last_owned.title()}.")
first_owned = motorcycles.pop(0)
print(f"The first motorcycled I owned was a {first_owned.title()}.")

motorcycles = ['honda', 'yahama', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
motorcycles.insert(3, 'ducati')
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

print(motorcycles[3])
motorcycles[]
print(motorcycles[-1])