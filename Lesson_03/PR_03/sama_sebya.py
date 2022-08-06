import sys
filename = sys.argv[0]
f = open(filename)
for line in f:
    print(line)
f.close()
