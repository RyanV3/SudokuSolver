import tkinter as tk

#sudoku board
sudBoard = [[0,2,0,0,0,4,3,0,0],
            [9,0,0,0,2,0,0,0,8],
            [0,0,0,6,0,9,0,5,0],
            [0,0,0,0,0,0,0,0,1],
            [0,7,2,5,0,3,6,8,0],
            [6,0,0,0,0,0,0,0,0],
            [0,8,0,2,0,5,0,0,0],
            [1,0,0,0,9,0,0,0,3],
            [0,0,9,8,0,0,0,6,0]]

#window setup
window = tk.Tk()
window.geometry("400x400")
window.configure(bg='black')
window.title("Sudoku Solver")
window.resizable(width=False, height=False)


#populates the sudoku grid with frames 
def popBoard():
    for i in range(len(sudBoard)):
        for j in range(len(sudBoard[0])):
            frameij = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1
            )
            if i % 3 == 0:
                frameij.grid(row=i, column=j, pady=(3, 0))
            if j % 3 == 0:
                frameij.grid(row=i, column=j, padx=(3, 0))
            else:    
                frameij.grid(row=i, column=j)
            label = tk.Label(master=frameij, height=2, width=5, text=str(sudBoard[i][j]))
            label.pack()


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
            #label = tk.Label(master=frameij, height=2, width=5, text=str(sudBoard[row][col]))
            #label.pack()
            #popBoard()

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


popBoard()

#handles the button function. when the button is clicked, the board is solved and repopulated with the correct values
def handleClick(event):
    solve(sudBoard)
    popBoard()


#white box at bottom of window that the button sits on
bottomDisplay = tk.Frame(
    master=window,
    width=400,
    height=46,
    bg='white'
)

#solve button
solveButton = tk.Button(
    master=bottomDisplay,
    text="Solve",
    height=2,
    width=8
)

#create bottom frame and button
bottomDisplay.pack_propagate(False)
bottomDisplay.grid(row=10, column=0, columnspan=9, pady=(3, 0))
solveButton.pack()

#bind buttton to click event
solveButton.bind("<Button-1>", handleClick)

#test
    #time.sleep(3)
    #solve(sudBoard)
    #popBoard()
window.mainloop()
