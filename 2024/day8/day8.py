from collections import defaultdict


def part1(file_name: str) -> int:
    file = open(file_name, "r")
    data = [x for x in file]

    frequencies = defaultdict(list)
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            if char != "." and char != "\n":
                frequencies[char].append((x, y))

    antinodes = set()
    for key, values in frequencies.items():
        for value in values:
            for val in values:
                if value == val:
                    continue

                distance = (val[0] - value[0], val[1] - value[1])
                pos = (val[0] + distance[0], val[1] + distance[1])

                if is_in_bounds(data, pos):
                    antinodes.add(pos)

    return len(antinodes)


def is_in_bounds(data: [str], pos: (int, int)) -> bool:
    if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(data) or pos[1] >= len(data[0]) - 1:
        return False
    return True


def part2(file_name: str) -> int:
    file = open(file_name, "r")
    data = [x for x in file]

    frequencies = defaultdict(list)
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            if char != "." and char != "\n":
                frequencies[char].append((x, y))

    antinodes = set()
    for key, values in frequencies.items():
        for value in values:
            for val in values:
                if value == val:
                    continue

                distance = (val[0] - value[0], val[1] - value[1])
                pos1 = (val[0] + distance[0], val[1] + distance[1])
                pos2 = (val[0] - distance[0], val[1] - distance[1])

                while is_in_bounds(data, pos1):
                    antinodes.add(pos1)
                    pos1 = (pos1[0] + distance[0], pos1[1] + distance[1])

                while is_in_bounds(data, pos2):
                    antinodes.add(pos2)
                    pos2 = (pos2[0] + distance[0], pos2[1] + distance[1])

    return len(antinodes)


# print(part1("input.txt"))
print(part2("input.txt"))
