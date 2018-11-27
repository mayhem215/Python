n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
l_i, l_j = 0, 0
max = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > max:
            max = a[i][j]
            l_i, l_j = i, j
print(l_i, l_j)