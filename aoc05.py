# Day 05 of Advent of Code
def get_inputs(path):
    seeds = []
    almanac = {}
    with open(path, "r") as file:
        seeds = list(map(int, file.readline().strip().split()[1:]))
        file.readline()

        while mapName := file.readline().strip():
            mapName = mapName.split()[0]
            almanac[mapName] = []
            while l := file.readline().strip():
                almanac[mapName].append(list(map(int, l.split())))

    return seeds, almanac


def inSpan(start, range, x):
    return x >= start and x < range + start


def part1(seeds: list, almanac: dict):
    dists = []
    for seed in seeds:
        thing = []
        # print(f"Setting check: {seed}")
        check = seed
        for k, v in almanac.items():
            for dr, sr, rl in v:
                if inSpan(sr, rl, check):
                    check = dr + check - sr
                    # print(
                    #     f"Seed: {seed}.\tCheck: {check}\tdr,sr,rl: {dr}, {sr}, {rl}.\tMap: {k}."
                    # )
                    break

            thing.append(check)
        # print(f"what {thing}")
        dists.append(thing[-1])
    # print(dists)
    return min(dists)


def part2(seeds, almanac):
    seedList = 0
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        end = seeds[i + 1] + start

        seedList += end - start
    # print(seedList)

    return seedList


if __name__ == "__main__":
    seeds, almanac = get_inputs("inputs/day05")
    # seeds, almanac = get_inputs("test/test05")

    # print(seeds, almanac)

    # p1 = part1(seeds, almanac)
    # print(p1)

    p2 = part2(seeds, almanac)
    print(p2)
