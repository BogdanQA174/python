"""
0601_Определение_и_вызов_функций
"""

print()

def greet():
    print('Hello')

greet()
greet()
greet()

# b = input()
# c = set()

def greet(name):
    print('Hello, ' + name)

greet('John')
greet(name='John')
#print(1, end='', sep='')

def greet(name, age):
    print('Hello, ' + name + ', you are ' + str(age))

greet('John', 25)
greet(name='John', age=25)


def add(a, b):
    print(a, 'работает 32 строчка')
    print(b, 'работает 33 строчка')
    return a + b

print(add(1, 2), '\n')
print(add(1, 3), '\n')

a = 1
b = 2
print(a, 'работает 41 строчка')
print(b, 'работает 42 строчка', '\n')
print(a + b)

a = 1
b = 3
print(a, 'работает 47 строчка')
print(b, 'работает 48 строчка')
print(a + b)

a = 1
b = 3
print(a, 'работает 47 строчка')
print(b, 'работает 48 строчка')
print(a + b)


for i in range(10):
    print(i)
    
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

a = 1
b = 3
def add(a, b):
    x = 10
    return a + b

print(add(a, b))
#print(x)

# области видимости
# получение/изменение глобальной переменной
# 602
# 606

print(len(range(5)))
print(len([1, 2]))