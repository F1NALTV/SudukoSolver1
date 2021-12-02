# 11/25/21
# Jordan Schmidt
# Sudoku Solver
# Sudoku consists of 9 grids comprised of 9 tiles all in a 3x3 pattern. Each Grid must have the numbers 1-9
# (one in each tile) Each row and column must also contain the numbers 1-9.

# to make the sudoku board I'm debating either using a nested list to break numbers into their respective grids or
# just listing all 81 numbers in a list. I also need to decide how I want to represent blanks on a board.
# if I mark a blank with an 'X' it might have to do string processing if i mark with a 0 it might place the
# 0 on the board later when I take it into tkinter
# to represent the board I will use a list consisting of 9 lists each of those with a set length of 9.
# when representing the board with a lol i run into a problem trying to pull rows and columns i could predefine each
# row and column like row0 = x[0][0],x[0][1]... it just seems labour intensive. not sure how to get around it tho
# I could make a function that breaks a board (9x9) into 9 rows of 9 and 9 columns of 9
# maybe make a board class that houses the board, 9 rows and 9 columns. i wouldn't need to house grids because of the
# way I created the "board" (each sub list is a grid).
# it might be easier to write each sub list as a row not grid bc pulling columns will be alot easier.
# i am going to switch it up.


# each board consists of a list of 9 other lists. Each sub-list represents a row on the suduko board this set up allows
# me to pull columns by having the same index for column and just incrementing the row
board1 = [[9, 'X', 4, 'X', 'X', 'X', 6, 'X', 'X'],  # 0
          ['X', 'X', 'X', 9, 'X', 'X', 'X', 7, 'X'],  # 1
          [5, 6, 'X', 'X', 4, 3, 'X', 'X', 'X', ],  # 2
          [1, 7, 5, 6, 'X', 4, 2, 'X', 9],  # 3
          ['X', 3, 'X', 'X', 'X', 'X', 7, 'X', 8],  # 4
          [4, 'X', 8, 3, 7, 2, 1, 'X', 6],  # 5
          ['X', 'X', 1, 'X', 9, 7, 'X', 6, 'X', ],  # 6
          ['X', 'X', 'X', 4, 'X', 8, 3, 1, 'X'],  # 7
          ['X', 5, 'X', 'X', 'X', 'X', 4, 'X', 'X']]  # 8


board2 = [['X', 'X', 4, 'X', 'X', 'X', 6, 'X', 'X'],  # 0
          ['X', 'X', 'X', 9, 'X', 'X', 'X', 7, 'X'],  # 1
          [5, 6, 'X', 'X', 4, 3, 'X', 'X', 'X', ],  # 2
          [1, 7, 5, 6, 'X', 4, 2, 'X', 9],  # 3
          ['X', 3, 'X', 'X', 'X', 'X', 7, 'X', 8],  # 4
          [4, 'X', 8, 3, 7, 2, 1, 'X', 6],  # 5
          ['X', 'X', 1, 'X', 9, 7, 'X', 6, 'X', ],  # 6
          ['X', 'X', 'X', 4, 'X', 8, 3, 1, 'X'],  # 7
          ['X', 5, 'X', 'X', 'X', 'X', 4, 'X', 'X']]  # 8


badboard = [[8, 3, 1, 6, 'X', 'X', 5, 'X', 'X'],
            ['X', 4, 9, 5, 'X', 1, 8, 2, 7],
            [2, 5, 'X', 9, 'X', 'X', 'X', 'X', 3],
            ['X', 5, 7, 3, 'X', 'X', 'X', 8, 4],
            [4, 'X', 'X', 'X', 'X', 'X', 'X', 3],
            ['X', 'X', 'X', 7, 4, 5, 1, 'X', 'X'],
            ['X', 6, 'X', 4, 'X', 'X', 9, 2, 'X'],
            [1, 'X', 'X', 9, 'X', 'X', 3, 'X', 'X'],
            ['X', 2, 'X', 'X', 'X', 'X', 5, 6, 1]]


# Checks to see if board consists of a list of 9 other lists all with a length of 9
# returns true if correct board false if wrong board
# lol -> Boolean
def checkBoard(lol):
    j = 0
    for x in lol:
        if len(x) == 9:
            j = j + 1
    if j == 9:
        print("Correct input")
        return True
    else:
        print("Incorrect input")
        return False

# checks whether or not a number is in a list this function can be used to see if a number is in a row or column IF
# the column has been created


def checkList(num, l):
    if num in l:
        return True
    else:
        return False


# makes 1 column that you specify from rows by incrementing the row by 1 with each loop
def makeCol(col, board):
    column = []
    row = -1
    for x in board:
        row = row + 1
        column.append(board[row][col])
    return column


# I think this is a useless function but its here anyway
def makeRow(row, board):
    return board[row]


