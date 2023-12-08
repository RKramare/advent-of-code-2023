from os.path import exists


def get_tmp(day):
    return f""" # Day {day} of Advent of Code
def get_inputs(path):
    inputs = []
    with open(path, 'r') as file:
        inputs = [line.strip() for line in file]

    print(inputs)
    return inputs

    
def part1(inputs):
    return 0


def part2(inputs):
    return 0

if __name__ == "__main__":
    # tmp = get_inputs("inputs/day{day}")
    tmp = get_inputs("test/test{day}")

    p1 = part1(tmp)
    print(p1)

    # p2 = part2(tmp)
    # print(p2)

"""


def create_day(day):
    day = f"0{day}" if day < 10 else str(day)
    path = "aoc" + day + ".py"
    if not exists(path):
        f = open(path, "w")
        f.write(get_tmp(day))
        f.close()

        d = open("inputs/day" + day, "w")
        d.close()

        t = open("test/test" + day, "w")
        t.close()
    else:
        print("File exists already")


if __name__ == "__main__":
    create_day(8)
