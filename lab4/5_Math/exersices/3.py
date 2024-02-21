import math

number, length = int(input()), int(input())

area = number * length * length / (4 * math.tan(math.pi / number))

#print("{:.2f}".format(area))
print(int(area))