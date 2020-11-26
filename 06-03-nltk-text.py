from urllib.request import urlopen

import nltk

tokens = nltk.word_tokenize(urlopen(
    'http://www.gutenberg.org/files/2554/2554-0.txt').read().decode('utf-8-sig'))

text = nltk.Text(tokens)
print(type(text))

print(text[1026:1042])

# make sure we hove stopwords downloaded locally before calling collocations!
nltk.download('stopwords')

print(text.collocations())
