def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    digit_names = ['zero', 'one', 'two', 'three', 'four',
                   'five', 'six', 'seven', 'eight', 'nine']

    coord_sum = 0

    for line in lines:
        for digit in digit_names:
            if 'twone' in line:
                line = line.replace('twone', '2ne', -1)
            if digit in line:
                line = line.replace(digit, str(digit_names.index(digit)), -1)

        numbers = [num for num in line if num.isdecimal()]
        if len(numbers) == 0:
            coord = 0
        else:
            coord = int(numbers[0] + numbers[-1])
            # print(coord)

        coord_sum = coord_sum + coord

    print(coord_sum)
    return coord_sum


main()
