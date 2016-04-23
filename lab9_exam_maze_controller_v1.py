import random

def print_maze(maze,x,y):
    for i in range(len(maze)):
        s = ''
        for j in range(len(maze)):
            if i == x and j == y:
                s += 'X'
            elif maze[i][j] == 1:
                s += '1'
            else:
                s += '.'
        print s
    print ' '

class MazeRunner(object):

    def __init__(self, maze, start, finish):
        self.__maze = maze
        self.__rotation = (1,0)
        self.__x = start[0]
        self.__y = start[1]
        self.__finish = finish

    def go(self):
        x = self.__x + self.__rotation[0]
        y = self.__y + self.__rotation[1]
        if x > len(self.__maze)-1 \
            or y > len(self.__maze)-1 \
            or x < 0 or y < 0 \
            or self.__maze[x][y] == 1:
            return False
        self.__x = x
        self.__y = y
        # print_maze(self.__maze, self.__x, self.__y)
        return True

    def turn_left(self):
        left_rotation = {
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1),
        }
        self.__rotation = left_rotation[self.__rotation]
        return self

    def turn_right(self):
        right_rotation = {
            (1, 0): (0, 1),
            (0, -1): (1, 0),
            (-1, 0): (0, -1),
            (0, 1): (-1, 0),
        }
        self.__rotation = right_rotation[self.__rotation]
        return self

    def found(self):
        return self.__x == self.__finish[0] and self.__y == self.__finish[1]



def maze_controller(runner):

    # direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
    CardinalDirections = ('South', 'East', 'North', 'West')
    way = {
        'South': (1, 0),
        'East': (0, 1),
        'North': (-1, 0),
        'West': (0,-1)
    }

    class Step(object):
        def __init__(self):
            self.row = 0
            self.col = 0
            self.usedways = []
            self.moves = list(CardinalDirections)
            random.shuffle(self.moves)
            self.vector = 0
            self.move=''

    def print_way(size, x, y, print_coordinates = 0):
        matrix =[]
        for i in range(size):
            line = []
            for j in range(size):
                if not print_coordinates:
                    line.append('.')
                else:
                    line.append(('.','.'))
            matrix.append(line)

        for step in steps:
            rr = y + step.row
            cc = x + step.col
            if not print_coordinates:
                matrix[rr][cc] = str(step.move[0])
            elif print_coordinates == 1:
                matrix[rr][cc] = (str(step.row),str(step.col))
            else:
                matrix[rr][cc] = (str(rr), str(cc))
        if not print_coordinates:
            matrix[y][x] = "X"
        else:
            matrix[y][x] = ("X","Y")

        for i in range(size):
            print matrix[i]
        print

    def rotateToNewDirection():
        while CardinalDirections[next_step.vector] != next_step.move:
            runner.turn_left()
            next_step.vector = (next_step.vector - 1) % 4


    def can_go(candidate):
        if not runner.go():
            return False

        if len(steps)>0:
            for i in steps:
                if i.row == candidate.row and \
                   i.col == candidate.col:
                    for used_way in i.usedways:
                        if used_way == candidate.move:
                            runner.turn_left()
                            runner.turn_left()
                            runner.go()
                            runner.turn_right()
                            runner.turn_right()
                            return False
        candidate.row += way[CardinalDirections[candidate.vector]][0]
        candidate.col += way[CardinalDirections[candidate.vector]][1]
        return True

    steps = []
    index = 0
    while not runner.found():
        if index == len(steps):
            next_step = Step()
            if index > 0:
                next_step.row = steps[index-1].row
                next_step.col = steps[index-1].col
                next_step.vector = steps[index - 1].vector
                next_step.move = CardinalDirections[next_step.vector]
                next_step.moves.remove(next_step.move)
        else:
            next_step = steps.pop()
        newstep = True
        while len(next_step.moves) > 0:
            if not newstep or index == 0:
                next_step.move = next_step.moves.pop()
            newstep = False
            rotateToNewDirection()
            if can_go(next_step):
                steps.append(next_step)
                index += 1
                break
            else:
                next_step.usedways.append(next_step.move)
        else:
            if index > 0:
                index -= 1
    # print index

maze_example1 = {
    'm': [
        [0,1,0,0,0],
        [0,1,1,1,1],
        [0,0,0,0,0],
        [1,1,1,1,0],
        [0,0,0,1,0],
    ],
    's': (0,0),
    'f': (4,4)
}

maze_runner = MazeRunner(maze_example1['m'], maze_example1['s'], maze_example1['f'])
maze_controller(maze_runner)
print maze_runner.found()


maze_example2 = {
    'm': [
        [0,0,0,0,0,0,0,1],
        [0,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0],
        [1,1,1,1,0,1,0,1],
        [0,0,0,0,0,1,0,1],
        [0,1,0,1,1,1,1,1],
        [1,1,0,0,0,0,0,0],
        [0,0,0,1,1,1,1,0],
    ],
    's': (7,7),
    'f': (0,0)
}

maze_runner = MazeRunner(maze_example2['m'], maze_example2['s'], maze_example2['f'])
maze_controller(maze_runner)
print maze_runner.found()


maze_example3 = {
    'm': [
        [0,0,0,0,0,0,0,0,0,0,0],
        [1,0,1,1,1,0,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,1,1,0,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
    ],
    's': (0,5),
    'f': (10,5)
}
maze_runner = MazeRunner(maze_example3['m'], maze_example3['s'], maze_example3['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True

maze_example4 = {
    'm': [
        [0,0,0,0,1,0,1,0,0,0,0],
        [0,1,1,1,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [1,1,0,1,0,0,0,1,0,1,1],
        [0,1,0,1,0,1,0,1,0,1,0],
        [0,1,0,0,0,1,0,0,0,1,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,1,1,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
    ],
    's': (0,5),
    'f': (4,5)
}
maze_runner = MazeRunner(maze_example4['m'], maze_example4['s'], maze_example4['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True

maze_example5 = {
    'm': [
        [0,0,0,1,1,0,1,1,0,0,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,1,1,0,0,0,1,1,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,1,0,1,0,1,0,1,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,1,1,1,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,1,0,1,0,1,0,0],
    ],
    's': (0,5),
    'f': (4,5)
}
maze_runner = MazeRunner(maze_example5['m'], maze_example5['s'], maze_example5['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True