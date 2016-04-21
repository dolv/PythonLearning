# 1.5sec, 22740 combinations
counter = 0
n = 8
print 'v7, recursion bactracking'

def output_desk(p):
    if p == None:
        return
    for i in range(n):
        row = ''
        for j in range(n):
            flag = False
            for ii in range(n):
                if p[ii][0] == i and p[ii][1] == j:
                    flag = True
            row += '1'*int(flag) + '0'*(1-int(flag))
        print row

def is_ok(p):
    global counter
    counter += 1
    for i in range(n):
        for j in range(n):
            if i != j and \
                (p[i][0] == p[j][0] or p[i][1] == p[j][1] \
                or p[i][0]+p[i][1] == p[j][0]+p[j][1] \
                or n-p[i][0]+p[i][1] == n-p[j][0]+p[j][1]):
                return False
    return True

def find_position():
    def try_queen(pos):
        if len(pos) == n:
            if is_ok(pos):
                return pos
            else:
                return False
        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                if pos[i][1] == pos[j][1]:
                    return False
        for current_queen_pos in range(0,n):
            pos_new = pos[:]
            pos_new.append((len(pos), current_queen_pos))
            res = try_queen(pos_new)
            if res:
                return res

    start_position = []
    return try_queen(start_position)

p = find_position()
print counter
print p
output_desk(p)

