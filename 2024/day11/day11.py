from functools import cache


def part1(file_name: str) -> int:
    file = open(file_name, "r")
    data = [x for x in file][0]
    stones = [int(x) for x in data.split(" ")]

    for i in range(0, 25):
        print(i)
        j_offset = 0
        for j, stone in enumerate(stones):
            j += j_offset
            if stone == 0:
                stones[j] = 1
                continue

            if len(str(stone)) % 2 == 0:
                stones[j] = int(str(stone)[:int(len(str(stone)) / 2)])
                stones = stones[:j + 1] + [int(str(stone)[int(len(str(stone)) / 2):])] + stones[j + 1:]
                j_offset += 1
                continue

            stones[j] = stone * 2024

    return len(stones)


@cache
def get_new_stone_rec(i, stone: int):
    if i == 75:
        return 1

    stones = list()
    sum = 0

    if stone == 0:
        stones.append(1)
    elif len(str(stone)) % 2 == 0:
        stones.append(int(str(stone)[:int(len(str(stone)) / 2)]))
        stones.append(int(str(stone)[int(len(str(stone)) / 2):]))
    else:
        stones.append(stone * 2024)

    for s in stones:
        sum += get_new_stone_rec(i + 1, s)

    return sum


def part2(file_name: str) -> int:
    file = open(file_name, "r")
    data = [x for x in file][0]
    stones = [int(x) for x in data.split(" ")]
    sum = 0

    for s in stones:
        sum += get_new_stone_rec(0, s)

    return sum


# print(part1("input.txt"))
print(part2("input.txt"))
