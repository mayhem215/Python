x1 = input()
y1 = input()
x2 = input()
y2 = input()

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')
