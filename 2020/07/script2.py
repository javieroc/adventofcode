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

def find(haystack, needle):
    bags = haystack[needle]
    if not bags:
        return 0
    return reduce(lambda accum, bag: accum + bag['space'] + bag['space'] * find(haystack, bag['bag']), bags, 0)

result = find(bags, 'shiny gold')
print(f"Result: {result}")
