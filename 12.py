def data(filename):
    data = []
    for line in open(filename):
        data.append(line.strip())

    def neighbors(x, y, data, visited, want):
        neighbors = []
        if x > 0 and (x - 1, y) not in visited and data[x - 1][y] == want:
            neighbors.append((x - 1, y))
        if y > 0 and (x, y - 1) not in visited and data[x][y - 1] == want:
            neighbors.append((x, y - 1))
        if x < len(data) - 1 and (x + 1, y) not in visited and data[x + 1][y] == want:
            neighbors.append((x + 1, y))
        if (
            y < len(data[0]) - 1
            and (x, y + 1) not in visited
            and data[x][y + 1] == want
        ):
            neighbors.append((x, y + 1))
        return neighbors

    regions = []
    globalvisited = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            curr = data[i][j]
            if (i, j) in globalvisited:
                continue
            # new region
            visited = set()
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                globalvisited.add((x, y))
                for n in neighbors(x, y, data, visited, curr):
                    stack.append(n)
            regions.append(visited)

    return regions


def part1(filename):
    regions = data(filename)

    def num_neighbors(x, y, visited):
        res = 0
        for nx, ny in visited:
            diff = abs(x - nx) + abs(y - ny)
            if diff == 1:
                res += 1
        return res

    def get_perimeter(region):
        res = 0
        for x, y in region:
            res += 4 - num_neighbors(x, y, region)
        return res

    total = 0
    for r in regions:
        total += get_perimeter(r) * len(r)

    print("Part 1 for ", filename, "is", total)


def part2(filename):
    regions = data(filename)
    res = 0
    for r in regions:
        fences = []
        for x, y in r:
            neighbors = [
                (x - 1, y, "up"),
                (x + 1, y, "down"),
                (x, y - 1, "left"),
                (x, y + 1, "right"),
            ]
            for nx, ny, direction in neighbors:
                if (nx, ny) not in r:
                    fences.append((x, y, direction))

        counter = 0
        for x, y, dir in fences:
            if (x - 1, y, dir) not in fences:
                counter += 1
            else:
                counter -= 1
            if (x, y - 1, dir) not in fences:
                counter += 1
            else:
                counter -= 1
        res += len(r) * int(counter / 2)

    print("Part 2 for ", filename, "is", res)


part1("data/12demo.txt")
part1("data/12.txt")
part2("data/12demo.txt")
part2("data/12.txt")
