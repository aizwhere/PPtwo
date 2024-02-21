import datetime


x = datetime.datetime(2024, 2, 16, 14, 28, 50, 12)
y = datetime.datetime(2024, 2, 16, 14, 28, 59, 9)
print(abs(x.second - y.second))