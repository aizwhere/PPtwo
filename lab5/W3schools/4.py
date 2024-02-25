import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print(x.start())
x = re.search("Portugal", txt)
print(x)