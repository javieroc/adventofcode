from itertools import product

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

SHAPE = 9
GRID = 3
EMPTY = '.'
DIGITS = set([str(num) for num in range(1, SHAPE + 1)])

def is_valid_state(board):
    # check if it is a valid solution
    # validate all the rows
    for row in get_rows(board):
        if not set(row) == DIGITS:
            return False
    # validate columns
    for col in get_cols(board):
        if not set(col) == DIGITS:
            return False
    # validate sub-boxes
    for grid in get_grids(board):
        if not set(grid) == DIGITS:
            return False
    return True

def get_candidates(board, row, col):
    used_digits = set()
    # remove digits used by the same row
    used_digits.update(get_kth_row(board, row))
    # remove digits used by the same column
    used_digits.update(get_kth_col(board, col))
    # remove digits used by the 3x3 sub-box
    used_digits.update(get_grid_at_row_col(board, row, col))
    used_digits -= set([EMPTY])
    candidates = DIGITS - used_digits
    return candidates

def search(board):
    if is_valid_state(board):
        return True # found solution

    # find the next empty spot and take a guess
    for row_idx, row in enumerate(board):
        for col_idx, elm in enumerate(row):
            if elm == EMPTY:
                # find candidates to construct the next state
                for candidate in get_candidates(board, row_idx, col_idx):
                    board[row_idx][col_idx] = candidate
                    # recurse on the modified board
                    is_solved = search(board)
                    if is_solved:
                        return True
                    else:
                        # undo the wrong guess and start anew
                        board[row_idx][col_idx] = EMPTY
                # exhausted all candidates
                # but none solves the problem
                return False
    # no empty spot
    return True

# helper functions for retrieving rows, cols, and grids
def get_kth_row(board, k):
    return board[k]

def get_rows(board):
    for i in range(SHAPE):
        yield board[i]

def get_kth_col(board, k):
    return [
        board[row][k] for row in range(SHAPE)
    ]

def get_cols(board):
    for col in range(SHAPE):
        ret = [
            board[row][col] for row in range(SHAPE)
        ]
        yield ret

def get_grid_at_row_col(board, row, col):
    row = row // GRID * GRID
    col = col // GRID * GRID
    return [
        board[r][c] for r, c in
        product(range(row, row + GRID), range(col, col + GRID))
    ]

def get_grids(board):
    for row in range(0, SHAPE, GRID):
        for col in range(0, SHAPE, GRID):
            grid = [
                board[r][c] for r, c in
                product(range(row, row + GRID), range(col, col + GRID))
            ]
            yield grid

def solveSudoku(board: list[list[str]]) -> None:
    search(board)
    print(board)


solveSudoku(board)
