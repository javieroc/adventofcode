from functools import reduce
import re

rules = {}
your_ticket = None
nearby_tickets = []

with open("input.txt", "r") as file:
    data_group = 1
    for line in file:
        contains_numbers = bool(re.search(r"\d", line))
        if line == '\n':
            data_group = data_group + 1
        if data_group == 1 and contains_numbers:
            rule_name,range_string = line.replace('\n', '').split(':')
            group1,group2 = re.findall(r"([0-9]+-[0-9]+)", range_string.strip())
            r1,r2 = group1.split('-')
            l1,l2 = group2.split('-')
            rules[rule_name] = [range(int(r1), int(r2)+1),range(int(l1), int(l2)+1)]
        if data_group == 2 and contains_numbers:
            your_ticket = [int(x) for x in line.replace('\n', '').split(',')]
        if data_group == 3 and contains_numbers:
            nearby_tickets.append([int(x) for x in line.replace('\n', '').split(',')])


def is_valid_value(value: int) -> bool:
    result = False
    for rule in rules:
        for rule_range in rules[rule]:
            if value in rule_range:
                result = True
                break
        if result:
            break
    return result

def solve():
    invalid_values = []
    for ticket in nearby_tickets:
        for value in ticket:
            if not is_valid_value(value):
                invalid_values.append(value)
    result = reduce(lambda accum,x: accum + x, invalid_values, 0)
    print(invalid_values)
    return result

result = solve()
print(f"Result: {result}")

#print(rules)
#print(is_valid_value(935))
