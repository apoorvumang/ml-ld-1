#!/usr/bin/python
import re
import sys
from collections import Counter

def remove_till_first_quote(text):
    regex = r"^(.*?)\""
    text = re.sub(regex, '', text)
    return text

def remove_unicode(text):
    """Replace unicode codes like \uxxxx with space"""
    regex = r"(\\u....)"
    text = re.sub(regex, ' ', text)
    return text

def denoise_text(text):
    text = remove_till_first_quote(text)
    text = remove_unicode(text)
    text = remove_punctuation(text)
    return text

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


for line in sys.stdin:
    line = line.strip()
    splitLine = line.split('\t', 2)
    document = splitLine[1]
    classes = splitLine[0]
    classes = classes.strip()
    classes = classes.split(',')
    document = denoise_text(document)
    words = document.split()
    words = to_lowercase(words)
    for myword in words:
        for myclass in classes:
            print '%s,%s\t%s' % (myword, myclass, 1)
