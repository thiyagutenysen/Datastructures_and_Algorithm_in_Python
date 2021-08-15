import numpy as np
import itertools

iterator = itertools.count(start=1, step=1)
queen_count = 0
N = 8


def possible(x, y):
    if x >= 0 and x <= N-1:
        if y >= 0 and y <= N-1:
            return True
    return False


def mark_area(grid, x, y, queen_count):
    for i in range(N):
        if grid[x][i] == 0:
            grid[x][i] = -1
        if grid[i][y] == 0:
            grid[i][y] = -1
    for i in range(-(N-1), N-1+1):
        if possible(x+i, y+i):
            if grid[x+i][y+i] == 0:
                grid[x+i][y+i] = -1
        if possible(x+i, y-i):
            if grid[x+i][y-i] == 0:
                grid[x+i][y-i] = -1
    grid[x][y] = queen_count
    return grid


def complete(grid):
    for i in range(N):
        for j in range(N):
            if grid[i][j] == N:
                return True
    return False


def n_queens_solver(grid, queen_count):
    for row in range(N):
        if grid[row][queen_count] == 0:
            temp = grid.copy()
            queen_count += 1
            grid = mark_area(grid, row, queen_count-1, queen_count)
            if complete(grid):
                print("Solution number =", next(iterator))
                print(grid)
                return
            else:
                n_queens_solver(grid, queen_count)
                queen_count -= 1
                grid = temp.copy()
    return


grid = np.zeros((N, N))
n_queens_solver(grid, queen_count)
