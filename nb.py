from collections import Counter
import re

# for each word + class combination, need to find number of occurences
# in the dataset

# first load all documents along with their classes
documentWordsFile = open("data/words-with-count.txt", "r")
documentClassesFile = open("data/document-classes.txt", "r")

documents = []
for line in documentWordsFile.readlines():
    wordsWithCount = re.split(',|\n', line)
    wordsWithCountNoBlanks = []
    for wordWithCount in wordsWithCount:
        if(wordWithCount):
            x = wordWithCount.split(':')[0]
            y = wordWithCount.split(':')[1]
            entry = [x,int(y)]
            wordsWithCountNoBlanks.append(entry)
    documents.append(wordsWithCountNoBlanks)

documentClasses = []
for line in documentClassesFile.readlines():
    classes = re.split(',|\n| ', line)
    classesNoBlanks = []
    for documentClass in classes:
        if(documentClass):
            classesNoBlanks.append(documentClass)
    documentClasses.append(classesNoBlanks)

# now load wordList (list of all words) and list of all classes

wordList = []
dictionaryFile = open("data/dictionary.txt", "r")
for line in dictionaryFile.readlines():
    line = line.strip()
    if(line):
        wordList.append(line)

classesList = []
classesListFile = open("data/classes.txt", "r")
for line in classesListFile.readlines():
    line = line.strip()
    if(line):
        classesList.append(line)

# all data now loaded in memory
# now need to get count for every word + class combination

table = {}

for word in wordList:
    for documentClass in classesList:
        table[(word, documentClass)] = 0

for i in range(0, len(documents)):
    document = documents[i]
    classes = documentClasses[i]
    for wordCountPair in document:
        word = wordCountPair[0]
        count = wordCountPair[1]
        for documentClass in classes:
            a = table[(word, documentClass)]
            table[(word, documentClass)] += count
    print("Done " + str(i+1) + " documents")

# table no contains all the counts we need
