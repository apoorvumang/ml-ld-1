from collections import Counter
import re

# for each word + class combination, need to find number of occurences
# in the dataset
# these are written to file word-class-count.txt

# these are raw word counts, ie not normalized
# to normalize them, we should divide the word count for a document by the length
# of that document (and then add the count to the table)

# first load all documents along with their classes


# copied from counter.py start


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

f.close()
out1.close()

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

documentClassesFile.close()
f.close()

out2 = open("data/classes.txt", "w")
uniqueClasses = list(c)
uniqueClasses.sort()

for documentClass in uniqueClasses:
    out2.write(documentClass)
    out2.write('\n')
out2.close()

print "Part 1 done"

# copied from counter.py end


documentWordsFile = open("data/document-words.txt", "r")
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
            table[(word, documentClass)] += count

print("Done")
outFile = open("data/word-class-count.txt", "w")
for x, y in table.items():
    toWrite = x[0] + ',' + x[1] + ',' + str(y)
    outFile.write(toWrite)
    outFile.write('\n')
# table no contains all the counts we need
