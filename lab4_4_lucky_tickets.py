import sys

start = int(sys.argv[1])
stop = int(sys.argv[2])+1
count = 0

for i in range(start, stop):
    i_str = str(i)
    i_len = len(i_str)
    ticket = (6-i_len)*'0'+i_str
    if int(ticket[0]) + int(ticket[1]) + int(ticket[2]) == int(ticket[3]) + int(ticket[4]) + int(ticket[5]):
        count += 1
#        print count, ticket[0] + ticket[1] + ticket[2], ticket[3] + ticket[4] + ticket[5]
print str(count)