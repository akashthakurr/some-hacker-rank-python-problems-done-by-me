m = int(input())
m_set = set(map(int, input().split(' ')))
n = int(input())
n_set = set(map(int, input().split(' ')))

dif = sorted(m_set.symmetric_difference(n_set))
print('\n'.join([str(x) for x in dif]))