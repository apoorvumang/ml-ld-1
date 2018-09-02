from collections import Counter
import re

# for each word+class combination, need to find number of occurences
# in the dataset

# first load all documents along with their classes
documentWordsFile = open("data/words-with-count.txt", "r")
documentClassesFile = open("data/document-classes.txt", "r")

documents = []
for line in documentWordsFile.readlines():
    wordsWithCount = re.split(',|\n', line)
    wordsWithCountNoBlanks = []
    for word in wordsWithCount:
        if(word):
            wordsWithCountNoBlanks.append(word)
    documents.append(wordsWithCountNoBlanks)
print documents[0]

documentClasses = []
for line in documentClassesFile.readlines():
    classes = re.split(',|\n| ', line)
    classesNoBlanks = []
    for documentClass in classes:
        if(documentClass):
            classesNoBlanks.append(documentClass)
    documentClasses.append(classesNoBlanks)
print documentClasses[0]

# now load wordList (list of all words) and list of all classes

wordList = []
dictionaryFile = open("data/dictionary.txt", "r")
for line in dictionaryFile.readlines():
    line = line.strip()
    if(line):
        wordList.append(line)
print wordList[100]

classesList = []
classesListFile = open("data/classes.txt", "r")
for line in classesListFile.readlines():
    line = line.strip()
    if(line):
        classesList.append(line)
print classesList[0]

c = 0
# for i in range(0, 54000):
#     for j in range(0, 10500):
#         c += 1
#     print i
print c
