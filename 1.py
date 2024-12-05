

def data(filename):
    left = []
    right = []
    for line in open(filename):
        temp = [int(i) for i in line.split()]
        left.append(temp[0])
        right.append(temp[1])

    return left, right

def part1(filename):
    left, right = data(filename)
    left = sorted(left)
    right = sorted(right)

    diff = 0
    for l, r in zip(left, right):
        diff += abs(l-r)

    print("Result part 1: ", diff)

def part2(filename):
    left, right = data(filename)
    result = 0
    for l in left:
        count = 0
        for r in right:
            if l == r:
                count += 1
        result += count * l

    print("Result part 2: ", result)        

    

part1("data/1demo.txt")
part1("data/1.txt")
part2("data/1demo.txt")
part2("data/1.txt")

