import re
from re import Match

word = input()

x = re.search("ab{2,3}", word)


if x is not None:
    print(word)
else:
    print(None)

