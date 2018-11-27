x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
yx = abs(x1 - x2)
xy = abs(y1 - y2)
if yx == 1 and xy == 2 or yx == 2 and xy == 1:
    print('Да')
else:
    print('Нет')
