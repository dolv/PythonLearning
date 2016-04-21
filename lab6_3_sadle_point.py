
def saddle_point(matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == min(matrix[row]) and matrix[row][col] == max(row[col] for row in matrix):
                    point = (row, col)
                    count += 1
    return [False, point][count == 1]

print saddle_point([[13]])
print saddle_point([[0,0,0],[2,1,2],[1,0,1]])
print saddle_point([[1,2,3,0,1,1], [4,3,2,1,1,2], [4,3,2,0,1,1], [0,0,0,0,0,1]])
print saddle_point([[5,5,5], [5,5,6], [5,4,5]])
print saddle_point([[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [11, 10, 9, 8, 7, 6, 5, 4, 3, 2], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3], [13, 12, 11, 10, 9, 8, 7, 6, 5, 4], [14, 13, 12, 11, 10, 9, 8, 7, 6, 5], [15, 14, 13, 12, 11, 10, 9, 8, 7, 6], [16, 15, 14, 13, 12, 11, 10, 9, 8, 7], [17, 16, 15, 14, 13, 12, 11, 10, 9, 8], [18, 17, 16, 15, 14, 13, 12, 11, 10, 9], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10]])