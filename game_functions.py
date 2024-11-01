

# game_functions.py
import pandas as pd
import random
import numpy as np

def initialize_board():
    board = np.zeros((4,4),dtype = int)
    board = pd.DataFrame(board)
    add_new_two(board)
    add_new_two(board)
    return board

def display_board(board):
    print(board)
    print()

def add_new_two(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board.iloc[i, j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board.iat[i, j] = 2

def compress_and_merge(line):
    non_zero = [num for num in line if num != 0]
    merged = []
    i = 0
    while i < len(non_zero):
        if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
            merged.append(2 * non_zero[i])
            i += 2
        else:
            merged.append(non_zero[i])
            i += 1
    return merged + [0] * (4 - len(merged))

def move_up(board):
    new_board = board.copy()
    for col in range(4):
        new_col = compress_and_merge(board.iloc[:, col].tolist())
        new_board.iloc[:, col] = new_col
    return new_board

def move_down(board):
    new_board = board.copy()
    for col in range(4):
        reversed_col = board.iloc[:, col].tolist()[::-1]
        new_col = compress_and_merge(reversed_col)[::-1]
        new_board.iloc[:, col] = new_col
    return new_board

def move_left(board):
    new_board = board.copy()
    for row in range(4):
        new_row = compress_and_merge(board.iloc[row, :].tolist())
        new_board.iloc[row, :] = new_row
    return new_board

def move_right(board):
    new_board = board.copy()
    for row in range(4):
        reversed_row = board.iloc[row, :].tolist()[::-1]
        new_row = compress_and_merge(reversed_row)[::-1]
        new_board.iloc[row, :] = new_row
    return new_board

def can_move(board, direction):
    temp_board = board.copy()
    if direction == 'w':
        moved_board = move_up(temp_board)
    elif direction == 's':
        moved_board = move_down(temp_board)
    elif direction == 'a':
        moved_board = move_left(temp_board)
    elif direction == 'd':
        moved_board = move_right(temp_board)
    else:
        return False
    return not moved_board.equals(board)

def check_game_over(board):
    if (board == 0).any().any():
        return False
    for i in range(4):
        for j in range(3):
            if board.iat[i, j] == board.iat[i, j + 1] or board.iat[j, i] == board.iat[j + 1, i]:
                return False
    return True
