import re
no_input = int(input())
pattern = r'\#[a-fA-F0-9]{3,6}[;,)]'
for _ in range(no_input):
    user_input = input()
    matches = re.findall(pattern, user_input)
    for match in matches:
        if match[-1] == ',' or match[-1] == ')' or match[-1] == ';':
            match = match.replace(match[-1], '')
        print(match)