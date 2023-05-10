from datetime import datetime
import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(q, b):
    date1 = datetime.strptime(q, "%a %d %b %Y %H:%M:%S %z")
    date2 = datetime.strptime(b, "%a %d %b %Y %H:%M:%S %z")
    difference=abs((date1-date2).total_seconds())
    return int(difference)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = str(time_delta(t1, t2))

        fptr.write(delta + '\n')

    fptr.close()
    print(delta)