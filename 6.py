def data(filename):
    map = []
    for line in open(filename):
        map.append(line.strip())
    return map

def in_range(map, x, y):
    return x in range(len(map)) and y in range(len(map[0]))

def rotate(dx, dy):
    # from up to right
    if dx == -1:
        return 0, 1
    # from right to down
    if dy == 1:
        return 1, 0
    # from down to left
    if dx == 1:
        return 0, -1
    # from left to up
    if dy == -1:
        return -1, 0
    
def walk(map, x, y, dx, dy):
    visited = set()
    while in_range(map, x, y):
        while in_range(map, x, y) and map[x][y] != '#':
            visited.add((x, y))
            x += dx
            y += dy
        
        if not in_range(map, x, y):
            break
        x, y = x - dx, y - dy
        dx, dy = rotate(dx, dy)
    return visited


def get_starting_point(map):
    x, y = 0, 0
    dx, dy = 0, 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            temp = map[i][j]
            if temp == '^':
                dx = -1
                x, y = i, j
            if temp == 'v':
                dx = 1
                x, y = i, j
            if temp == '<':
                dy = -1
                x, y = i, j
            if temp == '>':
                dy = 1
                x, y = i, j
    return x, y, dx, dy

def part1(filename):
    map = data(filename)
    x, y, dx, dy = get_starting_point(map)
        
    visited = walk(map, x, y, dx, dy)

    print("Part 1 for ", filename, " is ", len(visited))



def part2(filename):
    def is_cycle_with_new_stone(map, x, y, dx, dy, maxmoves):
        moves = 0
        while in_range(map, x, y):
            while in_range(map, x, y) and map[x][y] != '#':
                moves += 1
                if moves >= 2*maxmoves:
                    return True

                x += dx
                y += dy
            
            if not in_range(map, x, y):
                break
            x, y = x - dx, y - dy
            dx, dy = rotate(dx, dy)

        return False
    
    map = data(filename)
    x, y, dx, dy = get_starting_point(map)

    visited = walk(map, x, y, dx, dy)

    res = 0
    for psx, psy in list(visited):
        currx, curry = x, y
        currdx, currdy = dx, dy

        # Setting a wall in one of the visited points
        tempmap = map.copy()
        tempmap[psx] = tempmap[psx][:psy] + '#' + tempmap[psx][psy+1:]

        if is_cycle_with_new_stone(tempmap, currx, curry, currdx, currdy, len(visited)):
            res += 1
        
    print("Part 2 for ", filename, " is ", res)

    

part1("data/6demo.txt")
part1("data/6.txt")

part2("data/6demo.txt")
part2("data/6.txt")

        
    







