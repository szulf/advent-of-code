def get_zeros(data: list[str]) -> list:
    zeros = list()

    for i, line in enumerate(data):
        temp = line.find("0")

        while temp != -1:
            zeros.append((i, temp))
            temp = line.find("0", temp + 1)

    return zeros


def in_bounds(data: list[str], pos: tuple[int, int]) -> bool:
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(data) and pos[1] < len(data[0]) - 1


def rec(data: list[str], i: int, j: int, last_val: int, positions: list[tuple[int, int]], seen: set = None):
    if not in_bounds(data, (i, j)):
        return

    if int(data[i][j]) != last_val + 1:
        return

    if seen is not None:
        if (i, j) in seen:
            return
        seen.add((i, j))

    if int(data[i][j]) == 9:
        positions.append((i, j))

    rec(data, i + 1, j, last_val + 1, positions, seen)
    rec(data, i - 1, j, last_val + 1, positions, seen)
    rec(data, i, j + 1, last_val + 1, positions, seen)
    rec(data, i, j - 1, last_val + 1, positions, seen)


def part1(file_name: str) -> int:
    file = open(file_name, "r")
    data = [x for x in file]

    zeros = get_zeros(data)
    trailheads = list()

    for zero in zeros:
        rec(data, zero[0], zero[1], -1, trailheads, set())

    return len(trailheads)


def part2(file_name: str) -> int:
    file = open(file_name, "r")
    data = [x for x in file]

    zeros = get_zeros(data)
    trailheads = list()

    for zero in zeros:
        rec(data, zero[0], zero[1], -1, trailheads)

    return len(trailheads)


print(part1("input.txt"))
print(part2("input.txt"))
