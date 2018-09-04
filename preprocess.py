import re
import sys
import nltk
import contractions
import inflect
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer

# reference: https://www.kdnuggets.com/2018/03/text-data-preprocessing-walkthrough-python.html
# takes as input the data file and creates 2 files
# 1st contains preprocessed word list for each document
# 2nd contains class(es) of each document

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

FIRST_LINE_INDEX = 0

def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

def remove_unicode(text):   #replace unicode codes like \uxxxx with space
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

def lemmatize_verbs(words):
    """Lemmatize verbs in list of tokenized words"""
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas

def normalize(words):
    words = to_lowercase(words)
    words = remove_stopwords(words)
    return words

def convert_unicode_to_string(words):
    new_words = []
    for word in words:
        new_words.append(word.encode('ascii','ignore'))
    return new_words

f = open("data/DBPedia.full.hdfs/full_test.txt")
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
original = documents[0]

sample = original
sample = denoise_text(sample)
sample = replace_contractions(sample)
print (original)
words = nltk.word_tokenize(sample)
words = normalize(words)



stems = convert_unicode_to_string(stem_words(words))
# lemmas = convert_unicode_to_string(lemmatize_verbs(words))
print('Stemmed:', stems)
print(len(stems))
# print('Lemmatized:', lemmas)


totalWordCount = 0
count = 1
f = open("data/document-words.txt", "w")
for document in documents:
    document = denoise_text(document)
    document = replace_contractions(document)
    words = nltk.word_tokenize(document)
    words = normalize(words)
    print("Documents done: ", count)
    count += 1
    stems = convert_unicode_to_string(stem_words(words))
    wordList = ','.join(stems)
    f.write(wordList)
    f.write("\n")
    totalWordCount += len(stems)
print('Total word count: ', totalWordCount)
