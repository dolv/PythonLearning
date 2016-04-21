import sys
inputString = ""
for i in range(len(sys.argv)-1):
    inputString += " " + sys.argv[len(sys.argv)-1-i]
print inputString[1:]
