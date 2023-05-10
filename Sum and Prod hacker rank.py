import numpy as np
n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append([i for i in map(int,input().split())])
print(np.prod(np.sum(np.array(a),axis = 0)))