def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f]

    part1(lines)
    part2(lines)


def part1(lines):
    items_map = get_item_map()

    sum_priority = 0

    for index, line in enumerate(lines):
        compart_A = line[0:int(len(line)/2)]
        compart_B = line[int(len(line)/2):]

        matching_letter = ''

        for letter in compart_A:
            if letter in compart_B:
                matching_letter = letter
                break

        sum_priority = sum_priority + int(items_map[matching_letter])

    print('Priorities sum = ' + str(sum_priority))
    return sum_priority


def part2(lines):
    threes = []
    three = []
    for index, line in enumerate(lines):
        three.append(line)
        if ((index + 1) % 3 == 0):
            threes.append(three)
            three = []

    item_map = get_item_map()
    sum_priority = 0

    for three in threes:
        common_item = ''
        for ch in three[0]:
            if ch in three[1] and ch in three[2]:
                common_item = ch
                break

        sum_priority = sum_priority + item_map[common_item]

    print('Sum priorities = ' + str(sum_priority))
    return sum_priority


def get_item_map():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    item_map = {}

    for index, letter in enumerate(alphabet):
        item_map[letter] = 1 + index

    for index, letter in enumerate(alphabet):
        item_map[letter.upper()] = 27 + index

    return item_map


if __name__ == '__main__':
    main()
