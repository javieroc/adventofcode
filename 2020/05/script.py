boarding_passes = [x.replace('\n', '') for x in open("input.txt").readlines()]

def binaryPartitioning(haystack, needles, key):
    if len(haystack) == 0:
        return None
    if len(haystack) == 1:
        return haystack.pop(0)
    needle = needles.pop(0)
    if needle == key:
        return binaryPartitioning(haystack[:len(haystack)//2], needles, key)
    return binaryPartitioning(haystack[len(haystack)//2:], needles, key)


def solve():
    max_id = 0
    ids = []
    for boarding_pass in boarding_passes:
        row = binaryPartitioning(list(range(128)), list(boarding_pass[:7]), 'F')
        col = binaryPartitioning(list(range(8)), list(boarding_pass[7:]), 'L')
        id = row * 8 + col
        ids.append(id)
        if (id > max_id):
            max_id = id
    ids.sort()
    return ids

ids_sorted = solve()
full_ids = list(range(ids_sorted[0], ids_sorted[len(ids_sorted)-1]+1))
my_id = list(set(full_ids)-set(ids_sorted))
print(f"My bording_pass id: {my_id.pop(0)}")
