import sys

inputString = sys.argv[1].lower().replace(" ", "")
l = int(len(inputString)) - 1
is_palindrome = True

for i in range(int(l/2)):
    if inputString[i] != inputString[l - i]:
        is_palindrome = False
        break
print(["NO", "YES"][is_palindrome])
