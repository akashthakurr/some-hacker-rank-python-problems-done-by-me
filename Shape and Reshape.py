import numpy as np
a=list(map(int,input().split()))
my_arr=np.array(a)
print(np.reshape(my_arr,(3,3)))