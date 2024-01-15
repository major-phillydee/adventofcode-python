def part1():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f]

    print(lines[0:5])

    pairs_counter = 0

    for line in lines:
        pairA = line.split(",")[0]
        pairB = line.split(",")[1]

        rangeA = (int(pairA.split('-')[0]), int(pairA.split('-')[1]))
        rangeB = (int(pairB.split('-')[0]), int(pairB.split('-')[1]))

        if rangeA[0] <= rangeB[0] and rangeA[1] >= rangeB[1]:
            pairs_counter += 1
            continue

        if rangeB[0] <= rangeA[0] and rangeB[1] >= rangeA[1]:
            pairs_counter += 1
            continue

    return pairs_counter


def part2():
    # How many assignment pairs ranges overlap?
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f]

    ranges_overlap = 0

    for line in lines:
        pairA = line.split(",")[0]
        pairB = line.split(",")[1]

        rangeA = (int(pairA.split('-')[0]), int(pairA.split('-')[1]))
        rangeB = (int(pairB.split('-')[0]), int(pairB.split('-')[1]))

        if rangeA[1] >= rangeB[0] or rangeB[1] >= rangeA[0]:
            # Ranges overlap
            ranges_overlap += 1
            continue

    return ranges_overlap


if __name__ == "__main__":
    print(part1())
    print(part2())
