def data(filename):
    fulltext = []
    for line in open(filename):
        text = line.strip()
        fulltext.append(text)
    return fulltext


def part1(filename):
    fulltext = data(filename)

    def check(tempx, tempy, searchfor):
        if tempx < 0 or tempy < 0 or tempx >= len(fulltext) or tempy >= len(fulltext[0]) or fulltext[tempx][tempy] != searchfor:
            return False
        return True

    res = 0
    for i in range(len(fulltext)):
        for j in range(len(fulltext[i])):
            if fulltext[i][j] != 'X':
                continue
            # left
            if check(i, j - 1, 'M') and check(i, j - 2, 'A') and check(i, j - 3, 'S'):
                res += 1
            # right
            if check(i, j + 1, 'M') and check(i, j + 2, 'A') and check(i, j + 3, 'S'):
                res += 1
            # up
            if check(i - 1, j, 'M') and check(i - 2, j, 'A') and check(i - 3, j, 'S'):
                res += 1
            # down
            if check(i + 1, j, 'M') and check(i + 2, j, 'A') and check(i + 3, j, 'S'):
                res += 1
            # diagonal top left
            if check(i - 1, j - 1, 'M') and check(i - 2, j - 2, 'A') and check(i - 3, j - 3, 'S'):
                res += 1
            # diagonal top right
            if check(i - 1, j + 1, 'M') and check(i - 2, j + 2, 'A') and check(i - 3, j + 3, 'S'):
                res += 1
            # diagonal bottom left
            if check(i + 1, j - 1, 'M') and check(i + 2, j - 2, 'A') and check(i + 3, j - 3, 'S'):
                res += 1
            # diagonal bottom right
            if check(i + 1, j + 1, 'M') and check(i + 2, j + 2, 'A') and check(i + 3, j + 3, 'S'):
                res += 1
    print("Part 1 for ", filename, " is ", res)

def part2(filename):
    fulltext = data(filename)

    def check(tempx, tempy, searchfor):
        if tempx < 0 or tempy < 0 or tempx >= len(fulltext) or tempy >= len(fulltext[0]) or fulltext[tempx][tempy] != searchfor:
            return False
        return True
    def checkcross(tempx, tempy, temptext):
        if check(tempx - 1, tempy - 1, temptext[0]) and check(tempx - 1, tempy + 1, temptext[1]) and check(tempx + 1, tempy - 1, temptext[2]) and check(tempx + 1, tempy + 1, temptext[3]):
            return True
        return False

    res = 0
    for i in range(len(fulltext)):
        for j in range(len(fulltext[0])):
            if fulltext[i][j] != 'A':
                continue
            
            if (
                checkcross(i, j, "MMSS") or 
                checkcross(i, j, "MSMS") or
                checkcross(i, j, "SMSM") or
                checkcross(i, j, "SSMM")
            ):
                res += 1

    print("Part 2 for ", filename, " is ", res)

part1("data/4demo.txt")
part1("data/4.txt")
    
part2("data/4demo.txt")
part2("data/4.txt")