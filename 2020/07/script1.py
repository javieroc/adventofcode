from functools import reduce
import re

bags = {}
with open("input.txt", "r") as file:
    for line in file:
        key_values = line.replace('\n', '').split('bags contain')
        bags_inside = key_values[1].split(',')
        bags[key_values[0].strip()] = []
        for bag_inside in bags_inside:
            match = re.search(r"(^\d\s*)(\w.+)(\bbags\b|\bbag\b)", bag_inside.strip())
            if match:
                bags[key_values[0].strip()].append({
                    "bag": match.group(2).strip(),
                    "space": int(match.group(1).strip())
                })

def find(haystack, needle) -> [str]:
    keys = []
    for key,value in haystack.items():
        isNeedel = list(filter(lambda bag: bag['bag'] == needle, value))
        if isNeedel:
            keys.append(key)
    return keys

def solve(haystack, needles, result):
    found = list(map(lambda needle: find(haystack, needle), needles))
    new_needles = reduce(lambda x,y: x+y, found)

    result = result + new_needles
    if not new_needles:
        return result
    return solve(haystack, new_needles, result)

bags_who_contains_needle = solve(bags, ['shiny gold'], [])
counter = len(list(set(bags_who_contains_needle)))
print(f"Total: {counter}")
