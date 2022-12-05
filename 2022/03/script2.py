def find_item(f1: str, f2: str, f3: str) -> str:
    for item in f1:
        if item in f2 and item in f3:
            return item


def solve():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rucksack_items = [x.replace('\n', '') for x in open("input.txt").readlines()]
    n = 3
    groups = [rucksack_items[i:i+n] for i in range(0, len(rucksack_items), n)]
    sum = 0
    for group in groups:
        [f1, f2, f3] = group
        item = find_item(f1, f2, f3)
        value = letters.index(item)+1
        sum += value
        print(item)
    print(sum)

solve()
