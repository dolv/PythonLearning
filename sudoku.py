import random
numbers = [1,2,3,4,5,6,7,8,9]

def makeBoard():
    board = None
    while board is None:
        board = attemptBoard()
    return board

def attemptBoard():
    board = [[None for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            checking = numbers[:]
            random.shuffle(checking)
            x = -1
            loopStart = 0
            while board[i][j] is None:
                x += 1
                if x == 9:
                    #No number is valid in this cell, start over
                    return None
                checkMe = [checking[x],True]
                if checkMe in board[i]:
                    #If it's already in this row
                    continue
                checkis = False
                for checkRow in board:
                    if checkRow[j] == checkMe:
                        #If it's already in this column
                        checkis = True
                if checkis: continue
                #Check if the number is elsewhere in this 3x3 grid based on where this is in the 3x3 grid
                if i % 3 == 1:
                    if   j % 3 == 0 and checkMe in (board[i-1][j+1],board[i-1][j+2]): continue
                    elif j % 3 == 1 and checkMe in (board[i-1][j-1],board[i-1][j+1]): continue
                    elif j % 3 == 2 and checkMe in (board[i-1][j-1],board[i-1][j-2]): continue
                elif i % 3 == 2:
                    if   j % 3 == 0 and checkMe in (board[i-1][j+1],board[i-1][j+2],board[i-2][j+1],board[i-2][j+2]): continue
                    elif j % 3 == 1 and checkMe in (board[i-1][j-1],board[i-1][j+1],board[i-2][j-1],board[i-2][j+1]): continue
                    elif j % 3 == 2 and checkMe in (board[i-1][j-1],board[i-1][j-2],board[i-2][j-1],board[i-2][j-2]): continue
                #If we've reached here, the number is valid.
                board[i][j] = checkMe
    return board


def printBoard(board):
    spacer = "++---+---+---++---+---+---++---+---+---++"
    print (spacer.replace('-','='))
    for i,line in enumerate(board):
        print ("|| {} | {} | {} || {} | {} | {} || {} | {} | {} ||"
               .format(*(cell[0] or ' ' for cell in line)))
        if (i+1) % 3 == 0: print(spacer.replace('-','='))
        else: print(spacer)

printBoard(makeBoard())