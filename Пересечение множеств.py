a = list(set([int(j) for j in input().split()]) & set([int(j) for j in input().split()]))
for elem in sorted(a):
 print(elem, end=' ')