n = [int(s) for s in input().split()]
b = set()
for num in n:
    if num in b:
        print('Да')
    else:
        print('Нет')
        b.add(num)