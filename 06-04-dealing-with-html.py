from urllib.request import urlopen

raw_html = urlopen('https://www.wikipedia.org/').read()
print(len(raw_html))

print(raw_html[:40])

html = raw_html.decode('utf-8')
print(html[:40])
