# a.copy是浅拷贝，浅copy只copy了父类

import copy

a = [1, 2, [3, 4]]
b = a
e = a.copy()
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(3)
a[2].append(5)
print(a)
print(b)
print(e)
print(c)
print(d)
print(id(a))
print(id(b))
print(id(e))
print(id(c))
print(id(d))