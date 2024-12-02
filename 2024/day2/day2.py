def get_nums_from_file(file_name):
    file = open(file_name, "r")

    arr = []
    while data := file.readline():
        strs = data.split(" ")
        local_arr = []
        for v in strs:
            local_arr.append(int(v))
        arr.append(local_arr)

    return arr


def is_safe(arr):
    prev_v = -1
    first = True
    safe = True

    for v in arr:
        if not first:
            if not (v - prev_v <= 3 and v - prev_v >= 1):
                safe = False

        prev_v = v
        first = False

    return safe


def part1(nums):
    safe_count = 0

    for arr in nums:
        if arr[0] > arr[len(arr) - 1]:
            arr.reverse()

        if is_safe(arr):
            safe_count += 1

    return safe_count


def part2(nums):
    safe_count = 0

    for arr in nums:
        if arr[0] > arr[len(arr) - 1]:
            arr.reverse()

        arr_arr = []
        for i, v in enumerate(arr):
            temp = list(arr)
            temp.pop(i)
            arr_arr.append(temp)

        for a in arr_arr:
            if is_safe(a):
                safe_count += 1
                break

    return safe_count


nums = get_nums_from_file("input.txt")
# print(part1(nums))
print(part2(nums))
