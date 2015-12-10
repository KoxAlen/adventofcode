#Written for Python 3.4.2

import re

data =  [line.rstrip('\n') for line in open("input.txt")]

matcher = re.compile(r"(turn on|turn off|toggle) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)")
lights = [[0 for i in range(1000)] for j in range(1000)]
brightness = [[0 for i in range(1000)] for j in range(1000)]

def turn(mode, xs, ys, xe, ye):
    for i in range(xs, xe+1):
        for j in range(ys, ye+1):
            lights[i][j] = mode

def toggle(xs, ys, xe, ye):
    for i in range(xs, xe+1):
        for j in range(ys, ye+1):
            lights[i][j] ^= 1

def control(dif, xs, ys, xe, ye):
    for i in range(xs, xe+1):
        for j in range(ys, ye+1):
            brightness[i][j] = max(brightness[i][j]+dif, 0)

for ins in data:
    m = matcher.match(ins)
    action = m.group(1)
    xs = int(m.group(2))
    ys = int(m.group(3))
    xe = int(m.group(4))
    ye = int(m.group(5))
    if action == "turn on":
        turn(1, xs, ys, xe, ye)
        control(1, xs, ys, xe, ye)
    elif action == "turn off":
        turn(0, xs, ys, xe, ye)
        control(-1, xs, ys, xe, ye)
    else:
        toggle(xs, ys, xe, ye)
        control(2, xs, ys, xe, ye)
    
print(sum(map(sum,lights)))
print(sum(map(sum,brightness)))
