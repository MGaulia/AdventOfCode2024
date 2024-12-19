import functools


def getdata():
    patterns = None
    designs = []
    for i in open("data/19.txt"):
        if patterns is None:
            patterns = i.strip().split(", ")
            continue
        elif i.strip() != "":
            designs.append(i.strip())
    return patterns, designs


patterns, designs = getdata()


@functools.cache
def dfs(d):
    if d == "":
        return True
    for p in patterns:
        if d.startswith(p):
            if dfs(d[len(p) :]):
                return True
    return False


@functools.cache
def dfswithcount(d):
    if d == "":
        return 1
    res = 0
    for p in patterns:
        if d.startswith(p):
            res += dfswithcount(d[len(p) :])
    return res


def part1():
    print("Part 1 is", sum([dfs(d) for d in designs]))


def part2():
    print("Part 2 is", sum([dfswithcount(d) for d in designs]))

part1()
part2()
