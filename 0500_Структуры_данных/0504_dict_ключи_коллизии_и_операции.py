"""
0504_dict_ключи_коллизии_и_операции
"""

print(type({}))

d = {1: 'a', 2: 'b', 3: 'c'}
print(d[2])
data = {
    'name': 'John',
    'age': 30,
    'children': ['Mary', 'Bob']
}
data = dict(name='John', age=30, children=['Mary', 'Bob'])
print(data['age'])
data['role'] = 'admin'
data['role'] = 'user'

print(data)
data.