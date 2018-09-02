from collections import Counter
import re

# creates 3 files
# 1st is words-with-counts for each document
# 2nd is list of total documentClasses
# 3rd is dictionary (list of all words)

f = open("data/document-words.txt", "r")
f2 = open("data/words-with-count.txt", "w")

f1 = f.readlines()
lines = []
for x in f1:
    lines.append(x)

for line in lines:
    words = re.split(',|\n', line)
    c = Counter(words)
    pairList = []
    for word, count in c.items():
        if(word):
            pairList.append(word + ':' + str(count))
    appendedList = ','.join(pairList)
    f2.write(appendedList)
    f2.write('\n')


wordList = []
for line in lines:
    words = re.split(',|\n', line)
    for word in words:
        if(word):
            wordList.append(word)

c = Counter(wordList)

out1 = open("data/dictionary.txt", "w")
uniqueWords = list(c)
uniqueWords.sort()

for word in uniqueWords:
    out1.write(word)
    out1.write('\n')

documentClassesFile = open("data/document-classes.txt", "r")
classList = []
lines = []
for line in documentClassesFile.readlines():
    classes = re.split(',|\n| ', line)
    for documentClass in classes:
        if(documentClass):
            classList.append(documentClass)
c = Counter(classList)
out2 = open("data/classes.txt", "w")
uniqueClasses = list(c)
uniqueClasses.sort()

for documentClass in uniqueClasses:
    out2.write(documentClass)
    out2.write('\n')
