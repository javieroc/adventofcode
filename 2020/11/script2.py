from functools import reduce

seats_map = [list(row.replace('\n', '')) for row in open("input.txt").readlines()]

def get_seat_in_direction(cell: (int, int), direction: (int, int), grid: list) -> (int, int):
    new_cell = (cell[0]+direction[0], cell[1]+direction[1])
    if  0 <= new_cell[0] < len(grid) and 0 <= new_cell[1] < len(grid[0]):
        i,j = new_cell
        if grid[i][j] == 'L' or grid[i][j] == '#':
            return new_cell
        else:
            return get_seat_in_direction(new_cell, direction, grid)
    else:
        return (-1,-1)


def next_state_cell(cell: (int, int), grid) -> str:
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1),(0,1),(1,-1), (1,0), (1,1)]
    to_check = list(map(lambda direction: get_seat_in_direction(cell, direction, grid), directions))
    to_check_filtered = list(filter(lambda cell: cell[0] != -1 and cell[1] != -1, to_check))
    seats_occupied = reduce(lambda count, cell: count + 1 if grid[cell[0]][cell[1]] == '#' else count, to_check_filtered, 0)
    i,j = cell
    if grid[i][j] == 'L' and seats_occupied == 0:
        return '#'
    if grid[i][j] == '#' and seats_occupied >= 5:
        return 'L'
    return grid[i][j]


def run_round(grid):
    new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            new_grid[i][j] = next_state_cell((i, j), grid)
    return new_grid


def print_grid(grid):
    for row in grid:
        print("".join(row))
    print('\n')


def is_identical(a: list, b: list) -> bool:
    rows, cols = len(a), len(a[0])
    return all([a[i][j] == b[i][j] for j in range(cols) for i in range(rows)])


def count_occupied_seats(grid):
    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                counter = counter + 1
    return counter


def solve(grid):
    print_grid(grid)
    new_grid = run_round(grid)
    if is_identical(grid, new_grid):
        return new_grid
    return solve(new_grid)


last_grid = solve(seats_map)
print_grid(last_grid)


print(f"Num of occupied seats: {count_occupied_seats(last_grid)}")
