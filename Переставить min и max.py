a = [int(s) for s in input().split()]
min = 0
max = 0
for i in range(1, len(a)):
    if a[i] > a[max]:
        max = i
    if a[i] < a[min]:
        index_of_min = i
a[min], a[max] = a[max], a[min]
print(' '.join([str(i) for i in a]))