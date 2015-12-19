#Written for Python 3.4.2
from collections import defaultdict

replacements = dict()
with open("input.txt", "r") as f:
    for line in f:
        r = line.strip().split(" => ")
        if len(r) == 2:
            replacements.setdefault(r[0], list()).append(r[1])
        else:
            if r[0] != '':
                target = r[0]

def next_step(replacements, molecule):
    result = set()
    for i, m in enumerate(molecule):
        if m in replacements:
            for r in replacements[m]:
                result.add("%s%s%s" %(molecule[:i], r, molecule[i+1:]))
        else:
            try:
                mm = m+molecule[i+1]
            except IndexError:
                break
            if mm in replacements:
                for r in replacements[mm]:
                    result.add("%s%s%s" %(molecule[:i], r, molecule[i+2:]))
    return result

print(len(next_step(replacements, target)))

def lookup(grammar):
    result = dict()
    for k in grammar:
        for t in grammar[k]:
            result[t] = k
    return result
def reduce(grammar, start, string):
    r_lookup = lookup(grammar)
    t = sorted(r_lookup.keys(), key=lambda n: len(n), reverse=True)
    trans = []
    while string != start:
        for h in t:
            if string == start:
                break
            if h in string:
                trans.append(r_lookup[h])
                string = string.replace(h, r_lookup[h], 1)
    return list(reversed(trans))

print(len(reduce(replacements, "e", target)))
