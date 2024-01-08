def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f]

    total_points = 0

    for index, line in enumerate(lines):
        split_a = line.split(":")

        card_number = split_a[0].split()[1]
        winning_numbers = split_a[1].split("|")[0].split()
        my_numbers = split_a[1].split("|")[1].split()

        matches = 0
        points = 0

        for num in winning_numbers:
            if num in my_numbers:
                matches = matches + 1
                if points == 0:
                    points = 1
                else:
                    points = points * 2

        print('Card ' + str(card_number) + ' is worth ' +
              (str(points) if points > 0 else 'no') + ' points')

        total_points = total_points + points

    print(f'The pile is worth {total_points} points in total')
    return total_points


def part_two(lines):
    # each number match grants you copy of next card(s) equal to the number of matches,
    # i.e 4 matches = you get copies of next 4 cards
    # process original and copies of scratchcards 'until no more scratchcards are won'
    # inluding the original set of scratchcards (like 200? in input.txt) how many total
    # scratchcards do you end up with?

    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
