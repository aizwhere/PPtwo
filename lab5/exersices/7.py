import re

word = input()

x = re.split(r'_', word)
answer = ''.join([x[0]] + [x[i].capitalize() for i in range(1, len(x))])
print(answer)