"""
1204_Инкапсуляция
"""

balance = -10000000

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("недостаточно средств")
        
account = BankAccount('Иван', 1000)
account.deposit(500)
print(account.balance)

account.withdraw(300)
print(account.balance)

"""
private
protected
public
"""


class User:
    # def __init__(self, name):
    #     self._name = name
        
    def __init__(self, name):
        self.__name = name
        
        
user = User("anna")
#print(user.__name)


class Temperature:
    def __init__(self):
        self._celsius = 0
    
    def set_temperature(self, value):
        if isinstance(value, (int, float)):
            self._celsius = value
        else:
            print('температура должна быть числом')
            
    def get_temperature(self):
        return self._celsius
    
    def _convert_to_fahrenheit(self):
        return self._celsius * 9 / 5 + 32
    
    
temp = Temperature()
temp.set_temperature(25)
print(temp.get_temperature())
temp.set_temperature("hot")