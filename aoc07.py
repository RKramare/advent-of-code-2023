# Day 07 of Advent of Code
from collections import Counter


def get_inputs(path):
    with open(path, "r") as file:
        games = [line.strip().split() for line in file]

    # print(games)
    return games


def part1(games):
    # print(len(games))
    pokerHands = {
        "five": [],
        "four": [],
        "house": [],
        "three": [],
        "two": [],
        "one": [],
        "high": [],
    }
    for hand, bid in games:
        # print(f"Hand: {hand}, bid: {int(bid)}")
        cards = Counter(hand)
        tmp = []
        for c in hand:
            match c:
                case "A":
                    tmp.append(14)
                case "K":
                    tmp.append(13)
                case "Q":
                    tmp.append(12)
                case "J":
                    tmp.append(11)
                case "T":
                    tmp.append(10)
                case _:
                    tmp.append(int(c))
        tmp.append(int(bid))
        intHand = tuple(tmp)

        match max(cards.values()):
            case 5:
                pokerHands["five"].append(intHand)
            case 4:
                pokerHands["four"].append(intHand)
            case 3 if len(cards) == 2:
                pokerHands["house"].append(intHand)
            case 3 if len(cards) > 2:
                pokerHands["three"].append(intHand)
            case 2 if len(cards) == 3:
                pokerHands["two"].append(intHand)
            case 2 if len(cards) == 4:
                pokerHands["one"].append(intHand)
            case 1:
                pokerHands["high"].append(intHand)

    rankedHands = []
    for ph in pokerHands:
        hands = pokerHands[ph]
        hands.sort(reverse=True)
        if hands:
            rankedHands.append(hands)
    rankedHands = sum(rankedHands, [])

    return sum(x[-1] * i for i, x in enumerate(reversed(rankedHands), 1))


def part2(games):
    # print(len(games))
    pokerHands = {
        "five": [],
        "four": [],
        "house": [],
        "three": [],
        "two": [],
        "one": [],
        "high": [],
    }
    for hand, bid in games:
        # print(f"Hand: {hand}, bid: {int(bid)}")
        cards = Counter(hand)
        tmp = []
        jokers = 0
        for c in hand:
            match c:
                case "A":
                    tmp.append(14)
                case "K":
                    tmp.append(13)
                case "Q":
                    tmp.append(12)
                case "J":
                    jokers += 1
                    tmp.append(1)
                case "T":
                    tmp.append(10)
                case _:
                    tmp.append(int(c))
        tmp.append(int(bid))
        intHand = tuple(tmp)

        if jokers and jokers != 5:
            del cards["J"]

        idx = max(enumerate(cards.values()), key=lambda x: x[1])[0]
        # print(idx, cards.keys())
        if jokers != 0 and jokers != 5:
            cards[list(cards.keys())[idx]] += jokers

        match max(cards.values()):
            case 5:
                pokerHands["five"].append(intHand)
            case 4:
                pokerHands["four"].append(intHand)
            case 3 if len(cards) == 2:
                pokerHands["house"].append(intHand)
            case 3 if len(cards) > 2:
                pokerHands["three"].append(intHand)
            case 2 if len(cards) == 3:
                pokerHands["two"].append(intHand)
            case 2 if len(cards) == 4:
                pokerHands["one"].append(intHand)
            case 1:
                pokerHands["high"].append(intHand)

    rankedHands = []
    for ph in pokerHands:
        hands = pokerHands[ph]
        hands.sort(reverse=True)
        if hands:
            rankedHands.append(hands)
    rankedHands = sum(rankedHands, [])
    # print(rankedHands)

    return sum(x[-1] * i for i, x in enumerate(reversed(rankedHands), 1))


if __name__ == "__main__":
    games = get_inputs("inputs/day07")
    # games = get_inputs("test/test07")

    # p1 = part1(games)
    # print(p1)

    p2 = part2(games)
    print(p2)
