from re import fullmatch
from email.utils import parseaddr

N = int(input())

for _ in range(N):
    input_line = input()

    if fullmatch(r"[a-zA-Z][a-zA-Z0-9_\-\.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}", parseaddr(input_line)[1]):
        print(input_line)