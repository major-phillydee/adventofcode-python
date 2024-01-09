def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f]

    numbers = []

    line_len = len(lines[0])
    lines.insert(0, str("." * (line_len + 2)))
    lines.append(str("." * (line_len + 2)))

    for line in lines:
        line = "." + line + "."

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

    print('Valid parts sum = ' + str(parts_sum))

    return parts_sum


def is_valid_part(number, lines):
    line_nr = number['line_nr']
    length = number['len']
    start_idx = number['start_idx']

    # Get fragment of string above
    string_above = lines[line_nr - 1][start_idx - 1:start_idx + length + 1]

    # The same line
    line = lines[line_nr]
    left_side = line[start_idx - 1:start_idx]
    right_side = line[start_idx + length:start_idx + length + 1]

    string_below = lines[line_nr + 1][start_idx - 1:start_idx + length + 1]

    print('above: ' + string_above)
    print('mid  : ' + left_side + str(number['value']) + right_side)
    print('below: ' + string_below)
    print('num  : ' + str(number))

    # Test for a symbol in a string
    if has_symbol(string_above):
        # print('has symbol above: True')
        return True

    # print('left side = ' + left_side)
    if has_symbol(left_side):
        # print('has symbol on the left: True')
        return True

    # print('Right side = ' + right_side)
    if has_symbol(right_side):
        # print('has symbol on the right: True')
        return True

    # Test for a symbol in a string below
    if has_symbol(string_below):
        # print('has symbol below: True')
        return True

    print('NOT valid part\n\n')

    return False


def has_symbol(string):
    no_dots = [i for i in string if i != '.' and not i.isnumeric()]
    return len(no_dots) > 0


main()
