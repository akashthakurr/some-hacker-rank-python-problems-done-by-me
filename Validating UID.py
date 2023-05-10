import re

for _ in range(int(input())):
    uid = input()
    if re.search("[a-zA-Z0-9]", uid) and re.search("[\d]{3,}[A-Z]{2,}", ''.join(sorted([*uid]))) and len(set(uid)) == 10:
        print('Valid')
    else:
        print('Invalid')