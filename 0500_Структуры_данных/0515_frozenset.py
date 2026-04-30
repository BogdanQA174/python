"""
0515_frozenset
"""

set1 = {1, 2, 3, 3}
print(set1)

set2 = frozenset({1, 2, 3, 3})
print(set2)
set2.add(4)