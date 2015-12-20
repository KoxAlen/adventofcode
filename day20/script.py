#Written for Python 3.4.2
import functools
import itertools
from math import sqrt

puzzle_input = 33100000

def integer_factorization(n):
    return set(functools.reduce(list.__iadd__, ([i, n//i] for i in range(1, int(sqrt(n))+1) if n % i == 0)))

def elfHouses():
    for i in itertools.count(start=1):
        elfs = integer_factorization(i)
        presents = sum(elfs)*10
        lazy_presents = sum([n for n in elfs if i <= n*50])*11
        yield i, presents, lazy_presents

part1 = False
part2 = False
for house, presents, lazy_presents in elfHouses():
    if not part1 and presents >= puzzle_input:
        print("Part 1", house, presents)
        part1 = True
    if not part2 and lazy_presents >= puzzle_input:
        print("Part 2", house, lazy_presents)
        part2 = True
    if part1 and part2: break
