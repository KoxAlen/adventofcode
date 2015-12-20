#Written for Python 3.4.2
import random

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
    t = list(r_lookup.keys())
    trans = []
    tmp = string
    while tmp != start:
        prev = tmp
        for h in t:
            if tmp == start:
                break
            if h in tmp:
                trans.append(r_lookup[h])
                tmp = tmp.replace(h, r_lookup[h], 1)
        if prev == tmp:
            print("Stuck on %s" % tmp)
            random.shuffle(t)
            tmp = string
            trans = []
            print("Randomize and retry")
    return list(reversed(trans))

def askalski_solution(string):
    """
    Solution based on the properties of the grammar
    https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju
    Even though my solution works (at least for my input) I found this interesting"""
    t = 0
    i = 0
    while i < len(string):
        try:
            if string[i+1].islower():
                i += 1
        except IndexError:
            pass
        i += 1
        t += 1
    par = string.count("Rn") + string.count("Ar")
    sep = string.count("Y")
    return t - par - sep*2 -1

print("Askalski solution: %d" % askalski_solution(target))

print(len(reduce(replacements, "e", target)))
