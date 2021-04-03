board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0]]


# Function for printing Sudoku Board
# (i , j)  row , col
def print_board():
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# Function for Finding Empty Space
# (i , j)  row , col
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i, j
    return None


# function for checking valid

def check(board, num, pos):
    # check row
    for i in range(len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # check col
    for j in range(len(board)):
        if board[j][pos[1]] == num and pos[0] != j:
            return False

    # check box
    box_i = pos[1] // 3
    box_j = pos[0] // 3

    for i in range(box_j * 3, box_j * 3, +3):
        for j in range(box_i * 3, box_i * 3, +3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


# function for solving
def solver(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    # filling numbers 1-9 after checking using check function
    for i in range(1, 10):
        if check(board, i, (row, col)):
            board[row][col] = i

            # calling solver recursively after filling a no. in the board
            if solver(board):
                return True

            # resetting board position to 0
            # backtracking
            board[row][col] = 0
    return False

