from functools import reduce

groups = []

with open("input.txt", "r") as file:
    group = set()
    for line in file:
        if line == '\n':
            groups.append(group)
            group = set()
            continue
        group.update(line.replace('\n', ''))
    groups.append(group)

counts = list(map(lambda x: len(x), groups))
result = reduce(lambda x, y: x+y, counts)
print(f"Total: {result}")
