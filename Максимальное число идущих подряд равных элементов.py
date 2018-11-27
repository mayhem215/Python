n = -1
p = 0
m_p = 0
m = int(input())
while m != 0:
    if n == m:
        p += 1
    else:
        n = m
        m_p = max(m_p, p)
        p = 1
    m = int(input())
m_p = max(m_p, p)
print(m_p)