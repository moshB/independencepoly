import numpy as np

p0 = np.array([1])
p1 = np.array([1, 1])


for i in range(50):
    p0 = np.insert(p0, 0, 0)
    if len(p1)<len(p0):
        p1 =np.insert(p1, len(p1), 0)
    p1 = np.pad(p1, (0, len(p0) - len(p1)), 'constant')

    p2 = p1 + p0
    print(p2)
    p0 = p1
    p1 = p2
