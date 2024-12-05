import re

pattern = r'mul\((\d{1,3},\d{1,3})\)'
pattern2 = r"do\(\)|don't\(\)"

def data(filename):
    fulltext = ''
    for line in open( filename):
        text = line.strip()
        fulltext += text

    return fulltext

def part1(filename):
    fulltext = data(filename)
    res = 0
    for temp in  re.findall(pattern, fulltext):
        parsed = [int(i) for i in temp.split(',')]
        first, second = parsed[0], parsed[1]
        res += first * second
    
    print("Part 1 for ", filename, " is ", res)


def part2(filename):
    fulltext = data(filename)


    ranges = {}
    for i in find(fulltext, "do()") + [0]:
        ranges[i] = 1
    for i in find(fulltext, "don't()"):
        ranges[i] = 0
    ranges = sorted(ranges.items())

    res = 0
    for match in re.finditer(pattern, fulltext, re.IGNORECASE):
        # check the closest range that is below
        for i in range(len(ranges) - 1, -1 , -1 ):
            start, enabled = ranges[i]
            if match.start() >= start:
                if enabled:
                    temp = match.group(0)
                    a, b = [int(t) for t in temp.split("(")[1].split(")")[0].split(",")]
                    res += a * b
                break
    print("Part 2 for ", filename, " is ", res)


def find(text, tofind):
    res = []
    for i in range(len(text) - len(tofind)):
        if text[i:i+len(tofind)] == tofind:
            res.append(i)
    return res

part1("data/3demo.txt")
part1("data/3.txt")

part2("data/3demo2.txt")
part2("data/3.txt")
