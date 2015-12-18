#Written for Python 3.4.2
import copy

lights = [[0]*100 for x in range(100)]

with open("input.txt", "r") as f:
    for x, y, c in ((x, y, c) for x, line in enumerate(f) for y, c in enumerate(line)):
        if c == '#':
            lights[x][y] = 1 

def getNeighbors(lights, x, y):
    positions = [(x-1, y-1), (x-1, y), (x-1, y+1),
                 (x, y-1),             (x, y+1),
                 (x+1, y-1), (x+1, y), (x+1, y+1)]
    
    neighbors = 0
    for nx, ny in positions:
        if 0 <= nx < len(lights) and 0 <= ny < len(lights[0]):
            neighbors += lights[nx][ny]
    return neighbors

def step(lights, stuck = []):
    snapshot = copy.deepcopy(lights)
    for x, y, s in ((x, y, s) for x, row in enumerate(snapshot) for y, s in enumerate(row)):
        if (x, y) in stuck: continue
        neighbors = getNeighbors(snapshot, x, y)
        if s == 1:
            if neighbors not in [2, 3]:
                lights[x][y] = 0
        else:
            if neighbors == 3:
                lights[x][y] = 1
    return lights

part1 = copy.deepcopy(lights)
for _ in range(100):
    part1 = step(part1)

print(sum(map(sum, part1)))

stuck = [(0            , 0), (0            , len(lights[0])-1),
         (len(lights)-1, 0), (len(lights)-1, len(lights[0])-1)]

part2 = copy.deepcopy(lights)
for x, y in stuck:
    part2[x][y] = 1
    
for _ in range(100):
    part2 = step(part2, stuck)

print(sum(map(sum, part2)))
