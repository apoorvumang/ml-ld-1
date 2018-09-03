from collections import Counter
import re

# first need to load the class+word counts into memory as a dictionary

f = open("data/word-class-count.txt", "r")
table = {}
# format is like
# line = "seventh,The_Football_League_players,2"



NUM_LINES = 2647000.0
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
    if(i%1000 == 0):
        print((100.0*i)/NUM_LINES)

print table[('seventh', 'The_Football_League_players')]
