p = int(input())
x = int(input())
y = int(input())

do = 100 * x + y
posle = int(do * (100 + p) / 100)

print(posle // 100, posle % 100)