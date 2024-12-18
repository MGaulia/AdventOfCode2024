def solve(filename, maxlevels):
    d = {int(k): 1 for k in open(filename).readlines()[0].split()}

    cache = {}

    def blinkstone(stone, level):
        if level == 0:
            return 1
        elif (stone, level) in cache:
            return cache[(stone, level)]
        elif stone == 0:
            temp = blinkstone(1, level - 1)
        elif len(strstone := str(stone)) % 2 == 0:
            mid = len(strstone) // 2
            left = strstone[:mid].lstrip("0")
            if left == "":
                left = 0
            right = strstone[mid:].lstrip("0")
            if right == "":
                right = 0
            temp = blinkstone(int(left), level - 1) + blinkstone(int(right), level - 1)
        else:
            temp = blinkstone(2024 * stone, level - 1)
        cache[(stone, level)] = temp
        return temp

    return sum([blinkstone(i, maxlevels) for i in d.keys()])


print("Part 1 for is", solve("data/11demo.txt", 25))
print("Part 1 for is", solve("data/11.txt", 25))
print("Part 2 for is", solve("data/11demo.txt", 75))
print("Part 2 for is", solve("data/11.txt", 75))
