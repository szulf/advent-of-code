import math


def part1(file_name: str):
    file = open(file_name, "r")

    calibration_result = 0

    for line in file:
        result, values = line.split(":")
        values = [no_except_int(x) for x in values.split(" ") if no_except_int(x) is not None]

        for i in range(0, 2 ** (len(values) - 1)):
            test = format(i, f"0{len(values) - 1}b")
            sum = values[0]

            for i, val in enumerate(values[1:]):
                if test[i] == "0":
                    sum += val
                elif test[i] == "1":
                    sum *= val

            if sum == int(result):
                calibration_result += sum
                break

    return calibration_result


def no_except_int(x):
    try:
        return int(x)
    except Exception:
        return


def dec_to_base3(n: int, digits: int) -> str:
    output = ""

    while n != 0:
        m = n % 3
        n = math.floor(n / 3)
        output = str(m) + output

    while len(output) != digits:
        output = "0" + output

    return output


def part2(file_name: str):
    file = open(file_name, "r")

    calibration_result = 0

    for line in file:
        result, values = line.split(":")
        values = [no_except_int(x) for x in values.split(" ") if no_except_int(x) is not None]

        for i in range(0, 3 ** (len(values) - 1)):
            test = dec_to_base3(i, len(values) - 1)
            sum = values[0]

            for i, val in enumerate(values[1:]):
                if test[i] == "0":
                    sum += val
                elif test[i] == "1":
                    sum *= val
                elif test[i] == "2":
                    sum = int(str(sum) + str(val))

            if sum == int(result):
                calibration_result += sum
                break

    return calibration_result


# print(part1("input.txt"))
print(part2("input.txt"))
