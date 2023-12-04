# Day 03 of Advent of Code

import re
import math


def get_inputs(path):
    inputs = []
    with open(path, "r") as file:
        inputs = [line.strip() for line in file]

    return inputs


def getSpansAndNumbers(line):
    p = re.compile(r"\d+")
    numbers = p.findall(line)
    iter = p.finditer(line)
    spans = [s.span() for s in iter]
    return spans, numbers


def hasSign(engine, row, span, w, h):
    NUMBERS = "1234567890"
    startY = max(row - 1, 0)
    endY = min(row + 2, h)
    startX = max(span[0] - 1, 0)
    endX = min(span[1] + 1, w)

    # print(f"Row: {row}. span: {span}. y: {startY}-{endY}. x: {startX},{endX}.")

    for y in range(startY, endY):
        for x in range(startX, endX):
            e = engine[y][x]
            if e not in NUMBERS and e not in ".":
                return e, x, y
    return False


def part1(engine):
    w = len(engine[0])
    h = len(engine)
    res = []
    for rowIdx, row in enumerate(engine):
        spans, numbers = getSpansAndNumbers(row)
        # print(spans, numbers)
        if not spans:
            continue
        for i, span in enumerate(spans):
            # print(numbers[i])
            if hasSign(engine, rowIdx, span, w, h):
                res.append(int(numbers[i]))
    # print(res)
    # print(sum(res))
    return sum(res)


def inSpan(sX, s):
    return sX >= s[0] and sX < s[1]


def part2(engine):
    w = len(engine[0])
    h = len(engine)
    stars = {}
    for rowIdx, row in enumerate(engine):
        spans, numbers = getSpansAndNumbers(row)
        # print(spans, numbers)
        if not spans:
            continue
        for i, span in enumerate(spans):
            # print(numbers[i])
            if hasSign(engine, rowIdx, span, w, h):
                e, x, y = hasSign(engine, rowIdx, span, w, h)
                if e == "*":
                    key = f"x: {x}, y: {y}"
                    if key in stars:
                        stars[key].append(numbers[i])
                    else:
                        stars[key] = [numbers[i]]

    print(stars)
    res = 0
    for v in stars.values():
        if len(v) > 1:
            res += math.prod(list(map(int, v)))

    return res


"""
def part1(engine):
    NUMBERS = "1234567890"

    w = len(engine[0])
    h = len(engine)
    visited = {}
    res = []
    for y in range(h):
        for x in range(w):
            e = engine[y][x]
            if e not in NUMBERS and e not in ".":
                for i in range(y - 1, y + 2):
                    for j in range(x - 1, x + 2):
                        if i >= 0 and i < h and j >= 0 and j < w:
                            p = engine[i][j]
                            if p in NUMBERS:
                                spans, numbers = getSpansAndNumbers(engine[i])
                                for ix, s in enumerate(spans):
                                    # if inSpan(j, s):
                                    # print(f"x,y: {x},{y}. j,i: {j},{i}. span: {s}")
                                    key = f"{e}:{str(x)},{str(y)}"
                                    if key not in visited:
                                        # print(f"Added {numbers[ix]} at key: {key}")
                                        visited[key] = [s]
                                        res.append(int(numbers[ix]))
                                    elif s not in visited[key]:
                                        # print(f"Pended {numbers[ix]} at key: {key}")
                                        visited[key].append(s)
                                        res.append(int(numbers[ix]))

    print(visited)
    print(res)
    return sum(res)
def partRE(engine):
    p = re.compile(r"[^.]+")
    for l in engine:
        m = p.findall(l)
        print(m)
        ind = p.finditer(l)
        if m:
            for match in ind:
                print(match.span())
            # print(ind)
"""

if __name__ == "__main__":
    engine = get_inputs("inputs/day03")
    # engine = get_inputs("test/test03")

    # p1 = part1(engine)
    # print(p1)

    p2 = part2(engine)
    print(p2)
