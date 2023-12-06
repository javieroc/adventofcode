"""
example on the left: [1, 3, 0, 2]
example on the right: [2, 0, 3, 1]
"""
def is_valid_state(state, n):
    # check if it is a valid solution
    return len(state) == n

def get_candidates(state, n):
    if not state:
        return range(n)

    # find the next position in the state to populate
    position = len(state)
    candidates = set(range(n))
    # prune down candidates that place the queen into attacks
    for row, col in enumerate(state):
        # discard the column index if it's occupied by a queen
        candidates.discard(col)
        dist = position - row
        # discard diagonals
        candidates.discard(col + dist)
        candidates.discard(col - dist)

    print(f"state: {state} - candidates: {candidates}")
    return candidates

def search(state, solutions, n):
    if is_valid_state(state, n):
        state_string = state_to_string(state, n)
        print(state_string)
        solutions.append(state_string)
        return

    candidates = get_candidates(state, n)
    # print(f"candidates {candidates}")
    for candidate in candidates:
        # recurse
        state.append(candidate)
        search(state, solutions, n)
        state.pop()

def state_to_string(state, n):
    # ex. [1, 3, 0, 2]
    # output: [".Q..","...Q","Q...","..Q."]
    ret = []
    for i in state:
        string = '.' * i + 'Q' + '.' * (n - i - 1)
        ret.append(string)
    return ret


def solveNQueens(n: int) -> list[list[str]]:
    solutions = []
    state = []
    search(state, solutions, n)
    print(solutions)
    return solutions


solveNQueens(4)
