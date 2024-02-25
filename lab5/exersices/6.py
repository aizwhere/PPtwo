import re

word = input()

x = re.sub("[\s\.\,]", ":", word)

print(x)