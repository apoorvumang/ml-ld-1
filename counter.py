from collections import Counter
import re

# creates 3 files
# 1st is dictionary (list of all words)
# 2nd is list of total documentClasses
# 3rd contains class distribution ie number of documents of each class in training data


f = open("data/document-words.txt", "r")

wordList = []
for line in f.readlines():
    line = line.strip()
    listOfPairs = re.split(',', line)
    for wordCountPair in listOfPairs:
        word = re.split(':', wordCountPair)[0]
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
# write class distribution to file
f = open("data/class-distribution-count.txt", "w")
for x in c.items():
    toWrite = x[0] + ',' + str(x[1])
    f.write(toWrite)
    f.write('\n')

out2 = open("data/classes.txt", "w")
uniqueClasses = list(c)
uniqueClasses.sort()

for documentClass in uniqueClasses:
    out2.write(documentClass)
    out2.write('\n')
