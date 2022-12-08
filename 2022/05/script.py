'''
[C]         [S] [H]
[F] [B]     [C] [S]     [W]
[B] [W]     [W] [M] [S] [B]
[L] [H] [G] [L] [P] [F] [Q]
[D] [P] [J] [F] [T] [G] [M] [T]
[P] [G] [B] [N] [L] [W] [P] [W] [R]
[Z] [V] [W] [J] [J] [C] [T] [S] [C]
[S] [N] [F] [G] [W] [B] [H] [F] [N]
 1   2   3   4   5   6   7   8   9
'''

import json


def execute_instruction_1(data: dict[int, list[str]], instruction: list[int]):
    [num_crates, from_stack, to_stack] = instruction
    for _ in range(num_crates):
        crate = data[from_stack].pop()
        data[to_stack].append(crate)
    return data


def execute_instruction_2(data: dict[int, list[str]], instruction: list[int]):
    [num_crates, from_stack, to_stack] = instruction
    crates_to_move = data[from_stack][-num_crates:]
    crates_to_keep = data[from_stack][:-num_crates]
    data[from_stack] = crates_to_keep
    data[to_stack].extend(crates_to_move)
    return data


def print_result(data: dict[int, list[str]]):
    result = ''
    for item in data.values():
        if len(item) > 0:
            result += item[len(item)-1]
    print(result)


def solve():
    instructions = [[int(s) for s in x.replace('\n', '').split() if s.isdigit()] for x in open("input.txt").readlines()]
    initial_state: dict[int, list[str]] = {
        1: ['S', 'Z', 'P', 'D', 'L', 'B', 'F', 'C'],
        2: ['N', 'V', 'G', 'P', 'H', 'W', 'B'],
        3: ['F', 'W', 'B', 'J', 'G'],
        4: ['G', 'J', 'N', 'F', 'L', 'W', 'C', 'S'],
        5: ['W', 'J', 'L', 'T', 'P', 'M', 'S', 'H'],
        6: ['B', 'C', 'W', 'G', 'F', 'S'],
        7: ['H', 'T', 'P', 'M', 'Q', 'B', 'W'],
        8: ['F', 'S', 'W', 'T'],
        9: ['N', 'C', 'R']
    }
    state = initial_state
    for instruction in instructions:
        state = execute_instruction_2(state, instruction)
    print(state)
    print_result(state)


solve()
