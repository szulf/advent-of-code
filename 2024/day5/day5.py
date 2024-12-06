from collections import defaultdict


def part1(file_name: str):
    file = open(file_name, "r")

    rules = []
    orders = []
    split = False
    sum = 0

    for line in file:
        if line == "\n":
            split = True
            continue
        if not split:
            rules.append(line)
        else:
            orders.append(line)

    map = defaultdict(list)
    for rule in rules:
        nums = rule.split("|")
        map[int(nums[0])].append(int(nums[1]))

    for order in orders:
        order = order.split(",")
        if is_order_correct(map, order):
            sum += int(order[int(len(order) / 2)])

    return sum


def part2(file_name: str) -> int:
    file = open(file_name, "r")

    rules = []
    orders = []
    split = False
    sum = 0

    for line in file:
        if line == "\n":
            split = True
            continue
        if not split:
            rules.append(line)
        else:
            orders.append(line)

    map = defaultdict(list)
    for rule in rules:
        nums = rule.split("|")
        map[int(nums[0])].append(int(nums[1]))

    for order in orders:
        order = order.split(",")
        if not is_order_correct(map, order):
            x = reorder_order(map, order)
            sum += int(x[int(len(x) / 2)])

    return sum


def is_order_correct(rules: dict, order: list) -> bool:
    seen_elems = []

    for page in order:
        for elem in seen_elems:
            if int(elem) in rules[int(page)]:
                return False
        seen_elems.append(page)

    return True


def reorder_order(rules: dict, order: list) -> list:
    new_list = []

    for i in range(0, len(order)):
        for j in range(0, len(order) - i - 1):
            try:
                if int(order[j]) in rules[int(order[j + 1])]:
                    temp = order[j]
                    order[j] = order[j + 1]
                    order[j + 1] = temp

            except Exception:
                str(Exception)

    return order


# print(part1("input.txt"))
print(part2("input.txt"))
