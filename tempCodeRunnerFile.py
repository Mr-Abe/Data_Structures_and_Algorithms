from Data_structures.DynamicArray import DynamicArray


Arr = DynamicArray(15)

for i in range(2000):
    Arr.pushback(i)

for i in range(0, 2000, 75):
    Arr.set(i, f"hello instead of {i}, I inserted {i * 2}")

for i in range(2000):
    print(Arr.popback())