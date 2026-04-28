"""
0206_str_immutability_и_slicing
"""

s = 'hello'
print(s)
print("hello world")
s = 'hello world'
s = "hello world!@#$%^&*()_+1234567890-=P}{L:<>?l;',./[]"
s = '456'
s = s + '123'
print(s)
print(s + '123')
print(s * 2)
s = 'hello world'
print(s.capitalize())

# str[index]
s = 'hello worl'
#    0123456789

s = 'hello worl'
#            -1

# str[index]
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print('-' * 20)
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])

""" 
start - начальный индекс
stop - конечный индекс, stop - не включается
step - шаг
"""

# str[start:stop]
# str[start:]
# str[:stop]
# str[start:stop:step]
# str[::step]
s = 'hello worl'

print('-' * 20)
print(s[2:4]) # ll
print(s[:2]) # he
print(s[2:]) # llo worl
print(s[2:9:1]) # llo wor
print(s[1:9:2]) # el o
print(s[1:9:3]) # eoo
print(s[::2]) # hlowr

print(s[::-1])

print('-' * 20)

print(s)
print(type(s))