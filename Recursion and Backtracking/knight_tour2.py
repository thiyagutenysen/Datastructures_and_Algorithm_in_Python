import numpy as np
import itertools


def possible_jumps(x, y):
    jumps = []
    if x+2 <= N-1 and x+2 >= 0:
        if y+1 <= N-1 and y+1 >= 0:
            jumps.append((x+2, y+1))
    if x+1 <= N-1 and x+1 >= 0:
        if y+2 <= N-1 and y+2 >= 0:
            jumps.append((x+1, y+2))
    if x-1 <= N-1 and x-1 >= 0:
        if y+2 <= N-1 and y+2 >= 0:
            jumps.append((x-1, y+2))
    if x-2 <= N-1 and x-2 >= 0:
        if y+1 <= N-1 and y+1 >= 0:
            jumps.append((x-2, y+1))
    if x-2 <= N-1 and x-2 >= 0:
        if y-1 <= N-1 and y-1 >= 0:
            jumps.append((x-2, y-1))
    if x-1 <= N-1 and x-1 >= 0:
        if y-2 <= N-1 and y-2 >= 0:
            jumps.append((x-1, y-2))
    if x+1 <= N-1 and x+1 >= 0:
        if y-2 <= N-1 and y-2 >= 0:
            jumps.append((x+1, y-2))
    if x+2 <= N-1 and x+2 >= 0:
        if y-1 <= N-1 and y-1 >= 0:
            jumps.append((x+2, y-1))
    return jumps


N = 5
board = np.zeros((N, N))
x = 0
y = 0


def complete(board):
    for i in range(N):
        for j in range(N):
            if board[i, j] == 0:
                return False
    else:
        return True


iterator = itertools.count(start=1, step=1)
move_count = 1


def tour(board, x, y, move_count):
    if board[x][y] == 0:
        board[x, y] = move_count
        move_count += 1
        if complete(board.copy()):
            print(" Tour is complete ")
            print(" solution number = ", next(iterator))
            print(board)
            return
        else:
            next_moves = possible_jumps(x, y)
            for next_move in next_moves:
                tour(board.copy(), next_move[0], next_move[1], move_count)
            return
    else:
        return


tour(board, x, y, move_count)
