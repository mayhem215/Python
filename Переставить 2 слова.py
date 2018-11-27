s = input()
w1 = s[:s.find(' ')]
w2 = s[s.find(' ') + 1:]
print(w2 + ' ' + w1)