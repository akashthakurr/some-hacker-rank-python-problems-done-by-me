import numpy
numpy.set_printoptions(legacy='1.13')

Arr=numpy.array(input().split(),float)

print(numpy.floor(Arr))
print(numpy.ceil(Arr))
print(numpy.rint(Arr))