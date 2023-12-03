# Day 02 of Advent of Code
def get_inputs(path):
    inputs = []
    with open(path, "r") as file:
        inputs = [line.strip() for line in file]

    # games = {k, v for k, v in inputs.split(",")}

    inputs = [line.split(":") for line in inputs]
    games = {int(k.split(" ")[1]): v.split(";") for k, v in inputs}
    for k, v in games.items():
        tmp = [x.split(",") for x in v]
        res = []
        for round in tmp:
            d = {"red": 0, "green": 0, "blue": 0}
            for x in round:
                x = x.split(" ")
                d[x[2]] = int(x[1])
            res.append(d)

        games[k] = res
    return games


def part1(games):
    validGames = []
    rules = {"red": 12, "green": 13, "blue": 14}
    for gameNr, game in games.items():
        validRound = True
        for round in game:
            if (
                round["red"] > rules["red"]
                or round["green"] > rules["green"]
                or round["blue"] > rules["blue"]
            ):
                validRound = False
        if validRound:
            validGames.append(gameNr)

    print(validGames)
    return sum(validGames)


def part2(games):
    minCubes = 0
    for game in games.values():
        minRed = 0
        minGreen = 0
        minBlue = 0
        for round in game:
            minRed = max(minRed, round["red"])
            minGreen = max(minGreen, round["green"])
            minBlue = max(minBlue, round["blue"])
        minCubes += minRed * minGreen * minBlue

    return minCubes


if __name__ == "__main__":
    games = get_inputs("inputs/day02")
    # games = get_inputs("test/test02")

    # print(games)

    # p1 = part1(games)
    # print(f"Part 1: {p1}")

    p2 = part2(games)
    print(f"Part 2: {p2}")
