dic = dict()
for i in range(int(input())):
    english_word,latin_words = list(map(str,input().split(" - ")))
    array_of_latin_words = latin_words.split(", ")
    for j in range(len(array_of_latin_words)):
        if(array_of_latin_words[j] not in dic):
            dic[array_of_latin_words[j]]= english_word
        else:
            dic[array_of_latin_words[j]] = dic[array_of_latin_words[j]]+", "+english_word
print(len(dic.keys()))
for latin_word,english_word in sorted(dic.items()):
    print(latin_word+' - '+english_word)