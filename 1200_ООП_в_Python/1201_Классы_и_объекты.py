"""
1201_Классы_и_объекты
"""


"""экземпляр - конкретный объект созданный на основе класса
атрибут(поле) класса - принадлежит самому классу и разделяется всеми экземплярами
атрибут(поле) экземпляра - принадлежит конкретному объекту  и уникален для каждого экземпляра
метод экземпляра def - функция конкретного объекта
метод класса @classmethod- работает с классом в целом
метод статический @staticmethod- не зависит от класса или объекта, нет доступа, но относится
конструктор __init__- вызывается при создании объекта
наследование - новый класс на основе существующего
полиморфизм - возможность использовать один и тот же интерфейс (метод) для объектов разных классов
инкапсуляция __ - скрытие деталей
свойство - атрибут поволяющий управлять доступом к данным через гет сет дел
дескриптор - объект который оперделяет поведение атрибутов класса __гет__ __сет__ __удалить__
магические методы - __???__ для перегрузки операторов
абстрактный класс - используется как шаблон, указываются методы для реализации
метакласс - определяет поведение других классов
множественное наследование
MRO - порядок поиска методов в иерархии наследования
перегрузка - переопределение поведения операторов и функций
сеттер - устанавливает значение атрибута
геттер - возвращает значение атрибута
делитер - метод удаляет атрибут
приватный атрибут - не предназначен для доступа извне
декораторы - через @
миксины - классы с доп функционалом, не предназначены для самостоятельного использования
"""

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"{self.brand} is driving.")

    def stop(self):
        print(f"{self.brand} has stopped.")
    
    
    
car1 = Car("Toyota", "blue")
car1.drive()

car2 = Car("Honda", "red")
car2.drive()

product_name = 'Laptop'
product_price = 1500
product_qantity = 10

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity
    
    def show_info(self):
        print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

product1 = Product("Laptop", 1500, 10)
print(product1.total_value())
product1.show_info()


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")


account1 = BankAccount("123456789", 1000)
account1.deposit(500)
account1.withdraw(200)

print(account1.balance)


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        
    def show_name(self):
        print(f"Username: {self.username}")

user1 = User("john_doe", "john@example.com")
user1.show_name()


class User:
    @classmethod
    def method_name(cls):
        pass
    
    
class User:
    count = 0
    
    def __init__(self, username):
        self.username = username
        User.count += 1
        
    @classmethod
    def get_user_count(cls):
        print(f"Total users: {cls.count}")

print(User.count)
user1 = User("john_doe")
user2 = User("jane_doe")
user3 = User("alice")
User.get_user_count()

user = User("john_doe")

#data = "John Doe,25"

class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age
        
    @classmethod
    def from_string(cls, data):
        username, age = data.split(",")
        return cls(username, int(age))
    
user = User.from_string("John Doe,25")
print(user.username)
print(user.age)


def method(self):
    pass

@classmethod
def class_method(cls):
    pass

@staticmethod
def static_method():
    pass


class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    
print(Math.add(5, 3))
print(Math.subtract(5, 3))


class Currency:
    rate = 90
    
    @classmethod
    def change_rate(cls, new_rate):
        cls.rate = new_rate
        
Currency.change_rate(100)
print(Currency.rate)