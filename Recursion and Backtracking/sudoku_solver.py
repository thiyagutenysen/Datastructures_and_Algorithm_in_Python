import numpy as np


def possible(grid, x, y, n):
    #global grid
    for i in range(9):
        if grid[i][y] == n:
            return False
    for j in range(9):
        if grid[x][j] == n:
            return False
    start_x = (x//3) * 3
    start_y = (y//3) * 3
    for i in range(start_x, start_x+3):
        for j in range(start_y, start_y+3):
            if grid[i][j] == n:
                return False
    return True


def completed(grid):
    #global grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return False
    return True


def sudoku_solver(grid):
    #global grid
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for n in range(1, 10):
                    if possible(grid, row, col, n):
                        grid[row][col] = n
                        if completed(grid):
                            print(grid)
                        sudoku_solver(grid)
                        grid[row][col] = 0
                return


grid = np.array([[0, 0, 9, 7, 0, 0, 0, 0, 8],
                 [0, 0, 3, 0, 0, 2, 1, 0, 0],
                 [8, 0, 0, 0, 6, 5, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0, 0, 8, 0],
                 [0, 0, 0, 0, 0, 7, 0, 5, 6],
                 [0, 0, 0, 6, 0, 9, 0, 0, 0],
                 [0, 6, 0, 0, 2, 0, 3, 0, 0],
                 [0, 0, 5, 4, 3, 8, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1]])
sudoku_solver(grid)
