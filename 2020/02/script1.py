stuffs = [x.split(' ') for x in open("input.txt").readlines()]

def solve(stuffs):
    counter = 0
    for item in stuffs:
        lmin,lmax = list(map(lambda x: int(x), item[0].split('-')))
        needle = item[1].replace(':', '')
        occurrences = item[2].replace('\n', '').count(needle)
        if lmin <= occurrences and occurrences <= lmax:
            counter = counter + 1
    return counter

result = solve(stuffs)
print('result: {}'.format(result))
