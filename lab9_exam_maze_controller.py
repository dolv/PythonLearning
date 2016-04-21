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
        print_maze(self.__maze, self.__x, self.__y)
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

    direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
    posibleMoves = ('forward','left','right')
    class Step(object):
        def __init__(self):
            self.row = 0
            self.col = 0
            self.rotations = [0,1,2,3]
            random.shuffle(self.rotations)
            self.moves = list(posibleMoves)
            self.vector = 0
            self.move=''

    def can_go(candidate):

        if candidate.move == 'forward':
            if runner.go():
                candidate.row += direction[candidate.vector][0]
                candidate.col += direction[candidate.vector][1]
            else:
                return False
        elif candidate.move == 'left':
            runner.turn_left()
            candidate.vector = (candidate.vector - 1) % 4
            if runner.go():
                candidate.row += direction[candidate.vector][0]
                candidate.col += direction[candidate.vector][1]
            else:
                runner.turn_right()
                candidate.vector = (candidate.vector + 1) % 4
                return False
        elif candidate.move == 'right':
            runner.turn_right()
            candidate.vector = (candidate.vector + 1) % 4
            if runner.go():
                candidate.row += direction[candidate.vector][0]
                candidate.col += direction[candidate.vector][1]
            else:
                runner.turn_left()
                candidate.vector = (candidate.vector - 1) % 4
                return False

        if len(steps)>0:
            for i in range(len(steps)-1, -1, -1):
                if steps[i].row == candidate.row and \
                   steps[i].col == candidate.col and \
                   steps[i].vector == candidate.vector:
                    runner.turn_left()
                    runner.turn_left()
                    candidate.vector = (candidate.vector - 2) % 4
                    runner.go()
                    return False

        return True

    steps = []
    index = 0

    while not runner.found():
        if index == len(steps):
            next_step = Step()
            if index > 0:
                next_step.row = steps[index-1].row
                next_step.col = steps[index-1].col
                next_step.vektor = steps[index - 1].vector
        else:
            next_step = steps.pop()
        while len(next_step.moves) > 0:
            next_step.move = next_step.moves.pop()
            if can_go(next_step):
                steps.append(next_step)
                index += 1
                break
        else:
            if index > 0:
                index -= 1

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



