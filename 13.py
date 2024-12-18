def getButtonXY(tokens):
    def getxint(str):
        return int(str.split("+")[1].split(",")[0])
    def getyint(str):
        return int(str.split("+")[1])
    return getxint(tokens[2]), getyint(tokens[3])

def getPrizeXY(tokens, part1):
    def getxint(str, part1):
        temp = int(str.split("=")[1].split(",")[0])
        return  temp + 10000000000000 if part1 else temp
    def getyint(str, part1):
        temp = int(str.split("=")[1]) + 10000000000000
        return  temp + 10000000000000 if part1 else temp

    return getxint(tokens[1],part1), getyint(tokens[2],part1)

def getdata(filename, part1):
    data = []
    a, b, prize = None, None, None
    for line in open(filename).readlines():
        tokens = line.split()
        if tokens == []:
            data.append((a, b, prize))
            continue
        if tokens[1] == "A:":
            x, y = getButtonXY(tokens)
            a = (x, y)
        if tokens[1] == "B:":
            x, y = getButtonXY(tokens)
            b = (x, y)
        if tokens[0] == "Prize:":
            x, y = getPrizeXY(tokens, part1)
            prize = (x, y)
    data.append((a, b, prize))
    return data

def solve(data):
    res = 0
    for a,b,prize in data:
        res1 = (prize[0] * b[1] - prize[1] * b[0]) / (a[0]*b[1] - b[0]*a[1])
        res2 = (prize[1] * a[0] - prize[0] * a[1]) / (a[0]*b[1] - b[0]*a[1])
        if res1 == int(res1) and res2 == int(res2):
            res +=  3*res1 + res2
    return int(res)

def part1(filename):
    data = getdata(filename, True)
    print("Part 1 for", filename, "is", solve(data))

def part2(filename):
    data = getdata(filename, False)
    print("Part 2 for", filename, "is", solve(data))

part1("data/13demo.txt")
part1("data/13.txt")
part2("data/13demo.txt")
part2("data/13.txt")



    