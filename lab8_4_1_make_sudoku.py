import time
import random
from print_table_unicode import print_matrix


class Cell:
    def __init__(self, index, size):
        self.regionWidth = size
        self.availableNumbers = []
        self.replenish()
        self.index = index
        self.value = 0
        self.region = (index / self.regionWidth ** 3) * self.regionWidth \
                      + (index % self.regionWidth ** 2) / self.regionWidth
        self.reg_row = index / self.regionWidth
        self.reg_col = index % self.regionWidth
        self.row = index / (self.regionWidth ** 2)
        self.col = index % (self.regionWidth ** 2)

    def replenish(self):
        self.availableNumbers = range(1, self.regionWidth ** 2 + 1)
        random.shuffle(self.availableNumbers)


class Grid:
    def __init__(self, size):
        self.blockSize = size
        self.width = self.blockSize ** 2
        self.totalCellsQuantity = self.width ** 2
        self.Cells = []

    def populate(self):
        count = 0
        candidateIndex = 0
        while len(self.Cells) < self.totalCellsQuantity:
            if candidateIndex == len(self.Cells):
                candidate = Cell(candidateIndex, self.blockSize)
            else:
                candidate = self.Cells.pop()
            while len(candidate.availableNumbers) > 0:
                candidate.value = candidate.availableNumbers.pop()
                count += 1
                if not self.conflicts(candidate):
                    self.Cells.append(candidate)
                    candidateIndex += 1
                    break
            else:
                candidateIndex -= 1


    def conflicts(self, tested):
        for cell in self.Cells:
            if (cell.row == tested.row \
                    or cell.col == tested.col \
                    or cell.region == tested.region
                ):
                if cell.value == tested.value:
                    return True
        return False

    def get_grid_cells_values_matrix(self):
        valueMatrix = []
        line = []
        ind = 0
        while ind < self.totalCellsQuantity:
            if ind < len(self.Cells):
                line.append(self.Cells[ind].value)
            else:
                line.append(0)
            if len(line) == self.width:
                valueMatrix.append(line)
                line = []
            ind += 1
        return valueMatrix

    def get_CellWithIndex(self, index):
        for cell in self.Cells:
            if cell.index == index:
                return cell
        return False

    def get_grid_cells_values_list(self):
        return [cell.value for cell in self.Cells]

    def get_grid_cells_index_list(self):
        return [cell.index for cell in self.Cells]

    def del_CellWithIndex(self, index):
        for cell in self.Cells:
            if cell.index == index:
                self.Cells.remove(cell)

    def get_Cells_regions(self):
        return [cell.region for cell in self.Cells]

    def get_Cells_rows(self):
        return [cell.row for cell in self.Cells]

    def get_Cells_cols(self):
        return [cell.col for cell in self.Cells]

def make_sudoku(size):
    table = Grid(size)
    table.populate()
    return table.get_grid_cells_values_matrix()


# s = time.time()
# matrix =  make_sudoku(1) # [[1]]
# print "elapsed = ", time.time() - s, ";", matrix
# print_matrix(matrix)
#
# s = time.time()
# matrix = make_sudoku(2) # [[1,2,3,4],[3,4,1,2],[2,1,4,3],[4,3,2,1]]
# print "elapsed = ", time.time() - s, ";", matrix
# print_matrix(matrix)

startAt = time.time()
bs = 4
matrix = make_sudoku(bs)  # [[3,5,8,1,2,7,6,4,9],[6,7,4,5,8,9,3,2,1],[2,1,9,3,4,6,5,7,8],[9,8,6,7,1,4,2,5,3],[4,3,1,2,6,5,8,9,7],[7,2,5,9,3,8,1,6,4],[1,6,3,4,7,2,9,8,5],[8,9,7,6,5,1,4,3,2],[5,4,2,8,9,3,7,1,6]]
print "elapsed = ", time.time() - startAt, ";", matrix
print_matrix(matrix, bs)
