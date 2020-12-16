from collections import Counter
starting_numbers = [11,18,0,20,1,7,16]
searched_turn = 30000000
counter = Counter(starting_numbers)
turn_appareances = {}
turn = 1

for number in starting_numbers:
    turn_appareances[number] = [turn, turn]
    last_element = number
    turn += 1
for new_turn in range(turn, searched_turn + 1, 1):
    if counter[last_element] == 1:
        last_element = 0
    elif counter[last_element] > 1:
        appareances = turn_appareances.get(last_element)
        turn_appareances[last_element] = [appareances[1], new_turn]
        counter[last_element] += 1
        last_element = appareances[1] - appareances[0]
    appareances = turn_appareances.get(last_element, None)
    if appareances:
        counter[last_element] += 1
        turn_appareances[last_element][1] = new_turn
    else:
        counter[last_element] = 1
        turn_appareances[last_element] = [new_turn, new_turn]
    print(f"Turn: {new_turn} Last element: {last_element}")
