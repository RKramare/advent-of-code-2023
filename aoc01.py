# Day 01 of Advent of Code
def get_inputs(path):
    inputs = []
    with open(path, "r") as file:
        inputs = [line.strip() for line in file]

    return inputs


def part1(inputs):
    NUMBERS = "1234567890"
    res = 0
    for line in inputs:
        tmp = ""
        for c in line:
            if c in NUMBERS:
                tmp = c
                break

        for c in line[::-1]:
            if c in NUMBERS:
                tmp += c
                break
        res += int(tmp)

    return res


def part2(inputs):
    NUMBERS = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]
    res = 0
    for line in inputs:
        best_index = float("inf")
        tmp = ""
        for n in NUMBERS:
            index = line.find(n)
            if index != -1 and index < best_index:
                best_index = index
                tmp = n

        if NUMBERS.index(tmp) < 9:
            tmp = str(NUMBERS.index(tmp) + 1)

        best_index = -2
        tmp2 = ""
        for n in NUMBERS:
            index = line.rfind(n)
            if index != -1 and index > best_index:
                best_index = index
                tmp2 = n

        if NUMBERS.index(tmp2) < 9:
            tmp2 = str(NUMBERS.index(tmp2) + 1)
        res += int(tmp + tmp2)
    return res


if __name__ == "__main__":
    inputs = get_inputs("inputs/day01")
    # inputs = get_inputs("test/test01")
    p1 = part1(inputs)
    p2 = part2(inputs)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
