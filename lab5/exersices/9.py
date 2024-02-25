import re

word= input()

x = re.findall(r'[A-Z][a-z]*', word)

answer = ' '.join(x)

print(answer)