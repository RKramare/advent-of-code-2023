# Day 08 of Advent of Code
def get_inputs(path):
    with open(path, "r") as file:
        rl = file.readline().strip()
        file.readline()
        network = [line.strip().split(" = ") for line in file]
    for n in network:
        n[1] = tuple(n[1][1:-1].split(", "))
    network = {k: v for k, v in network}
    return rl, network


def part1(rl, network):
    ptr = "AAA"
    i = 0
    s = len(rl)

    while True:
        dir = 0 if rl[i % s] == "L" else 1
        ptr = network[ptr][dir]
        i += 1
        if ptr == "ZZZ":
            break

    return i


def part2(rl, network):
    ptr = []
    i = 0
    s = len(rl)

    for k in network.keys():
        if k[2] == "A":
            ptr.append(k)

    print(f"Starting ptrs: {len(ptr)}:  {ptr}")
    while True:
        if i % 10000000 == 0:
            print(f"i: {i}. ptrs: {ptr}")
        dir = 0 if rl[i % s] == "L" else 1
        allZ = True
        for j, p in enumerate(ptr):
            p = network[p][dir]
            ptr[j] = p
            if p[2] != "Z":
                allZ = False
        # print(f"ptr {ptr}")
        i += 1
        if allZ:
            break
    return i


if __name__ == "__main__":
    rl, network = get_inputs("inputs/day08")
    # rl, network = get_inputs("test/test08")

    # p1 = part1(rl, network)
    # print(p1)

    p2 = part2(rl, network)
    print(p2)
