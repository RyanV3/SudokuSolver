#Sudoku Board Solver- 
#solves and completes the specified sudoku board below

#unsolved board
sudBoard = [[0,2,0,0,0,4,3,0,0],
         [9,0,0,0,2,0,0,0,8],
         [0,0,0,6,0,9,0,5,0],
         [0,0,0,0,0,0,0,0,1],
         [0,7,2,5,0,3,6,8,0],
         [6,0,0,0,0,0,0,0,0],
         [0,8,0,2,0,5,0,0,0],
         [1,0,0,0,9,0,0,0,3],
         [0,0,9,8,0,0,0,6,0]]


#solves the sudoku board using backtracking algorithm
def solve(board):

    slot = findEmpty(board)
    if slot:
        row, col = slot
    else:
        return True
    
    for i in range(1,10):
        if valid(board, (row, col), i):
            board[row][col] = i

            if solve(board):
                return True
            
            board[row][col] = 0
    return False


#finds the next empty(0) value 
def findEmpty(board):

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)

    return None


#returns true if the value is in a valid location
def valid(board, position, value): 

    #check down the row
    for i in range(0, len(board)):
        if board[position[0]][i] == value and position[1] != i:
            return False

    #check down the column
    for i in range(0, len(board)):
        if board[i][position[1]] == value and position[1] != i:
            return False
    
    #check in the 3x3 box
    boxCol = position[1]//3
    boxRow = position[0]//3
    for i in range(boxRow*3, boxRow*3 + 3):
        for j in range(boxCol*3, boxCol*3 + 3):
            if board[i][j] == value and (i,j) != position:
                return False

    return True


#prints a sudoku board with a proper format
def printBoard(board):

    for i in range(len(board)):
        if i % 3 == 0:
            print("-------------------------------")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print("|", end="")
            print(" " + str(board[i][j]) + " ", end="")
            if j == 8:
                if i == 8:
                    print("|\n-------------------------------")
                else:
                    print("|")
    
    
print("Unsolved Board - ")
printBoard(sudBoard)

print("Solved Board - ")
solve(sudBoard)
printBoard(sudBoard)

