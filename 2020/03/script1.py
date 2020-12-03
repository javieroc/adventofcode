grid = [[y for y in x.replace('\n', '')] for x in open("input.txt").readlines()]

def solve(startPosition, velocity, numberOfTrees):
    module = len(grid[0])
    endGrid = len(grid)
    newPosition = (startPosition[0]+velocity[0], (startPosition[1]+velocity[1]) % module)
    if newPosition[0] >= endGrid:
        return numberOfTrees
    if grid[newPosition[0]][newPosition[1]] == '#':
        numberOfTrees = numberOfTrees + 1
    return solve(newPosition, velocity, numberOfTrees)

result1 = solve((0,0), (1, 1), 0)
result2 = solve((0,0), (1, 3), 0)
result3 = solve((0,0), (1, 5), 0)
result4 = solve((0,0), (1, 7), 0)
result5 = solve((0,0), (2, 1), 0)
print('Num of trees r1: {}'.format(result1))
print('Num of trees r2: {}'.format(result2))
print('Num of trees r3: {}'.format(result3))
print('Num of trees r4: {}'.format(result4))
print('Num of trees r5: {}'.format(result5))
print('Final results: {}'.format(result1*result2*result3*result4*result5))
