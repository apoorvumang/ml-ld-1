from collections import Counter
import re

# first need to load the class+word counts into memory as a dictionary

f = open("data/word-class-count.txt", "r")
table = {}
# format is like
# line = "seventh,The_Football_League_players,2"

NUM_LINES = 2647000.0
VOCABULARY_SIZE = 54030
ALPHA = 0.01
NUM_DOCUMENTS = 1497
totalWords = 0
i = 0
for line in f.readlines():
    line = line.strip()
    splitLine = line.split(',')
    word = splitLine[0]
    documentClass = splitLine[1]
    count = int(splitLine[2])
    table[(word, documentClass)] = count
    totalWords += count
    i += 1
    if(i%10000 == 0):
        print((100.0*i)/NUM_LINES)

# print table[('seventh', 'The_Football_League_players')]

f = open("data/classes.txt", "r")
classesList = []
for line in f.readlines():
    classesList.append(line.strip())

f = open("data/dictionary.txt", "r")
wordList = []
for line in f.readlines():
    wordList.append(line.strip())

# now count table, word list and classes list is loaded

# lets load the test data
# this will first 100 documents of train data

f = open("data/words-with-count.txt", "r")
documents = []
for i in range(0,NUM_DOCUMENTS):
    line = f.readline()
    line = line.strip()
    document = []
    wordsWithCount = re.split(',', line)
    for wordWithCount in wordsWithCount:
        word = wordWithCount.split(':')[0]
        if(word):
            document.append(word)
    documents.append(document)

documentsGroundTruthClass = []
f = open("data/document-classes.txt", "r")
for i in range(0,NUM_DOCUMENTS):
    line = f.readline()
    line = line.strip()
    documentsGroundTruthClass.append(line.split(','))

wordsInClass = {}

print "Getting class-wise word counts"

for documentClass in classesList:
    wordCount = 0
    for word in wordList:
        wordCount += table[(word, documentClass)]
    wordsInClass[documentClass] = wordCount

print "Got class-wise word counts"

# print wordsInTestClass
print "Prediction begins"

i = 0
numCorrect = 0
numWrong = 0
for document in documents:
    bestP = 0.0
    pClass = 'Articles_containing_video_clips'
    for testClass in classesList:
        P = 1
        for word in document:
            if (word, testClass) in table:
                count = table[(word, testClass)]
            else:
                count = 0
            currP = float(count + ALPHA)/float(wordsInClass[testClass] + ALPHA*VOCABULARY_SIZE)
            P *= currP
        if (P > bestP):
            bestP = P
            pClass = testClass
    # print ("Ground truth: " + documentsGroundTruthClass[i] + " Predicted: " + pClass)
    if pClass in documentsGroundTruthClass[i]:
        numCorrect += 1
    else:
        numWrong += 1
    i += 1

print numCorrect
print numWrong
