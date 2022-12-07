def is_range_contains(r1: list[int], r2: list[int]) -> bool:
    [r1a, r1b] = r1
    [r2a, r2b] = r2
    return (r1a <= r2a and r2b <= r1b) or (r2a <= r1a and r1b <= r2b)


def is_range_overlaping(r1: list[int], r2: list[int]) -> bool:
    [r1a, r1b] = r1
    [r2a, r2b] = r2
    return (r2a in range(r1a, r1b+1)) or (r2b in range(r1a, r1b+1)) or (r1a in range(r2a, r2b+1)) or (r1b in range(r2a, r2b+1))

def solve():
    file_strings = [x.replace('\n', '') for x in open("input.txt").readlines()]
    ranges = [[list(map(lambda z: int(z), y.split('-'))) for y in x.split(',')] for x in file_strings]
    count = 0
    for range in ranges:
        [r1, r2] = range
        if (is_range_overlaping(r1, r2)):
            count += 1
    print(count)

solve()
