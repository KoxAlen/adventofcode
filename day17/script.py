#Written for Python 3.4.2

containers = []
with open("input.txt", "r") as f:
    for ins in f:
        containers.append(int(ins))

def permutations(containers, eggnog):
    for i in range(len(containers)):
        if containers[i] <= eggnog:
            yield from([containers[i]]+x for x in permutations(containers[i+1:], eggnog-containers[i]))
    yield []

eggnog = 150
solutions = [x for x in permutations(containers, eggnog) if sum(x) == eggnog]
print(len(solutions))

ncontainers = list(map(len, solutions))
print(len([x for x in ncontainers if x == min(ncontainers)]))
