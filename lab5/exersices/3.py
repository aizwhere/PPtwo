import re

word = input()

x = re.search("[a-z]+_[a-z]+", word)

if x:
    print(x.group())
    print(word)


