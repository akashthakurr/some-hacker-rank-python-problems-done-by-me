import cmath

z=complex(input())

phase=cmath.polar(z)

for i in phase:
    print(i)