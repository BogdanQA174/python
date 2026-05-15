"""
1201_Классы_и_объекты
"""


class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color



car1 = Car("Toyota", "blue")
#str1 = "Hello, World!"

Car.__init__(car1, "Toyota", "red")
#str1.index("World")


print(type(car1))
print(car1.brand)
print(car1.color)

car2 = Car("Honda", "black")
print(type(car2))
print(car2.brand)
print(car2.color)


class House:
    def __init__(self, address, floors):
        self.address = address
        self.floors = floors

house1 = House("123 Main St", 3)
print(type(house1))
print(house1.address)
print(house1.floors)