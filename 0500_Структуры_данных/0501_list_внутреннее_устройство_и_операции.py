"""
0501_list_внутреннее_устройство_и_операции
"""

a = [0, 1, 2, 3, 4]
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])

b = []
print(b)
print(a)

c = [1, '2',  False, 1.1, [1, 2]]
print(c)

numbers = list(range(10))
print(numbers)

data = []
print(data)
data.append(1)
print(data)
data.append(2)
print(data)

print()
for e in c:
    print(e)
    
data = [1, 2, 3]
data[0] = 10
print(data)