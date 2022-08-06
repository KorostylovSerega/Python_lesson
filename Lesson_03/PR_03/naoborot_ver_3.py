import sys

file_name = sys.argv[0]
file = open(file_name)

lines = file.readlines()
lines.reverse()

for i in lines:
    print(i.rstrip()[::-1])
