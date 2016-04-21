import time
import random
import math

def make_sudoku(size):
    sudoku = []
    def conflicts(tested, index):
        i = -1
        tested_row = index / size ** 2
        tested_col = index % size ** 2
        tested_region = (index / size ** 3) * size + (index % size ** 2) / size

        for cell in sudoku:
            i += 1
            cell_row = i / size ** 2
            if cell_row == tested_row:
                if cell[0] == tested[0]:
                    return True

            cell_col = i % size ** 2
            if cell_col == tested_col:
                if cell[0] == tested[0]:
                    return True

            cell_region = (i / size ** 3) * size + (i % size ** 2) / size
            if cell_region == tested_region:
                if cell[0] == tested[0]:
                    return True

        return False

    def get_matrix():
        line = []
        matrix = []
        for i in range(size**4):
            if i < len(sudoku):
                line.append(sudoku[i][0])
            else:
                line.append(0)
            if len(line) == size ** 2:
                matrix.append(line)
                line = []
        return matrix

    index = 0
    while len(sudoku) < size**4:
        if index == len(sudoku):
            candidate = [0,[num+1 for num in range(size ** 2)]]
            # random.shuffle(candidate[1])
        else:
            candidate = sudoku.pop()
        while len(candidate[1]) > 0:
            candidate[0] = candidate[1].pop()
            if not conflicts(candidate, index):
                sudoku.append(candidate)
                index += 1
                break
        else:
            index -= 1

    return get_matrix()

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

# startAt = time.time()
# matrix = make_sudoku(1)
# print "elapsed = ", time.time() - startAt
# print matrix
#
# startAt = time.time()
# matrix = make_sudoku(2)
# print "elapsed = ", time.time() - startAt
# print matrix

startAt = time.time()
matrix = make_sudoku(5)
print "elapsed = ", time.time() - startAt
print matrix
print check_sudoku(matrix)
