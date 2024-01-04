def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f]

    # Get list of numbers on each line of the file
    numbers = []

    for index, line in enumerate(lines):
        start_index = -1
        line_numbers = []
        number = ''
        for ch_idx, ch in enumerate(line):
            if ch.isnumeric():
                if start_index == -1:
                    start_index = ch_idx
                number = number + ch
            else:
                if number != '':
                    line_numbers.append({'value': int(number),
                                         'line_nr': index,
                                         'start_idx': start_index,
                                         'len': len(number)})
                    start_index = -1
                    number = ''
        numbers.append(line_numbers)

    parts_sum = 0

    # Check for numbers adjacent to a symbol
    for line in numbers:
        for num in line:
            print('Checking for valid part on number: '
                  + str(num['value']) + ', on line: ' + str(num['line_nr']))
            if is_valid_part(num, lines):
                parts_sum = parts_sum + num['value']

    print(numbers[-1][-1])

    print('Valid parts sum = ' + str(parts_sum))
    return parts_sum


def is_valid_part(number, lines):
    line_nr = number['line_nr']
    length = number['len']
    start_idx = number['start_idx']

    # Line above
    if line_nr > 0:
        string_above = lines[line_nr - 1]

        # Get fragment of string above
        if start_idx > 0:
            string_above = string_above[start_idx - 1:start_idx + length + 1]
        else:
            string_above = string_above[start_idx:start_idx + length + 1]

        print('line above = ' + string_above)

        # Test for a symbol in a string
        if has_symbol(string_above):
            print('has symbol above: True')
            return True

    # The same line
    line = lines[line_nr]
    if start_idx > 0:
        left_side = line[start_idx - 1:start_idx]
        print('left side = ' + left_side)
        if has_symbol(left_side):
            print('has symbol on the left: True')
            return True

    if start_idx < len(line) - 1 - length:
        right_side = line[start_idx + length:start_idx + length + 1]
        print('Right side = ' + right_side)
        if has_symbol(right_side):
            print('has symbol on the right: True')
            return True

    # Below line
    if line_nr < len(lines) - 1:
        string_below = lines[line_nr + 1]

        # Get fragment of string Below
        if start_idx > 0:
            string_below = string_below[start_idx - 1:start_idx + length + 1]
        else:
            string_below = string_below[start_idx:start_idx + length + 1]

        print('line below = ' + string_below)

        # Test for a symbol in a string below
        if has_symbol(string_below):
            print('has symbol below: True')
            return True


def has_symbol(string):
    no_dots = [i for i in string if i != '.' and not i.isnumeric()]
    return len(no_dots) != 0


main()
