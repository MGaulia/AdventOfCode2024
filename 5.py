def data(filename):
    rules, update = open(filename).read().split("\n\n")
    rulesdict = {}
    for a, b in [i.split("|") for i in  rules.split()]:
        a , b = int(a), int(b)
        if a in rulesdict:
            rulesdict[a].append(b)
        else:
            rulesdict[a] = [b]

    update = [[int(j) for j in i.split(',')] for i in update.split()]
    return rulesdict, update


def isvalid(rulesdict, upd):
    for idx, val in enumerate(upd):
        if val not in rulesdict:
            continue
        for before in rulesdict[val]:
            if before in upd and idx > upd.index(before):
                return False
    return True    

def part1(filename):
    rulesdict, updates = data(filename)

    res = 0
    for u in updates:
        if isvalid(rulesdict,u):
            res += u[len(u) // 2]

    print("Part 1 for ", filename, " is ", res)

def part2(filename):
    rulesdict, updates = data(filename)

    def fix(upd):
        for idx, val in enumerate(upd):
            if val not in rulesdict:
                continue
            for before in rulesdict[val]:
                if before in upd and idx > upd.index(before):
                    upd[idx], upd[upd.index(before)] = upd[upd.index(before)], upd[idx]
        return upd

    res = 0
    for u in updates:
        if isvalid(rulesdict,u):
            continue
        while not isvalid(rulesdict,u):
            u = fix(u)
        res += u[len(u) // 2]

    print("Part 2 for ", filename, " is ", res)


part1("data/5demo.txt")
part1("data/5.txt")

part2("data/5demo.txt")
part2("data/5.txt")
