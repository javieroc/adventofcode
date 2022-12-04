values: dict[str, int] = {
    'X': 1, # Rock
    'Y': 2, # Paper
    'Z': 3, # Scissor
}


def play(game: str) -> int:
    mapping = {
        'AX': '',
        'AY': 6,
        'AZ': 0,

        'BX': 0,
        'BY': 3,
        'BZ': 6,

        'CX': 6,
        'CY': 0,
        'CZ': 3,
    }
    return mapping[game]


def solve():
    strategies = [x.replace('\n', '').split(' ') for x in open("input.txt").readlines()]
    sum = 0
    for strategy in strategies:
        [elf, me] = strategy
        result = play(elf+me)
        value = values[me] + result
        print(value)
        sum += value
    print(sum)


solve()
