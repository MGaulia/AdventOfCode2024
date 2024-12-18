from collections import deque


def data(rows, cols, bytes, filename):
    pos = []
    for i in open(filename):
        tokens = i.strip().split(",")
        x, y = int(tokens[0]), int(tokens[1])
        pos.append((x, y))

    grid = [["." for _ in range(cols)] for _ in range(rows)]
    print("Bytes: ", pos[bytes-1])
    for x, y in pos[:bytes]:
        grid[y][x] = "#"

    for g in grid:
        print("".join(g))
    print()
    return grid


def shortestPath(grid):
    m, n = len(grid), len(grid[0])

    # x, y, obstacles, steps
    q = deque([(0, 0, 0)])
    seen = set()

    while q:
        x, y, steps = q.popleft()
        if (x, y) in seen:
            continue
        if (x, y) == (m - 1, n - 1):
            return steps
        seen.add((x, y))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == ".":
                q.append((new_x, new_y, steps + 1))
    return -1


def part1(rows, cols, bytes, filename):
    grid = data(rows, cols, bytes, filename)
    print("Part 1 for" + filename + " is " + str(shortestPath(grid)))

def part2(rows, cols, bytes, filename):
    for i in range(bytes, bytes*5):
        grid = data(rows, cols, i, filename)
        if shortestPath(grid) == -1:
            print("Part 2 for" + filename + " is " + str(i))
            break
        
part1(7, 7, 12, "data/18demo.txt")
part1(71, 71, 1024, "data/18.txt")

part2(7, 7, 12, "data/18demo.txt")
part2(71, 71, 1024, "data/18.txt")
