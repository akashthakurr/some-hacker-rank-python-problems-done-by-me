n, m = map(int, input().split())
array = list(map(int, input().split()))
n_set = set(map(int, input().split()))
m_set = set(map(int, input().split()))

print(len([x for x in array if x in n_set]) - len([x for x in array if x in m_set]))