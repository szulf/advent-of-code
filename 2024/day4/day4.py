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


print(part1("input.txt"))
