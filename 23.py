import networkx as nx

graph = nx.Graph()

for i in open("data/23.txt"):
    source, dest = i.strip().split("-")
    graph.add_edge(source, dest)


def part1():
    count = 0
    for c in nx.simple_cycles(graph, 3):
        if c[0].startswith("t") or c[1].startswith("t") or c[2].startswith("t"):
            count += 1
    print("Part 1 is ", count)


def part2():
    print("Part 2 is ", ",".join(sorted(max(list(nx.find_cliques(graph)), key=len))))


part1()
part2()
