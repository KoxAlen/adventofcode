#Written for Python 3.4.2
import re

matcher = re.compile(r"Sue (\d+): ([a-z]+): (\d+), ([a-z]+): (\d+), ([a-z]+): (\d+)")
aunts = dict()

with open("input.txt", "r") as f:
    for aunt in f:
        n, trait1, c1, trait2, c2, trait3, c3 = matcher.match(aunt).groups()
        aunts[n] = {trait1: int(c1), trait2: int(c2), trait3: int(c3)}

MFCSAM =\
"""
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
"""
traits = re.findall(r"([a-z]+): (\d+)", MFCSAM)

def sample_likelihood(aunt, traits):
    score = 0
    for trait, c in traits:
        if trait in aunt:
            if aunt[trait] == int(c):
                score += 1
    return score

def retroencabulator_induced_likelihood(aunt, traits):
    score = 0
    for trait, c in traits:
        if trait in aunt:
            c = int(c)
            if trait in ["cats", "trees"]:
                if aunt[trait] > c:
                    score += 1
            elif trait in ["pomeranians", "goldfish"]:
                if aunt[trait] < c:
                    score += 1
            else:
                if aunt[trait] == c:
                    score += 1
    return score

print(max(aunts.keys(), key=lambda k: sample_likelihood(aunts[k], traits)))
print(max(aunts.keys(), key=lambda k: retroencabulator_induced_likelihood(aunts[k], traits)))
