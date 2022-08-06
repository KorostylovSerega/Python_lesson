import sys

name = sys.argv[0]
text = open(name)
print(text.read()[::-1])

text.close()