# this function will Create a specified grid from a board this could probably be shortened but this works
# somehow this does work not sure how or why bc the gridHelp function looks wrong but returns the right values
def makeGrid(gridN, board):
    if gridN == 0:
        return gridHelp(-1, -1, board)

    elif gridN == 1:
        return gridHelp(-1, 2, board)

    elif gridN == 2:
        return gridHelp(-1, 5, board)

    elif gridN == 3:
        return gridHelp(2, -1, board)

    elif gridN == 4:
        return gridHelp(2, 2, board)

    elif gridN == 5:
        return gridHelp(2, 5, board)

    elif gridN == 6:
        return gridHelp(5, -1, board)

    elif gridN == 7:
        return gridHelp(5, 2, board)

    elif gridN == 8:
        return gridHelp(5, 5, board)

# does this work? why is row1 here?
# this works idk why it works but it does
# it really doesn't look like it should and i don't remember writing it but it works

def gridHelp(row, col, board):
    grid = []
    row1 = row
    col1 = col
    for y in range(3):
        row = row + 1
        col = col1
        for x in range(3):
            col = col + 1
            grid.append(board[row][col])
    return grid


def findGrid(posX, posY):
    gridN = int
    if (posY < 3) and (posX < 3):
        gridN = 0
    elif (3 <= posY < 6) and (posX < 3):
        gridN = 1
    elif (posY >= 6) and (posX < 3):
        gridN = 2
    elif (posY < 3) and (3 <= posX < 6):
        gridN = 3
    elif (3 <= posY < 6) and (3 <= posX < 6):
        gridN = 4
    elif (posY >= 6) and (3 <= posX < 6):
        gridN = 5
    elif (posY < 3) and (posX >= 6):
        gridN = 6
    elif (3 <= posY < 6) and (posX >= 6):
        gridN = 7
    else:
        gridN = 8
    return gridN


# so everything works i think i have functions to get rows columns and grids based on numbers 0-8
# now for the hard part creating an algorithm i thought this was easy but its more complex now that im trying to write
# it out my options are either to have each tile have a list of numbers that it could be and when that list is at 1 it
# places the remaining number and updates and affected tiles. this would scale into killer suduko as well.
# instead of having a solid list for each tile I could calculate if there is only one option for it I like the option
# for storing the possible numbers as it resembles pencil marking for traditional suduko and I think would help solve
# problems later down the line

# tile score will determine how many numbers can fit into a certain tilefefefefe


class Board:
    def __init__(self, board):
        self.board = board


testBoard = Board(board1)


# A tile contains a score and a possible list of numbers
class Tile:
    def __init__(self, score=9, posN=[1, 2, 3, 4, 5, 6, 7, 8, 9], posX=0, posY=0, full=False):
        self.score = score
        self.posN = posN
        self.posX = posX
        self.posY = posY
        self.full = full


def createTiles(board):
    newBoard = []
    numX = -1
    for x in board:
        numX = numX + 1
        numY = -1
        row = []
        for y in x:
            numY = numY + 1
            name = "A" + str(numX) + str(numY)
            name = Tile()
            name.posX = numX
            name.posY = numY
            # print("Tile Name" + str(name) + "PosX = " + str(name.posX) + " PosY = " + str(name.posY))
            if isinstance(y,int):
                name.full = True
                name.score = 0
                name.posN = None
            row.append(name)
        newBoard.append(row)
    return newBoard





def numElim(posN, l):
    nums = list(posN)
    for x in range(9):
        num = x + 1
        if checkList(num, l):
            if num in nums:
                nums.remove(num)
    return nums


def tileElim(Tile, board):
    posN = list(Tile.posN)
    posN = numElim(posN, board[Tile.posX])
    col = makeCol(Tile.posY, board)
    posN = numElim(posN, col)
    gridN = findGrid(Tile.posX, Tile.posY)
    grid = makeGrid(gridN, board)
    posN = numElim(posN, grid)
    return posN


def tileScore(lon):
    return len(lon) + 1




def Solve(board):
    tempBoard = board
    counter = 0
    # first we prepare the board

    # now we cycle through the board one tile at a time trying to eliminate numbers from possible
    while checkSolve(tempBoard):
        tileBoard = createTiles(tempBoard)
        for x in tileBoard:
            for y in x:
                if y.full == True:
                    print(str(y.posX), str(y.posY) + " already full")
                else:
                    nums = y.posN
                    nums = tileElim(y,tempBoard)
                    print(str(y.posX), str(y.posY) + " " + str(nums))
                    if len(nums) == 1:
                        print("nums" + str(nums))
                        tempBoard[y.posX][y.posY] = nums[0]
                        print("pasting number " + str(nums[0]))
                    y.full = True
        counter = counter + 1
        print("board # ", str(counter), tempBoard)
    return tempBoard

def checkSolve(board):
    for x in board:
        for y in x:
            if y == 'X':
                return False
            else:
                return True


print(Solve(board1))