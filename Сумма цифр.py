N = int(input("Введите число="))
s = 0
while N > 0:
    d = N%10
    N = N // 10
    s += d
    print("Сумма :",s)
