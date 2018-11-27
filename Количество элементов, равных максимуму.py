m = 0
n_m = 0
n = -1
while n != 0:
    n = int(input())
    if n > m:
        m, n_m = n, 1
    elif n == m:
        n_m += 1
print(n_m)