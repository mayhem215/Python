num_g = {}
for _ in range(int(input())):
    candidate, g = input().split()
    num_g[candidate] = num_g.get(candidate, 0) + int(g)

for candidate, g in sorted(num_g.items()):
    print(candidate, g)