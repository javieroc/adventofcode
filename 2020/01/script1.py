numbers = [int(x) for x in open("input.txt").readlines()]

def solve(numbers):
    for i, pivot in enumerate(numbers):
        for j, candidate in enumerate(numbers, start=i+1):
            if pivot+candidate == 2020:
                return (pivot, candidate)

(num1, num2) = solve(numbers)
print(num1*num2)
