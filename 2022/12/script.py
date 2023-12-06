board = [[y for y in x.replace('\n', '')] for x in open("input-test.txt").readlines()]
m = len(board)
n = len(board[0])


def is_valid_state(state: list[(int, int)]):
    end = find('E', board)
    return end in state


def get_candidates(state: list[(int, int)]) -> list[(int, int)]:
    adjacent_indices = []
    if (len(state) < 0):
        return []
    (i,j) = state[-1]
    if i > 0:
        adjacent_indices.append((i-1,j))
    if i+1 < m:
        adjacent_indices.append((i+1,j))
    if j > 0:
        adjacent_indices.append((i,j-1))
    if j+1 < n:
        adjacent_indices.append((i,j+1))
    return adjacent_indices


def search(state, solutions):
    if is_valid_state(state):
        solutions.append(state.copy())
        # return

    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)


def find(element, matrix):
    for i, matrix_i in enumerate(matrix):
        for j, value in enumerate(matrix_i):
            if value == element:
                return (i, j)


def solve():
    start = find('S', board)
    print(len(board))
    print(len(board[0]))
    # solutions = []
    # state = set()
    # search(state, solutions)
    # return solutions


solve()
