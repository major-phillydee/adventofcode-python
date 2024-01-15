def part1():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f]

    print(lines[0:10])


if __name__ == "__main__":
    print(part1())
