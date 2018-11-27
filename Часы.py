n = input("Введите время: ")

n = float(n)

hours = n % (60 * 24) // 60
minutes = n % 60

print(hours, minutes)

