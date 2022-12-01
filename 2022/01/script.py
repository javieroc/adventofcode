from functools import reduce

def sum_calories(calories: list[int]) -> int:
    sum = reduce(lambda sum, x: sum + x, calories, 0)
    return sum


def solve():
    with open("input.txt", "r") as file:
        summarized_calories = []
        elf_calories = []
        for line in file:
            if line == '\n':
                sum = sum_calories(elf_calories)
                summarized_calories.append(sum)
                elf_calories = []
                continue
            calories = int(line.replace('\n', ''))
            elf_calories.append(calories)
        sum = sum_calories(elf_calories)
        summarized_calories.append(sum)
        summarized_calories.sort()
        top_three = summarized_calories[-3:]
        print(top_three)
        print(sum_calories(top_three))

solve()
