#Written for Python 3.4.2
import re

with open("input.txt", "r") as f:
    data = list(f)

matcher = re.compile(r"(\S+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.")

reindeers = dict()

for ins in data:
    reindeer, speed, endurance, cooldown = matcher.match(ins).groups()
    reindeers[reindeer] = (int(speed), int(endurance), int(cooldown))

def reindeerPos(reindeer, time):
    speed, endurance, cooldown = reindeer
    cycle = endurance + cooldown
    steps, delta = divmod(time, cycle)
    return (steps*endurance + min(delta, endurance)) * speed

def leadersAt(reindeers, time):
    positions = dict()
    for reindeer in reindeers:
        positions[reindeer] = reindeerPos(reindeers[reindeer], time)
    pos = max(positions.values())
    return [(k, pos) for k in positions if positions[k] >= pos]

duration = 2503
print(leadersAt(reindeers, duration))

scores = dict()
for k in reindeers:
    scores[k] = 0
for t in range(1, duration+1):        
    leaders = leadersAt(reindeers, t)
    for reindeer, _ in leaders:
        scores[reindeer] += 1

winner = max(scores.keys(), key=lambda k: scores[k])
print(winner, scores[winner])
