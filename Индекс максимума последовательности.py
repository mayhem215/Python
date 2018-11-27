max = 0
i = -1
n = -1
p = 0
while n != 0:
    n = int(input())
    if n > max:
        max = n
        i = p
    p += 1
print(i)