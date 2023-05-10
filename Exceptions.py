T = int(input())

for i in range(T):
    try:
        a, b = map(int,input().split())
        print(a//b)
    except (ZeroDivisionError, ValueError) as e:
        print('Error Code:', e)