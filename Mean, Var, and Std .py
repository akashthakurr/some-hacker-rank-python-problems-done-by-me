import numpy as np

N, M = map(int, input().split())
arr = np.array([input().split() for _ in range(N)], float)
print(np.mean(arr, axis=1), np.var(arr, axis=0), round(np.std(arr), 11), sep='\n')