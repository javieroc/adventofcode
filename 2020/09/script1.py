numbers = [int(x) for x in open("input.txt").readlines()]

def find_summands(numbers: [int], num: int) -> (int, int):
    if (len(numbers) < 2):
        return (-1,-1)
    fst,rest = numbers[0],numbers[1:]
    filtered = list(filter(lambda x: x+fst == num, rest))
    if (filtered):
        return (fst, filtered.pop(0))
    return find_summands(rest, num)

def solve():
    rest_numbers = numbers[25:]
    first_fail_number = None
    for index, num in enumerate(rest_numbers):
        sum1, sum2 = find_summands(numbers[index:25+index], num)
        if sum1 == -1 and sum2 == -1:
            first_fail_number = num
            break
    return first_fail_number

result = solve()
print(f"Result: {result}")
