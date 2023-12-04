# Day 04 of Advent of Code
def get_inputs(path):
    inputs = []
    with open(path, "r") as file:
        x = file.readline().find(":") + 1
        file.seek(0)
        inputs = [line.strip()[x:] for line in file]

    inputs = [line.split("|") for line in inputs]
    # print(inputs)
    ans = []
    mine = []
    for line in inputs:
        x = set(map(int, list(filter(None, line[0].split(" ")))))
        y = set(map(int, list(filter(None, line[1].split(" ")))))
        ans.append(x)
        mine.append(y)

    return ans, mine


def part1(ans, mine):
    totalScore = 0
    for g in range(len(ans)):
        corr = len(mine[g].intersection(ans[g]))
        gameScore = 0 if corr == 0 else pow(2, corr - 1)

        totalScore += gameScore
    return totalScore


def part2(ans, mine):
    cards = [1] * len(ans)
    for g in range(len(ans)):
        corr = len(mine[g].intersection(ans[g]))
        for x in range(g + 1, g + corr + 1):
            cards[x] += cards[g]
            # print(f"Set {g}.\tCurr: {x}.\tL: {cards}")
    # print(cards)
    return sum(cards)


if __name__ == "__main__":
    ans, mine = get_inputs("inputs/day04")
    # ans, mine = get_inputs("test/test04")

    # print(ans)
    # print(mine)

    # p1 = part1(ans, mine)
    # print(p1)

    p2 = part2(ans, mine)
    print(p2)
