import sys
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
coded = str(sys.argv[1]).replace(" ","")
if len(coded)%5 > 0:
    coded = coded[:-(len(coded)%5)]
decoded = ''
result = ''
for char in coded:
    if char.isupper():
        decoded += 'b'
    else:
        decoded += 'a'
for i in range(0,len(decoded)/5):
    later = decoded[i*5:i*5+5]
    result += alphabet[key.find(later)]
print result
