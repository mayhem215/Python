def capitalize(word):
    l = word[0]
    b = chr(ord(l) - ord('a') + ord('A'))
    return b + word[1:]


source = input().split()
res = []
for word in source:
    res.append(capitalize(word))
print(' '.join(res))
