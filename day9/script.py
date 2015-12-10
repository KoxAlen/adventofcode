#Written for Python 3.4.2

import re
import itertools 

data =  [line.rstrip('\n') for line in open("input.txt")]

matcher = re.compile(r"([A-Za-z]+) to ([A-Za-z]+) = ([0-9]+)")

nodes = set()
distances = dict()

for entry in data:
    node1, node2, distance = matcher.match(entry).groups()

    nodes.add(node1)
    nodes.add(node2)

    distances.setdefault(node1, dict())[node2] = int(distance)
    distances.setdefault(node2, dict())[node1] = int(distance)

shortest = float("inf")
longest = 0
for p in itertools.permutations(nodes):
    dist = sum(map(lambda n1, n2: distances[n1][n2], p[:-1], p[1:]))
    shortest = min(shortest, dist)
    longest = max(longest, dist)

print(shortest)
print(longest)
