# Day 06 of Advent of Code
import math


def get_inputs(path):
    with open(path, "r") as file:
        time = list(map(int, list(filter(None, file.readline().strip().split()))[1:]))
        dist = list(map(int, list(filter(None, file.readline().strip().split()))[1:]))

    return time, dist


def part1(time, dist):
    res = []
    for i in range(len(time)):
        t = time[i]
        d = dist[i]
        ways = 0
        for x in range(t):
            remainingTime = t - x
            speed = x
            travel = remainingTime * speed
            if travel > d:
                ways += 1
        res.append(ways)
    return math.prod(res)


def part2(time, dist):
    t = ""
    d = ""
    for i in range(len(time)):
        t += str(time[i])
        d += str(dist[i])

    t = int(t)
    d = int(d)
    ways = 0
    for x in range(t):
        remainingTime = t - x
        speed = x
        travel = remainingTime * speed
        if travel > d:
            ways += 1

    return ways


if __name__ == "__main__":
    time, dist = get_inputs("inputs/day06")
    # time, dist = get_inputs("test/test06")

    # print(time, dist)

    # p1 = part1(time, dist)
    # print(p1)

    p2 = part2(time, dist)
    print(p2)
