def count_down(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())

for num in count_down(n):
    print(num)
