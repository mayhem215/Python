m1 = int(input())
m2 = int(input())
if m1 < m2:
    m1, m2 = m2, m1
n = int(input())
while n != 0:
    if n > m1:
        m2, m1 = m1, m2
    elif n > m2:
        m2 = n
    n = int(input())
print(m2)