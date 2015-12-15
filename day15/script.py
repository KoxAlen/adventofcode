#Written for Python 3.4.2
import re
import itertools
import operator

matcher = re.compile(r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)")
ingredients = dict()

with open("input.txt", "r") as f:
    for ins in f:
        name, cap, dur, flavor, texture, cal = matcher.match(ins).groups()
        ingredients[name] = (int(cap), int(dur), int(flavor), int(texture), int(cal))

def cookie_score(cookie):
    partial_scores = [[part[0]*v for v in ingredients[part[1]]] for part in cookie]
    scores = [0]*len(partial_scores[0])
    for i in range(len(partial_scores[0])):
        scores[i] = max(0, sum([x[i] for x in partial_scores]))
    return scores, list(itertools.accumulate(scores[:-1], operator.mul))[-1]

def recipes(MAX, n):
    if n==1:
        yield [MAX]
    else:
        yield from([ing]+recipe for ing in range(MAX+1) for recipe in recipes(MAX-ing, n-1))


cookie_weight = 100
names = list(ingredients.keys())

max_score = 0
max_cookie = None
for recipe in recipes(cookie_weight, len(ingredients)):
    cookie = []
    for i in range(len(recipe)):
        cookie.append((recipe[i], names[i]))
    _, score = cookie_score(cookie)
    if score > max_score:
        max_score = score
        max_cookie = cookie
print(max_score, max_cookie)

max_score = 0
max_cookie = None
for recipe in recipes(cookie_weight, len(ingredients)):
    cookie = [(recipe[i], names[i]) for i in range(len(recipe))]
    totals, score = cookie_score(cookie)
    if totals[-1] != 500:
        continue
    if score > max_score:
        max_score = score
        max_cookie = cookie
print(max_score, max_cookie)
