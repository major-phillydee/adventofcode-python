def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f]

    visible_count = 0

    # Count edge trees
    edge_trees = len(lines[0]) + len(lines[-1]) + 2 * (len(lines) - 2)
    visible_count += edge_trees

    visible_trees_left = 0
    visible_trees_right = 0
    visible_trees_top = 0
    visible_trees_bottom = 0

    for index, line in enumerate(lines):
        if index == 0 or index == len(lines) - 1:
            # don't check edge top and bottom trees
            continue

        for idx, tree in enumerate(line):
            if idx == 0 or idx == len(tree) - 1:
                # Edge left and right tree
                continue

            if idx < len(tree) // 2:
                # Start with checking left side
                if visible_left(idx, line):
                    visible_trees_left += 1
                    continue

                if visible_right(idx, line):
                    visible_trees_right += 1
                    continue
            else:
                # Start with checking right side
                if visible_right(idx, line):
                    visible_trees_right += 1
                    continue

                if visible_left(idx, line):
                    visible_trees_left += 1
                    continue

            if index < len(lines) // 2:
                # Start with top check
                if visible_top(idx, line, index, lines):
                    visible_trees_top += 1
                    continue

                if visible_bottom(idx, line, index, lines):
                    visible_trees_bottom += 1
                    continue

            else:
                # Start with checking bottom
                if visible_bottom(idx, line, index, lines):
                    visible_trees_bottom += 1
                    continue

                if visible_top(idx, line, index, lines):
                    visible_trees_top += 1
                    continue

    print(f'Outer trees    = {edge_trees}')
    print(f'visible left   = {visible_trees_left}')
    print(f'visible right  = {visible_trees_right}')
    print(f'visible top    = {visible_trees_top}')
    print(f'visible bottom = {visible_trees_bottom}')

    visible_count += visible_trees_left
    visible_count += visible_trees_right
    visible_count += visible_trees_top
    visible_count += visible_trees_bottom

    return visible_count


def visible_left(idx, line):
    tree = int(line[idx])
    for i in range(idx):
        if int(line[i]) > tree:
            return False

    return True


def visible_right(idx, line):
    tree = int(line[idx])
    for i in range(idx + 1, len(line)):
        if int(line[i]) > tree:
            return False

    return True


def visible_top(idx, line, line_idx, lines):
    height = int(line[idx])
    for i in range(line_idx):
        current_tree = int(lines[i][idx])
        if current_tree > height:
            return False

    return True


def visible_bottom(idx, line, line_idx, lines):
    height = int(line[idx])
    for i in range(line_idx + 1, len(lines)):
        current_tree = int(lines[i][idx])
        if current_tree > height:
            return False

    return True


if __name__ == '__main__':
    print(main())
