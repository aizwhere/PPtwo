import re

word = input()

first_word = re.search('^[a-z]+', word)
x = re.findall('[A-Z][a-z]*', word)
if first_word is not None:
    x.insert(0, first_word.group())
answer = '_'.join([i.lower() for i in x])

print(answer)