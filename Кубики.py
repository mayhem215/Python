n,m =[int(i) for i in input().split()]
k1 = set(int(input()) for _ in range(n))
k2 = set(int(input()) for _ in range(m))
for i in (k1 & k2,k1 - k2,k2 - k1):
    print(len(i))
    print(*(sorted(i)))