from urllib.request import urlopen

raw_html = urlopen('https://en.wikipedia.org/wiki/Python').read()
print(len(raw_html))

print(raw_html[:400])

html = raw_html.decode('utf-8')
print(html[:400])
