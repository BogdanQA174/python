"""
1203_Методы_и___init__
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
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
            
            
account1 = BankAccount("John Doe", 1000)
account1.deposit(500)
account1.withdraw(200)
print(account1.balance)

account2 = BankAccount("Jane Doe")
account2.deposit(300)
account2.withdraw(100) 
print(account2.balance)


class Book:
    pass

class Reader:
    pass

class Library:
    pass


def hello():
    print("Hello, world!")
    
print(type(hello))