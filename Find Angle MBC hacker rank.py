from math import atan2 , pi
a, b = int(input()), int(input())
theta = atan2(a,b)/pi*180
print(f'{theta:.0f}\N{DEGREE SIGN}')