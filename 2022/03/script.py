def find_item(first_compartment: str, second_compartment: str) -> str:
    for item in first_compartment:
        if item in second_compartment:
            return item


def solve():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rucksack_items = [x.replace('\n', '') for x in open("input.txt").readlines()]
    sum = 0
    for items in rucksack_items:
        middle = len(items)//2
        first_compartment = items[:middle]
        second_compartment = items[middle:]
        item = find_item(first_compartment, second_compartment)
        value = letters.index(item)+1
        sum += value
        print(item)
    print(sum)

solve()
