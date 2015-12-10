#Written for Python 3.4.2

from itertools import groupby

data = "3113322113"

def elvesLookElvesSay(sequence):
    return "".join([str(len(list(g)))+k for k, g in groupby(sequence)])

t = data[:]

part1 = 40
for i in range(part1):
    t = elvesLookElvesSay(t)

print(len(t))

part2 = 50
for i in range(part2-part1):
    t = elvesLookElvesSay(t)

print(len(t))


    
