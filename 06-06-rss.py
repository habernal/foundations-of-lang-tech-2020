import feedparser
from bs4 import BeautifulSoup
from nltk import word_tokenize

lang_log = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
print(lang_log['feed']['title'])
print(len(lang_log.entries))

post = lang_log.entries[2]
print(post.title)

content = post.content[0].value
print(content[:70])

raw = BeautifulSoup(content, 'html.parser').get_text()
print(word_tokenize(raw)[:20])
