from urllib.request import urlopen

url = "http://www.gutenberg.org/files/2554/2554-0.txt"
raw = urlopen(url).read()

print(type(raw))

print(len(raw))

print(raw[:90])

# '\xef\xbb\xbf' is the UTF8 encoded version of the unicode
# ZERO WIDTH NO-BREAK SPACE U+FEFF. It is often used as a
# Byte Order Mark at the beginning of unicode text files
#
# 3 bytes: '\xef\xbb\xbf', then the file is utf8 encoded
