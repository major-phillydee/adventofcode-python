opp_values = {'rock': 'A', 'paper': 'B', 'scissors': 'C'}
my_values = {'rock': 'X', 'paper': 'Y', 'scissors': 'Z'}


def main():

    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f]

    total_score = 0

    for index, line in enumerate(lines):
        opp_play = line.split()[0]
        my_play = line.split()[1]

        round_score = calc_round_points(opp_play, my_play) + points_for_shape(my_play)

        print('Round ' + str(index + 1) + ' - ' + str(round_score) + ' points')
        total_score = total_score + round_score

    print('Total score: ' + str(total_score))
    return total_score


def points_for_shape(shape):

    points = 0

    if shape.upper() == my_values['rock']:
        points = 1
    elif shape.upper() == my_values['paper']:
        points = 2
    elif shape.upper() == my_values['scissors']:
        points = 3

    return points


def calc_round_points(op, my):

    WON = 6
    DRAW = 3
    LOST = 0

    score = 0

    # opponent played ROCK
    if op == opp_values['rock']:
        if my == my_values['paper']:
            score = WON
        elif my == my_values['scissors']:
            score = LOST
        elif my == my_values['rock']:
            score = DRAW

    # oponent played PAPER
    elif op == opp_values['paper']:
        if my == my_values['rock']:
            score = LOST
        elif my == my_values['scissors']:
            score = WON
        elif my == my_values['paper']:
            score = DRAW

    # oponent played SCISSORS
    elif op == opp_values['scissors']:
        if my == my_values['paper']:
            score = LOST
        elif my == my_values['rock']:
            score = WON
        elif my == my_values['scissors']:
            score = DRAW

    return int(score)


if __name__ == '__main__':
    main()
