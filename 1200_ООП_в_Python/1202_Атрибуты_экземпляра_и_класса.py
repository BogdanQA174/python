"""
1202_Атрибуты_экземпляра_и_класса
"""

class Some:
    pass


some1 = Some()
print(some1)


class Car:
    wheels = 4  # атрибут класса

    def __init__(self, brand, color):
        self.brand = brand  # атрибут экземпляра
        self.color = color  # атрибут экземпляра
        
    def drive(self):
        print(f"{self.brand} is driving.")
        

car1 = Car("Toyota", "blue")
car1.drive()


second_car = Car("Honda", "red")
second_car.drive()