def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    left_ids = []
    right_ids = []

    for line in lines:
        left, right = line.split()
        left_ids.append(left)
        right_ids.append(right)

    left_sorted = sorted(left_ids)
    right_sorted = sorted(right_ids)

    if len(left_sorted) != len(right_sorted):
        raise ValueError("Left and right ids do not match")
    
    id_sum = 0
    for i in range(len(left_sorted)):
        distance = abs(int(left_sorted[i]) - int(right_sorted[i]))
        id_sum += distance

    print(id_sum)
    return id_sum


def part_two():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    left = []
    right = [] 

    for line in lines:
        line_left, line_right = line.split()
        left.append(int(line_left))
        right.append(int(line_right))

    similarity_score = 0
    for id in left:
        appears_times = find_in_list(right, id)
        similarity_score += id * appears_times

    print(similarity_score)
    return similarity_score


def find_in_list(list, id):
    appears_times_sum = 0
    for right_id in list:
        if right_id == id:
            appears_times_sum += 1

    return appears_times_sum


if __name__ == '__main__':
    main()
    part_two()
