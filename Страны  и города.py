g = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        g[city] = country

for i in range(int(input())):
    print(g[input()])