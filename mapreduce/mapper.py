#!/usr/bin/env python
"""mapper.py"""
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

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    splitLine = line.split('\t', 2)
    document = splitLine[1]
    document = denoise_text(document)
    document = replace_contractions(document)
    words = nltk.word_tokenize(document)
    words = normalize(words)
    stems = convert_unicode_to_string(stem_words(words))
    c = Counter(stems)
    pairList = []
    for word, count in c.items():
        if(word):
            pairList.append(word + '\t' + str(count))
    # split the line into words
    # increase counters
    for pair in pairList:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print pair
