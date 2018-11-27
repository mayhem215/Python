from math import sqrt

s = 0
sum = 0
x_i = int(input())
n = 0
while x_i != 0:
    n += 1
    s += x_i
    sum += x_i ** 2
    x_i = int(input())
print(sqrt((sum - s ** 2 / n) / (n - 1)))