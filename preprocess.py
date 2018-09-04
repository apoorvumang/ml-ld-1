import re
import sys
import nltk
import contractions
import inflect
from collections import Counter
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer

# reference: https://www.kdnuggets.com/2018/03/text-data-preprocessing-walkthrough-python.html
# takes as input the data file and creates 2 files
# 1st contains list of documents (1 per line). each document consists of a list of word:count pairs
# 2nd contains class(es) of each document

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

FIRST_LINE_INDEX = 0

def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

def remove_unicode(text):
    """Replace unicode codes like \uxxxx with space"""
    regex = r"(\\u....)"
    text = re.sub(regex, ' ', text)
    return text

def denoise_text(text):
    text = strip_html(text)
    text = remove_unicode(text)
    text = remove_punctuation(text)
    return text

def replace_contractions(text):
    """Replace contractions in string of text"""
    return contractions.fix(text)

def to_lowercase(words):
    """Convert all characters to lowercase from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words

def remove_punctuation(text):
    """Remove punctuation and replace with space"""
    text = re.sub(r'[^\w\s]', ' ', text)
    return text


# TODO: somehow stop words removal is taking considerable time if input file is
#       train (large) but not for smaller files
def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        if word not in stopwords.words('english'):
            new_words.append(word)
    return new_words

def stem_words(words):
    """Stem words in list of tokenized words"""
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems

def normalize(words):
    words = to_lowercase(words)
    words = remove_stopwords(words)
    return words

def convert_unicode_to_string(words):
    new_words = []
    for word in words:
        new_words.append(word.encode('ascii','ignore'))
    return new_words

f = open("data/DBPedia.full.hdfs/full_devel.txt")
f1 = f.readlines()
lines = []
for x in f1:
    lines.append(x)

lines = lines[FIRST_LINE_INDEX:]
documentClasses = []
documents = []

for line in lines:
    splitLine = line.split('\t', 2)
    documentClasses.append(splitLine[0])
    documents.append(splitLine[1])

# write document classes to file
documentClassesFile = open("data/document-classes.txt", "w")
for documentClass in documentClasses:
    documentClassesFile.write(documentClass)
    documentClassesFile.write('\n')

totalWordCount = 0
documentsDoneCount = 1
f = open("data/document-words.txt", "w")
for document in documents:
    document = denoise_text(document)
    document = replace_contractions(document)
    words = nltk.word_tokenize(document)
    words = normalize(words)
    print("Documents done: ", documentsDoneCount)
    documentsDoneCount += 1
    stems = convert_unicode_to_string(stem_words(words))
    c = Counter(stems)
    pairList = []
    for word, count in c.items():
        if(word):
            pairList.append(word + ':' + str(count))
    appendedList = ','.join(pairList)
    f.write(appendedList)
    f.write('\n')
    totalWordCount += len(stems)
print('Total word count: ', totalWordCount)
