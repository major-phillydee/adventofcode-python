def main():
    # Load input data from input.txt
    with open('input.txt', 'r') as f:
        moves = [(line.strip().split()[0], line.strip().split()[1]) for line in f]

    starting_position = (0, 0)
    head_pos = starting_position
    tail_pos = starting_position

    visited_by_tail = []
    prev_direction = moves[0][0]
    direction = moves[0][0]

    counter = 0

    for move in moves:
        prev_direction = direction

        direction = move[0]
        distance = int(move[1])
        prev_head_pos = head_pos

        if direction == 'R':
            head_pos = (head_pos[0] + distance, head_pos[1])
        elif direction == 'L':
            head_pos = (head_pos[0] - distance, head_pos[1])
        elif direction == 'U':
            head_pos = (head_pos[0], head_pos[1] + distance)
        elif direction == 'D':
            head_pos = (head_pos[0], head_pos[1] - distance)

        if is_diagonal_move(direction, prev_direction):
            if direction == 'U':
                tail_pos = (head_pos[0], head_pos[1] - 1)
            elif direction == 'D':
                tail_pos = (head_pos[0], head_pos[1] + 1)
            elif direction == 'R':
                tail_pos = (head_pos[0] + 1, head_pos[1])
            elif direction == 'L':
                tail_pos = (head_pos[0] - 1, head_pos[1])
        elif is_reverse(direction, prev_direction):
            tail_pos = head_pos
        else:
            tail_pos = prev_head_pos

        if tail_pos not in visited_by_tail:
            visited_by_tail.append(tail_pos)

        if counter < 20:
            print(head_pos)
            print(tail_pos)
            print('######')

        counter += 1

    print(len(visited_by_tail))
    return len(visited_by_tail)


def is_diagonal_move(direction, prev_direction):
    if direction == 'R' or direction == 'L' and prev_direction in ('U', 'D'):
        return True
    elif direction == 'U' or direction == 'D' and prev_direction in ('R', 'L'):
        return True
    else:
        return False


def is_reverse(direction, prev_direction):
    if prev_direction == 'U' and direction == 'D':
        return True
    elif prev_direction == 'D' and direction == 'U':
        return True
    elif prev_direction == 'R' and direction == 'L':
        return True
    elif prev_direction == 'L' and direction == 'R':
        return True

    return False


if __name__ == '__main__':
    main()
