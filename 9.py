dotset = set(".")


def getdata(filename):
    numtext = ""
    for line in open(filename, "r"):
        numtext += line.strip()
    data = []
    idx = 0
    while idx < len(numtext):
        if len(numtext) - idx == 1:
            data.append([numtext[idx], 0])
            break
        else:
            data.append([numtext[idx], numtext[idx + 1]])
            idx += 2
    print(data)
    return data


def part1(filename):
    data = getdata(filename)
    temp = []
    idx = 0
    for d in data:
        block, space = int(d[0]), 0 if len(d) == 1 else int(d[1])
        for i in range(block):
            temp.append(str(idx))
        for i in range(space):
            temp.append(".")
        idx += 1

    def getnextinsertfrom(curr, temp):
        idx = curr
        while idx >= 0:
            if set(temp[idx]) != dotset:
                return idx, temp[idx]
            idx -= 1

    def getnextinsertat(curr, temp):
        idx = curr
        while idx < len(temp):
            if set(temp[idx]) == dotset:
                return idx
            idx += 1

    insertfrom, insertfromval = getnextinsertfrom(len(temp) - 1, temp)
    insertat = getnextinsertat(0, temp)

    while insertat < insertfrom:
        temp[insertat] = insertfromval
        temp[insertfrom] = "."
        insertfrom, insertfromval = getnextinsertfrom(insertfrom, temp)
        insertat = getnextinsertat(insertat, temp)

    res = 0
    for idx in range(len(temp)):
        if set(temp[idx]) == dotset:
            continue
        else:
            res += idx * int(temp[idx])
    print("Part 1 for", filename, "is", res)


def joinzeros(temp):
    newtemp = []
    tempdots = ""
    for t in temp:
        if set(t) == dotset:
            tempdots += t
        else:
            if len(tempdots) > 0:
                newtemp.append(tempdots)
                tempdots = ""
            newtemp.append(t)
    if len(tempdots) > 0:
        newtemp.append(tempdots)

    return newtemp


def part2(filename):
    data = getdata(filename)
    temp = []
    idx = 0
    for d in data:
        block, space = int(d[0]), 0 if len(d) == 1 else int(d[1])
        temp.append(block * str(idx))
        if space > 0:
            temp.append(space * ".")
        idx += 1

    # Getting values to remove in reverse order
    toremove = []
    for i in range(len(temp) - 1, -1, -1):
        if set(temp[i]) != dotset:
            toremove.append(temp[i])

    for remove in toremove:
        # Recalculating index since it might have changed
        i = temp.index(remove)
        curr = remove
        spaceneeded = len(curr)

        for j in range(0, i):
            freespace = len(temp[j])
            # if current space is dots only and length is greater than or equal to space needed
            if set(temp[j]) == dotset and freespace >= spaceneeded:
                leftoverspace = freespace - spaceneeded
                # set the newplace to the current value
                temp[j] = curr
                # set the old place to dots * length
                temp[i] = spaceneeded * "."
                # if we have leftover space, insert it after the newplace
                if leftoverspace > 0:
                    temp.insert(j + 1, leftoverspace * ".")

                # Joing all consecutive dots together
                temp = joinzeros(temp)

                break
    print("".join(temp))

    res = 0
    temp = "".join(temp)
    for idx in range(len(temp)):
        if set(temp[idx]) == dotset:
            continue
        else:
            res += idx * int(temp[idx])
    print("Part 2 for", filename, "is", res)


# part1("data/9demo.txt")
# part1("data/9.txt")

part2("data/9demo.txt")
# part2("data/9.txt")
