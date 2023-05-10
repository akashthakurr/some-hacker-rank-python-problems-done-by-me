import numpy as np
n, _ = map(int, input().split())
array = np.array([input().split() for _ in range(n)], int)
print(np.transpose(array))
print(array.flatten())