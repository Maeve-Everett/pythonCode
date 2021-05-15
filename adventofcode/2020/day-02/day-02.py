f = open("adventofcode/2020/day-02/day-02-input.txt", "r")
data = f.readlines()
f.close()

def part1():
    validpasswords = 0
    for x in data:
        
        splitted = x.split("-", 1)
        minimum = int(splitted[0])
        splitted = splitted[1].split(" ", 1)
        maximum = int(splitted[0])
        splitted = splitted[1].split(":", 1)
        letter = splitted[0]
        password = splitted[1][1:]

        #print("Min:", minimum)
        #print("Max:", maximum)
        #print("Letter:", letter)
        #print("Password:",password)
        #input()

        occurances = 0
        for char in password:
            if char == letter:
                occurances += 1
        
        if occurances in range(minimum, maximum+1):
            validpasswords += 1
    
    return validpasswords


def part2():
    validpasswords = 0
    for x in data:
        
        splitted = x.split("-", 1)
        minimum = int(splitted[0])
        splitted = splitted[1].split(" ", 1)
        maximum = int(splitted[0])
        splitted = splitted[1].split(":", 1)
        letter = splitted[0]
        password = splitted[1][1:]

        #print("Min:", minimum)
        #print("Max:", maximum)
        #print("Letter:", letter)
        #print("Password:",password)
        #input()

        occurances = 0
        count = 1
        for char in password:
            if char == letter and (count == minimum or count == maximum):
                occurances += 1
            count += 1
        
        if occurances == 1:
            validpasswords += 1
    
    return validpasswords


if __name__ == "__main__":
    print("Part 1: ", part1())
    print("Part 2: ", part2())