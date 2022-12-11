def has_duplicated(chunk: str) -> bool:
    return len(chunk) != len(set(chunk))


def solve():
    with open("input.txt", "r") as file:
        stream = file.readline()
        window_size = 14
        was_found = False
        start_position = 0
        chunk = None
        while not was_found:
            chunk = stream[start_position:start_position+window_size]
            if not has_duplicated(chunk):
                was_found = True
            start_position += 1
        print(chunk)
        print(start_position+window_size-1)

solve()
