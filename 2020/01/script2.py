numbers = [int(x) for x in open("input.txt").readlines()]

def solve(numbers):
    for i, pivot in enumerate(numbers):
        for j, pivot2 in enumerate(numbers, start=i+1):
            for k, candidate in enumerate(numbers, start=j+1):
                if pivot+pivot2+candidate == 2020:
                    return (pivot, pivot2, candidate)

(num1, num2, num3) = solve(numbers)
print(num1*num2*num3)
