import functools


def mix(secret_num, val):
    return int(secret_num ^ val)


def prune(secret_num):
    return secret_num % 16777216


@functools.lru_cache(maxsize=None)
def evolve(secret_num):
    res = secret_num * 64
    secret_num = mix(secret_num, res)
    secret_num = prune(secret_num)
    res = int(secret_num / 32)
    secret_num = mix(secret_num, res)
    secret_num = prune(secret_num)
    res = secret_num * 2048
    secret_num = mix(secret_num, res)
    secret_num = prune(secret_num)

    return secret_num


def diff(inlist):
    return [inlist[i + 1] - inlist[i] for i in range(len(inlist) - 1)]


vals = [int(i.strip()) for i in open("data/22.txt").readlines()]
d = {}
part1res = 0
for v in vals:
    changes = [int(str(v)[-1])]

    for i in range(2000):
        v = evolve(v)
        changes.append(int(str(v)[-1]))

    part1res += v
    diffchanges = diff(changes)

    locald = {}

    for i in range(0, len(diffchanges) - 4 + 1):
        sequence = diffchanges[i : i + 4]
        money = changes[i + 4]
        tuplesequence = tuple(sequence)
        if tuplesequence in locald:
            continue
        else:
            locald[tuplesequence] = money

    for k, v in locald.items():
        if k in d:
            d[k] += v
        else:
            d[k] = v


print("Part 1 is ", part1res)
max_key = max(d, key=d.get)
maxval = d[max_key]
print("Part 2 is ", maxval, "for", max_key)
