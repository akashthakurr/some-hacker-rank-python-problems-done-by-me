import re

def fun(s):
        reg = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
        if re.match(reg, s):
                return True
        else:
                return False