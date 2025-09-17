frequency = {}
with open("book content.txt", "r", encoding="utf8") as text: 
# with open("test.txt", "r", encoding="utf8") as text: 
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
    for j in range(0, len(frequency)):
            frequency[list(frequency.keys())[j]][1] = frequency[list(frequency.keys())[j]][0]/length

sorted_frequency = dict(sorted(frequency.items(), key=lambda item: item[1][0], reverse=True))
print(sorted_frequency)