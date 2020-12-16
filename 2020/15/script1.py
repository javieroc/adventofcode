starting_numbers = [11,18,0,20,1,7,16]
starting_numbers_test = [1,3,2]

def find_last_index(numbers: [int], ele: int) -> int:
    return len(numbers) - numbers[::-1].index(ele) - 1

def play(numbers: [int], stop):
    while len(numbers) < stop:
        last_number = numbers[-1]
        if numbers.count(last_number) == 1:
            numbers.append(0)
        else:
            diff = find_last_index(numbers, last_number) - find_last_index(numbers[:-1], last_number)
            numbers.append(diff)
    return numbers[-1]

result = play(starting_numbers, 2020)
print(f"Result turn 2020: {result}")
