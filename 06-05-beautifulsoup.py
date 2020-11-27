from urllib.request import urlopen

import nltk
from bs4 import BeautifulSoup

raw_html = urlopen('https://www.tu-darmstadt.de/universitaet/index.en.jsp').read()

text = BeautifulSoup(raw_html, features='html5lib').get_text()

tokens = nltk.word_tokenize(text)
print(tokens[:150])
