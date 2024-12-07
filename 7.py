
from itertools import product

def data(filename):
    res = []
    for line in open(filename):
        total, nums = line.strip().split(":")
        total, nums = int(total), [int(x) for x in nums.strip().split(" ")]
        res.append((total, nums))
    return res

def generate(allmoves, n):
    res = []
    for aCombination in product(allmoves, repeat=n):
        res.append(list(aCombination))
    return res 
    
def do_op(a, b, op):
    if op == "+":
        return a + b
    elif op == "*":
        return a * b
    else:
        return int(str(a) + str(b))

def solver(allmoves, filename):
    sum = 0
    for total, nums in data(filename):
        for ops in generate(allmoves, len(nums)-1):
            start = nums[0]
            numidx = 1
            opidx = 0
            while opidx < len(ops):
                start = do_op(start, nums[numidx], ops[opidx])
                numidx += 1
                opidx += 1
            
            if start == total:
                sum += total
                break
    return sum

def part1(filename):
    sum = solver(['+', '*'], filename)
    print("Part 1 for ", filename, " is ", sum)

def part2(filename):
    sum = solver(['+', '*', '$'], filename)
    print("Part 1 for ", filename, " is ", sum)

part1("data/7demo.txt")
part1("data/7.txt")

part2("data/7demo.txt")
part2("data/7.txt")
