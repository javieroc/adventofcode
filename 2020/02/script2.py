stuffs = [x.split(' ') for x in open("input.txt").readlines()]

def solve(stuffs):
    counter = 0
    for item in stuffs:
        occurrences = 0
        pos1,pos2 = list(map(lambda x: int(x), item[0].split('-')))
        needle = item[1].replace(':', '')
        haystack = item[2].replace('\n', '')
        if haystack[pos1-1] == needle:
            occurrences = occurrences + 1
        if haystack[pos2-1] == needle:
            occurrences = occurrences + 1
        if occurrences == 1:
            counter = counter + 1
    return counter

result = solve(stuffs)
print('result: {}'.format(result))
