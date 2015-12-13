#Written for Python 3.4.2
import re
import itertools

with open("input.txt", "r") as f:
    data = list(f)

nodes = dict()
matcher = re.compile(r"([A-Za-z]+)\s.*(gain|lose) ([0-9]+).*to ([A-Za-z]+)")
for ins in data:
    node1, action, value, node2 = matcher.match(ins).groups()
    value = int(value)
    if action == "lose":
        value *= -1
    nodes.setdefault(node1, dict())[node2] = value

def calc_happiness():
    happiness = 0
    for state in itertools.permutations(nodes):
        happiness = max(happiness,
                        sum([nodes[state[i]][state[(i+1)%len(state)]] +
                             nodes[state[i]][state[i-1]]
                             for i in range(len(state))]))
    return happiness

print(calc_happiness())

for k in list(nodes.keys()):
    nodes.setdefault("me", dict())[k] = 0
    nodes[k]["me"] = 0

print(calc_happiness())

