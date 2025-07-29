import numpy as np

a = np.zeros((3, 3))
b = np.ones((3, 3))
c = np.full((3, 3), 7)
d = np.eye(3)
e = np.arange(0, 10)
f = np.arange(0, 10, 2)
g = np.linspace(0, 1, 5)

for i in [a, b, c, d, e, f, g]:
    print(i, end="\n\n")

