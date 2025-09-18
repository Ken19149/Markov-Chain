frequency = {}
with open("corpus.txt", "r", encoding="utf8") as text: 
    text = text.read()
    length = len(text)
    for i in range(0, len(text)):
        if text[i] in frequency:
            frequency[text[i]][0] += 1
        else:
            frequency[text[i]] = [1, 1/(i+1)] # [count, percent]
        '''
        for j in range(0, len(frequency)):
            frequency[list(frequency.keys())[j]][1] = frequency[list(frequency.keys())[j]][0]/(i+1)
        print()
        print(frequency)
        '''
    for i in range(0, len(frequency)):
            frequency[list(frequency.keys())[i]][1] = frequency[list(frequency.keys())[i]][0]/length

frequency = dict(sorted(frequency.items(), key=lambda item: item[1][0], reverse=True))

with open("data/1c.txt", "w", encoding="utf8") as f:
    f.write(str(frequency))
    # print(frequency)

# 2c // 2 character n-gram
c2 = {}
with open("test.txt", "r", encoding="utf8") as text: 
    text = text.read()
    length = len(text)
    for i in range(0, len(text)):
        if text[i] in c2:
            c2[text[i]][text[i+1]][0] += 1
        else:
            try:
                frequency[text[i]][i+1] = {1, 1/(i+1)} # 
            except:
                 pass
    for i in range(0, len(c2)):
            c2[list(c2.keys())[i]][1] = c2[list(c2.keys())[i]][0]/length

print(c2)