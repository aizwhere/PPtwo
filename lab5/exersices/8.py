import re

word = input()

x = re.split('[A-Z]', word)

print(x)