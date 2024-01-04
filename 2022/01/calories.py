import sys


def load_data(filename):
    data = []
    with open(filename) as file:
        for line in file:
            data.append(line.strip())

    return data


class Elf:
    calories_carrying = 0
    index = 0

    def __init__(self, index, calories):
        self.calories_carrying = calories
        self.index = index

    def __repr__(self):
        return "{Elf, calories=%s, index=%s}" % (self.calories_carrying, self.index)

    def getCalories(self):
        return self.calories_carrying


def main():
    calories = load_data(sys.argv[1])
    print(calories)
    elfs = []
    sum = 0
    idx = 0
    for calory in calories:
        if calory != '':
            sum = sum + int(calory)
        else:
            elfs.append(Elf(idx, sum))
            sum = 0
            idx = idx + 1

    elfs.append(Elf(idx, sum))

    # Get the elf carryinig most calories
    print(findElfWithMostCalories(elfs))


def findElfWithMostCalories(list):
    max = None
    for elf in list:
        if max is None or elf.getCalories() > max.getCalories():
            max = elf
    return max


if __name__ == "__main__":
    main()
