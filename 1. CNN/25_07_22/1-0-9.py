import numpy as np

a = np.random.rand(3)
b = np.random.rand(2, 3)

print(a)
print()
print(b)

c = np.random.randint(1, 10, 3)
d = np.random.randint(1, 10, (2, 3))

print(c)
print()
print(d)

e = np.array([1, 2, 3, 4, 5])
np.random.shuffle(e)

print(e)


