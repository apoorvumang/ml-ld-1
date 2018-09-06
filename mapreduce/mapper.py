#!/usr/bin/python
import re
import sys
import nltk
import contractions
import inflect
from collections import Counter
from bs4 import BeautifulSoup
from nltk.stem import LancasterStemmer, WordNetLemmatizer


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



def stem_words(words):
    """Stem words in list of tokenized words"""
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems

def convert_unicode_to_string(words):
    new_words = []
    for word in words:
        new_words.append(word.encode('ascii','ignore'))
    return new_words



# document = denoise_text(document)
# document = replace_contractions(document)
# words = nltk.word_tokenize(document)
# words = normalize(words)
# print("Documents done: ", documentsDoneCount)
# documentsDoneCount += 1
# stems = convert_unicode_to_string(stem_words(words))
# c = Counter(stems)
# pairList = []
# for word, count in c.items():
#     if(word):
#         pairList.append(word + ':' + str(count))

for line in sys.stdin:
    line = line.strip()
    splitLine = line.split('\t', 2)
    document = splitLine[1]
    classes = splitLine[0]
    classes = classes.strip()
    classes = classes.split(',')
    document = denoise_text(document)
    # words = nltk.word_tokenize(document)
    words = document.split()
    words = to_lowercase(words)
    for myword in words:
        for myclass in classes:
            print '%s,%s\t%s' % (myword, myclass, 1)
