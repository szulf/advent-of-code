def input_to_disk(data: [str]) -> [str]:
    disk = list()
    ids = 0

    for i, v in enumerate(data):
        try:
            if i % 2 == 0:
                for x in range(0, int(v)):
                    disk.append(str(ids))
                ids += 1
            else:
                for x in range(0, int(v)):
                    disk.append(".")
        except Exception:
            pass

    return disk


def get_last_non_dot_idx(disk: [str]) -> int:
    for i, v in enumerate(disk[::-1]):
        if v != ".":
            return len(disk) - i - 1


def swap(disk: [str], i):
    idx = get_last_non_dot_idx(disk)
    if idx is not None and i < idx:
        temp = disk[i]
        disk[i] = disk[idx]
        disk[idx] = temp
    return disk


def get_checksum(disk):
    checksum = 0
    for i, v in enumerate(disk):
        try:
            checksum += int(v) * i
        except Exception:
            pass

    return checksum


def part1(file_name: str) -> int:
    file = open(file_name, "r")
    data = list([x for x in file][0])

    disk = input_to_disk(data)

    for i, v in enumerate(disk):
        if v == ".":
            disk = swap(disk, i)

    return get_checksum(disk)


def get_i_length(data: [str], val: str, start: int = 0) -> (int, int):
    length = 0

    try:
        idx = data.index(val, start)
    except Exception:
        return -1, 0

    for i in range(idx, len(data)):
        if data[i] == val:
            length += 1
        else:
            break

    return idx, length


def part2(file_name: str) -> int:
    file = open(file_name, "r")
    data = list([x for x in file][0])

    disk = input_to_disk(data)

    id = disk[len(disk) - 1]
    for i, v in enumerate(disk):
        if int(id) < 0:
            break

        dot_idx, dot_length = get_i_length(disk, ".")
        id_idx, id_length = get_i_length(disk, id)

        while dot_length < id_length:
            dot_idx, dot_length = get_i_length(disk, ".", dot_idx + 1)

            if dot_idx == -1:
                break

        if dot_length >= id_length and dot_idx < id_idx:
            for j in range(0, id_length):
                disk[dot_idx + j] = id
                disk[id_idx + j] = "."

        id = str(int(id) - 1)

    return get_checksum(disk)


# print(part1("input.txt"))
print(part2("input.txt"))
