def part1(file_name: str) -> int:
    file = open(file_name, "r")
    data = [x for x in file]

    guard_pos = (-1, -1)
    guard_char = ""

    for x, lines in enumerate(data):
        for y, char in enumerate(lines):
            if char == "^":
                guard_pos = (int(x), int(y))
                guard_char = char

    seen_positions = set()
    seen_positions.add(guard_pos)
    while guard_pos[0] != len(data[0]) - 2 and guard_pos[0] != 0 and guard_pos[1] != len(data) - 1 and guard_pos[1] != 0:
        temp_pos = get_new_pos(guard_pos, guard_char)

        if data[temp_pos[0]][temp_pos[1]] == "#":
            if guard_char == "^":
                guard_char = ">"
            elif guard_char == ">":
                guard_char = "v"
            elif guard_char == "<":
                guard_char = "^"
            elif guard_char == "v":
                guard_char = "<"

        guard_pos = get_new_pos(guard_pos, guard_char)
        seen_positions.add(guard_pos)

    return len(seen_positions)


def get_new_pos(guard_pos: tuple, guard_char: str) -> tuple:
    pos = (-1, -1)
    if guard_char == "^":
        pos = (guard_pos[0] - 1, guard_pos[1])
    elif guard_char == ">":
        pos = (guard_pos[0], guard_pos[1] + 1)
    elif guard_char == "<":
        pos = (guard_pos[0], guard_pos[1] - 1)
    elif guard_char == "v":
        pos = (guard_pos[0] + 1, guard_pos[1])

    return pos


def get_new_guard_char(data: [str], obstacle: tuple, guard_pos, guard_char: str) -> str:
    temp_pos = get_new_pos(guard_pos, guard_char)

    while data[temp_pos[0]][temp_pos[1]] == "#" or obstacle == temp_pos:
        if data[temp_pos[0]][temp_pos[1]] == "#" or obstacle == temp_pos:
            if guard_char == "^":
                guard_char = ">"
            elif guard_char == ">":
                guard_char = "v"
            elif guard_char == "<":
                guard_char = "^"
            elif guard_char == "v":
                guard_char = "<"
        temp_pos = get_new_pos(guard_pos, guard_char)

    return guard_char


def part2(file_name) -> int:
    file = open(file_name, "r")
    data = [x for x in file]

    start_pos = (-1, -1)

    for x, lines in enumerate(data):
        for y, char in enumerate(lines):
            if char == "^":
                start_pos = (int(x), int(y))

    loop_count = 0
    for x, lines in enumerate(data):
        for y, char in enumerate(lines):
            guard_pos = (start_pos[0], start_pos[1])
            guard_char = "^"

            if (x, y) == guard_pos or data[x][y] == "#":
                continue

            seen_positions = set()
            seen_positions.add(guard_pos)
            seen_positions_count = 1

            while guard_pos[1] != len(data[0]) - 2 and guard_pos[1] != 0 and guard_pos[0] != len(data) - 1 and guard_pos[0] != 0:
                guard_char = get_new_guard_char(data, (x, y), guard_pos, guard_char)

                guard_pos = get_new_pos(guard_pos, guard_char)

                if guard_pos in seen_positions:
                    seen_positions_count += 1

                seen_positions.add(guard_pos)

                if seen_positions_count >= 10_000:
                    loop_count += 1
                    break

    return loop_count


# print(part1("input.txt"))
print(part2("input.txt"))
