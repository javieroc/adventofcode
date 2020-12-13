numbers = [int(x) for x in open("input.txt").readlines()]

def find_summands(numbers: [int], num: int) -> (int, [int]):
    accum = 0
    summands = []
    result = None
    for x in numbers:
        summands.append(x)
        accum = accum + x
        if accum == num:
            result = num
            break
        if accum > num:
            break
    return (result, summands)

def solve(numbers, num):
    result = None
    while len(numbers) > 2 and not result:
        result,summands = find_summands(numbers, num)
        if result and summands:
            summands.sort()
            result = summands[0] + summands[len(summands)-1]
        else:
            numbers = numbers[1:]
    return result

result = solve(numbers, 542529149)
print(f"Result: {result}")
