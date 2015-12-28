#Written for Python 3.4.2
import itertools
import functools
import operator

with open("input.txt", "r") as f:
    weights = [int(l.strip()) for l in f]

def balance(containers):
    split_size = sum(weights) // containers
    for i in range(len(weights)):
        QE = [functools.reduce(operator.mul, comb)
              for comb in itertools.combinations(weights, i)
              if sum(comb) == split_size]
        if len(QE) > 0:
            return min(QE)
#Part1
print(balance(3))
#Part2
print(balance(4))
