import re

word = input()

x = re.search("ab*", word)

if x is not None:
    print(word)
else:
    print("None")