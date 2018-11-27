n= {}
for word in input().split():
    n[word] = n.get(word, 0) + 1
    print(n[word] - 1, end=' ')