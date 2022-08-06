import sys

file_name = sys.argv[0]
file = open(file_name)

for line in file.read()[::-1]:
    print(line, end= '')
