def getdata(filename):
    data = []
    for line in open(filename):
        tokens = line.strip().split(" ")

        def getxy(t):
            x, y = t.split("=")[1].split(",")
            return int(x), int(y)

        x, y = getxy(tokens[0])
        y, x = x, y
        vx, vy = getxy(tokens[1])
        vy, vx = vx, vy
        data.append((x, y, vx, vy))

    return data


def getfinalpos(data, steps, maxx, maxy):
    finalpos = []
    for x, y, vx, vy in data:
        x, y = x + steps * vx, y + steps * vy
        x, y = x - (x // maxx) * maxx, y - (y // maxy) * maxy
        finalpos.append((x, y))
    return finalpos


def getdict():
    return {
        "topleft": 0,
        "topright": 0,
        "botleft": 0,
        "botright": 0,
    }


def incdict(oldd, x, y, midpartx, midparty):
    if x == midpartx or y == midparty:
        return oldd
    d = oldd.copy()
    if x < midpartx and y < midparty:
        d["topleft"] += 1
    elif x >= midpartx + 1 and y >= midparty + 1:
        d["botright"] += 1
    elif x > midpartx and y < midparty:
        d["topright"] += 1
    else:
        d["botleft"] += 1
    return d


def part1(filename, maxx, maxy):
    steps = 100
    data = getdata(filename)
    finalpos = getfinalpos(data, steps, maxx, maxy)
    d = getdict()

    for x, y in finalpos:
        d = incdict(d, x, y, maxx // 2, maxy // 2)

    res = 1
    for v in d.values():
        res *= v

    print("Part 1 for", filename, "is", res)


def part2(filename, maxx, maxy):
    maxrowcount = 0
    maxcolcount = 0
    res = None
    for s in range(1, 10000):
        data = getdata(filename)
        finalpos = getfinalpos(data, s, maxx, maxy)
        d = getdict()
        grid = [["." for _ in range(maxy)] for _ in range(maxx)]
        midpartx = maxx // 2
        midparty = maxy // 2
        for x, y in finalpos:
            d = incdict(d, x, y, midpartx, midparty)
            grid[x][y] = "#"

        rowcounts = max([sum([1 for c in row if c == "#"]) for row in grid])
        colcounts = max(
            [sum([1 for row in grid if row[c] == "#"]) for c in range(maxy)]
        )
        if rowcounts > maxrowcount and colcounts > maxcolcount:
            maxrowcount = rowcounts
            maxcolcount = colcounts
            res = (s, grid)
    print(res[0])
    for g in res[1]:
        print("".join(g))


part1("data/14demo.txt", 7, 11)
part1("data/14.txt", 103, 101)

part2("data/14demo.txt", 7, 11)
part2("data/14.txt", 103, 101)
