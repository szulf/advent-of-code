def part1(file_name: str) -> int:
    file = open(file_name, "r")
    data = [x for x in file]
    sum = 0
    for row, line in enumerate(data):
        for col, letter in enumerate(line):
            if letter == "X":
                sum += func(data, letter, row, col, len(data), len(line) - 1)
    return sum


def func(data: [str], string: str, row: int, col: int, max_row: int, max_col: int) -> int:
    sum = 0
    if string == "X":
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if i >= 0 and i < max_row and j >= 0 and j < max_col and (i != row or j != col):
                    try:
                        if data[i][j] == "M":
                            if data[i + i - row][j + j - col] == "A":
                                if data[i + 2 * (i - row)][j + 2 * (j - col)] == "S":
                                    sum += 1
                    except Exception:
                        str(Exception)
    return sum


def part2(file_name: str) -> int:
    sum = 0

    file = open(file_name, "r")
    data = [x for x in file]
    for row, line in enumerate(data):
        for col, letter in enumerate(line):
            if letter == "A":
                if func2(data, col, row, len(data), len(line) - 1):
                    sum += 1
    return sum


def func2(data: [str], col: int, row: int, max_row: int, max_col: int) -> bool:
    sum = 0
    positions = [(row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)]
    opposites = [(row + 1, col + 1), (row + 1, col - 1), (row - 1, col + 1), (row - 1, col - 1)]
    for i, v in enumerate(positions):
        try:
            if v[0] >= 0 and v[0] < max_row and v[1] >= 0 and v[1] < max_col and (v[0] != row or v[1] != col):
                if data[v[0]][v[1]] == "M" and data[opposites[i][0]][opposites[i][1]] == "S":
                    sum += 1
        except Exception:
            str(Exception)
    if sum == 2:
        return True
    return False


# print(part1("sample-input.txt"))
print(part2("input.txt"))
