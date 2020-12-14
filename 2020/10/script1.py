from functools import reduce

adapters = [int(x) for x in open("input.txt").readlines()]
adapters.sort()

def solve():
    differences = {}
    last_adapter = 0
    for adapter in adapters:
        diff = adapter - last_adapter
        if diff not in differences.keys():
            differences[diff] = 1
        else:
            differences[diff] = differences[diff] + 1
        last_adapter = adapter
    return differences

result = solve()
print(f"Result: {result[1] * (result[3] + 1)}")
