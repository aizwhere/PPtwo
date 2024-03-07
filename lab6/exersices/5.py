import os

f = open("txt.txt", "w")
list = [1, 2, 3, ]

f.write(str(list))

print(list)

f.close()