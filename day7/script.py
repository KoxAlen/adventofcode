#Written for Python 3.4.2

import functools
data =  [line.rstrip('\n') for line in open("input.txt")]

wires = dict()
operator = {"AND": lambda x, y: x & y,
            "OR": lambda x, y: x | y,
            "LSHIFT": lambda x, y: x << y,
            "RSHIFT": lambda x, y: x >> y,
            "NOT": lambda x: ~x}

for ins in data:
    value, wire = [x.strip() for x in ins.split("->")]
    wires[wire] = value.split()

@functools.lru_cache(maxsize=None)
def resolve(wire):
    try:
        return int(wire)
    except ValueError:
        pass
    value = wires[wire]
    if len(value) == 1:
        return resolve(value[0])
    elif len(value) == 2:
        return operator[value[0]](resolve(value[1]))
    else:
        return operator[value[1]](resolve(value[0]), resolve(value[2]))

wire_a = resolve("a")
print(wire_a) #part 1
wires["b"] = [wire_a]
resolve.cache_clear()
print(resolve("a")) #part 2
