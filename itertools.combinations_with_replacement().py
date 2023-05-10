
from itertools import combinations_with_replacement
io = input().split();
char = sorted(io[0]);
N = int(io[1]);
for i in combinations_with_replacement(char,N):
    print(''.join(i));