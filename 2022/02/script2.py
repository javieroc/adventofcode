values: dict[str, int] = {
    'A': 1, # Rock
    'B': 2, # Paper
    'C': 3, # Scissor
}

scores: dict[str, int] = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

def play(game: str) -> str:
    mapping = {
        'AX': 'C',
        'AY': 'A',
        'AZ': 'B',

        'BX': 'A',
        'BY': 'B',
        'BZ': 'C',

        'CX': 'B',
        'CY': 'C',
        'CZ': 'A',
    }
    return mapping[game]


def solve():
    strategies = [x.replace('\n', '').split(' ') for x in open("input.txt").readlines()]
    sum = 0
    for strategy in strategies:
        [elf, me] = strategy
        result = play(elf+me)
        value = values[result] + scores[me]
        print(value)
        sum += value
    print(sum)


solve()
