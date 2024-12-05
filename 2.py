def valid(temp):
    increasing = None
    for i in range(len(temp) - 1):
        diff = temp[i+1] - temp[i]

        if increasing is None:
            if diff > 0:
                increasing = True
            else:
                increasing = False
        if (
            increasing and diff < 0 or
            not increasing and diff > 0 or
            abs(diff) > 3 or 
            diff == 0
            ):
            return False
    return True

def part1(filename):
    res = 0
    for line in open(filename):
        temp = [int(i) for i in line.strip().split()]
        res += valid(temp)
    print("Part 1 for ", filename, " is ", res)

def part2(filename):
    res = 0
    for line in open(filename):
        temp = [int(i) for i in line.strip().split()]
        isvalid = valid(temp)
        if isvalid:
            res += 1
        else:
            for i in range(len(temp)):
                # list without the index i
                temp2 = temp[:i] + temp[i+1:]
                if valid(temp2):
                    res += 1
                    break
    print("Part 2 for ", filename, " is ", res)

part1("data/2demo.txt")
part1("data/2.txt")

part2("data/2demo.txt")
part2("data/2.txt")
