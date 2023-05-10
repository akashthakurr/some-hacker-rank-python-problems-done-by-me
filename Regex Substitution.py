import re
for i in range(int(input())):
  print(re.sub(r"(?<=\s)\|{2}(?=\s)",'or',re.sub(r"(?<=\s)&&(?=\s)",'and',input())))