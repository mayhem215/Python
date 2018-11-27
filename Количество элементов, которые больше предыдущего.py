n = int(input())
i = 0
while n != 0:
    m = int(input())
    if m != 0 and n < m:
        i += 1
    n = m
print(i)