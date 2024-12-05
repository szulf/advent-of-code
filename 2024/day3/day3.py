import re


def part1(file_name):
    sum = 0

    file = open(file_name, "r")
    while data := file.readline():
        arr = re.findall(r"mul\((\d*),(\d*)\)", data)
        for v in arr:
            sum += int(v[0]) * int(v[1])

    return sum


def part2(file_name):
    sum = 0
    do = True

    file = open(file_name, "r")
    while data := file.readline():
        arr = re.findall(r"mul\((\d*),(\d*)\)|(do\(\))|(don't\(\))", data)
        for v in arr:
            x = list(filter(lambda a: a != '', list(v)))
            if x[0] == "do()":
                do = True
            elif x[0] == "don't()":
                do = False
            else:
                if do:
                    sum += int(x[0]) * int(x[1])

    return sum


# print(part1("input.txt"))
print(part2("input.txt"))
