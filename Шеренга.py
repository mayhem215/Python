a = [int(i) for i in input().split()]
x = int(input())
n = 0
while n < len(a) and a[n] >= x:
    n += 1
print(n + 1)