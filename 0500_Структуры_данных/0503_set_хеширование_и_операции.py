"""
0503_set_хеширование_и_операции
"""

a = {1, 2, 3, 3}
#print(a)
a.add(4)
#print(a)
#print(a[0])

b = set()
#print(b)

#set = {1, 'edef', (1, 2), [1, 2]}




print(hash('10'))


s = set()
s.add(10)
s.add('10')
print(s)

#s.add([1, 2])
print(s)

print(hash(10))
print(hash('10'))
print(hash(10) == hash(10))


#пользовательские классы + хеширование