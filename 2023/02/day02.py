MAX_GREEN = 13
MAX_RED = 12
MAX_BLUE = 14


def main():
    print('advent of code 2023 - day 2')

    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f]

    valid_game_id_sum = 0
    sum_powers = 0

    for line in lines:
        split_a = line.split(":")
        game_id = int(split_a[0].split(" ")[1])

        sets = split_a[1].strip().split("; ")

        if valid_set(sets):
            valid_game_id_sum = valid_game_id_sum + game_id

        sum_powers = sum_powers + get_set_power(sets)

    print({'valid_game_id_sum': valid_game_id_sum, 'sum_powers': sum_powers})
    return valid_game_id_sum


def valid_set(set_list):
    valid_sets_bools = []
    for set in set_list:
        cubes = set.split(", ")
        valid_set = False
        for cube in cubes:
            valid_cube = True
            count = cube.split(" ")[0]
            color = cube.split(" ")[1]

            if color == 'blue' and int(count) > MAX_BLUE:
                valid_cube = False
            if color == 'red' and int(count) > MAX_RED:
                valid_cube = False
            if color == 'green' and int(count) > MAX_GREEN:
                valid_cube = False

            if valid_cube:
                valid_set = True
            else:
                valid_set = False

            valid_sets_bools.append(valid_set)

    are_all_sets_valid = False not in valid_sets_bools

    return are_all_sets_valid


def get_set_power(set_list):
    max_red = 1
    max_green = 1
    max_blue = 1

    for set in set_list:
        cubes = set.split(", ")
        for cube in cubes:
            count = int(cube.split(" ")[0])
            color = cube.split(" ")[1]

            if color == 'red':
                if count > max_red:
                    max_red = count

            if color == 'green':
                if count > max_green:
                    max_green = count

            if color == 'blue':
                if count > max_blue:
                    max_blue = count

    set_power = max_red * max_green * max_blue
    return set_power


main()
