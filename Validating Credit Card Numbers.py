import re
p=re.compile(r'^(?!.*(\d)(?:\-?\1){3}.*)(?=(?:\d{16})|(?:\d{4}\-\d{4}\-\d{4}\-\d{4}))[456][\d-]{15,18}$')
for _ in range(int(input())):
    m=p.match(input())
    if bool(m):
        print('Valid')
    else:
        print('Invalid')