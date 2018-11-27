n, k = [int(s) for s in input().split()]
keg = ['I'] * n
for i in range(k):
    l, r = [int(s) for s in input().split()]
    for j in range(l - 1, r):
        keg[j] = '.'
print(''.join(keg))