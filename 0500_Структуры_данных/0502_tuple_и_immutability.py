"""
0502_tuple_и_immutability
"""

a = (1, 2, 3)
#a[0] = 10
b = (1, 1.1, 'hello')

d = {}
d[(1, 2, 3)] = 'tuple'
print(d[(1, 2, 3)])

t = (1, [1, 2, 3])
t[1].append(4)
print(t)

print(hash((1, 2, 3)))
print(hash((1, 2, 3)) == hash((1, 2, 3)))
#print(hash(t))