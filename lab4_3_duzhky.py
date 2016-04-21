import sys

inputString = sys.argv[1]
count = 0

for char in inputString:
    if char == "(":
        count += 1
    if char == ")":
        count -= 1
    if count < 0:
        break
print(["NO", "YES"][count == 0])
