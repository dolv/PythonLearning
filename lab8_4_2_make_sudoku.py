import random
import time
import math

from print_table_unicode import print_matrix

def make_sudoku(size):
    numbers = range(1, size**2+1)
    random.shuffle(numbers)
    matrix = []
    for i in range(size):
        for j in range(size):
            line = numbers[i + j*size:]
            line.extend(numbers[:i + j*size])
            matrix.append(line)
    return matrix

def check_sudoku(l):
    n = len(l)
    if n == 1 and l == [[1]]:
        return True

    for i in xrange(n):
        for j in xrange(n):
            v = l[i][j]
            for t in xrange(j + 1, n):
                if l[i][t] == v:
                    return False
            for t in xrange(i + 1, n):
                if l[t][j] == v:
                    return False

    nn = int(math.sqrt(n))
    for i in xrange(nn):
       for j in xrange(nn):
        t = j * nn
        lt = []
        for x in xrange(nn):
            lt += l[i * nn + x][t : t + nn]
        for i1 in xrange(n):
            for j1 in xrange(i1 + 1, n):
                if lt[i1] == lt[j1]:
                    return False;

    return True

size = 3
startAt = time.time()
m = make_sudoku(size)
finishAt = time.time()
# print_matrix(m, size)
print "elapsed = ", finishAt - startAt
print m
# print check_sudoku(m)