"""
0205_bool
"""

flag1 = True
flag2 = False


"""операторы сравнения
>
<

>=
<=

==
!=
"""
a = 10
b = 3
"""
логическое выражение
"""
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)
print()

print("5 > 3", 5 > 3)
print("5 < 3", 5 < 3)
print("5 >= 3", 5 >= 3)
print("5 <= 3", 5 <= 3)
print("5 == 3", 5 == 3)
print("5 != 3", 5 != 3)
print()
"""
False (0)
True (1)

логические операторы
and (и) (*)
or (или) (+)
not (не) (!) (инверсия)
"""

print(False and 5 < 4 or not True and 8 != 8 and (not 7 <= 9 or a != b))

print(True and False)
#      1 * 0
print(True or False)
#      1 + 0


print(True + True)
print(True + False)
print(False + True)
print(False + False)

print(True * True)
print(True * False)
print(False * True)
print(False * False)


print(type(5 > 3))


