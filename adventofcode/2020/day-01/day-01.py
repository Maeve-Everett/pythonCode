f = open("adventofcode/2020/day-01/day-01-input.txt", "r")
data = f.readlines()
f.close()

def part1():
    for x in data:
        for y in data:
            if (int(x)+int(y) == 2020):
                return int(x)*int(y)

def part2():
    for x in data:
        for y in data:
            for z in data:
                if (int(x)+int(y)+int(z) == 2020):
                    return int(x)*int(y)*int(z)


if __name__ == "__main__":
    print("Part 1: ", part1())
    print("Part 2: ", part2())