from urllib.request import urlopen

import nltk

url = "http://www.gutenberg.org/files/2554/2554-0.txt"
raw = urlopen(url).read()

# decoded = raw.decode('utf-8')
# This does not remove the ugly UTF-8 BOM '\xef\xbb\xbf'!

# removes BOM if present
decoded = raw.decode('utf-8-sig')
print(decoded[:85])

# first make sure we have the model locally available
nltk.download('punkt')

tokens = nltk.word_tokenize(decoded)

print(type(tokens))

print(len(tokens))

print(tokens[:10])
