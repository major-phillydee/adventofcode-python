def main(part_no):
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f]

    # Parse stacks
    stack_lines = lines[0:9]
    CRATE_COLUMNS_INDEX = 8

    # Get create columns indexe
    crate_indexes = []
    for index, ch in enumerate(stack_lines[CRATE_COLUMNS_INDEX]):
        if ch.isnumeric():
            crate_indexes.append(index)

    # Fill column stacks
    stacks = []
    for column in crate_indexes:
        column_stack = []
        for line in reversed(stack_lines[0:8]):
            if column + 1 > len(line):
                continue
            if not line[column + 1].isalpha():
                continue
            column_stack.append(line[column + 1])

        stacks.append(column_stack)

    # Parse move instructions
    instructions = lines[10:]

    for instruction in instructions:
        how_many = int(instruction.split()[1])

        source = instruction.split()[3]
        source_idx = int(source) - 1

        destination = instruction.split()[5]
        destination_idx = int(destination) - 1

        if part_no == 1:
            # part 1
            for i in range(how_many):
                stacks[destination_idx].append(stacks[source_idx].pop())

        elif part_no == 2:
            # part 2
            current_load = stacks[source_idx][-how_many:]
            stacks[source_idx] = stacks[source_idx][0:-how_many]
            stacks[destination_idx] += current_load

    # Generate string of last item on every stack
    output = ''.join([item[-1] for item in stacks])

    return output


if __name__ == "__main__":
    print(f'Part 1: {main(1)}')
    print(f'Part 2: {main(2)}')
