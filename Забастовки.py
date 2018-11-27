n, k = [int(s) for s in input().split()]
a_i = set([day for day in range(1, n + 1) if day % 7 not in (6, 0)])
a_b = set(a_i)
for party in range(k):
    a, b = [int(s) for s in input().split()]
    max_work = (n - a) // b + 1
    a_b -= {a + b*i for i in range(max_work)}
print(len(a_i) - len(a_b))