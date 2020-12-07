from functools import reduce

groups = []

with open("input.txt", "r") as file:
    group = []
    for line in file:
        if line == '\n':
            groups.append(reduce(lambda x, y: x.intersection(y), group))
            group = []
            continue
        group.append(set(line.replace('\n', '')))
    groups.append(reduce(lambda x, y: x.intersection(y), group))

counts = list(map(lambda x: len(x), groups))
result = reduce(lambda x, y: x+y, counts)
print(f"Total: {result}")
