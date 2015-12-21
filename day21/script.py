#Written for Python 3.4.2
import re
import itertools
from math import ceil

shop_re = re.compile(r"(\w+ [\+\d]{0,2})\s*(\d+)\s*(\d+)\s*(\d+)")

_weapons_shop =\
"""
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
"""
weapons_shop = dict()
for item, cost, damage, defense in shop_re.findall(_weapons_shop):
    weapons_shop[item] = (int(cost), int(damage), int(defense))

_armor_shop =\
"""
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
"""
armor_shop = dict()
for item, cost, damage, defense in shop_re.findall(_armor_shop):
    armor_shop[item] = (int(cost), int(damage), int(defense))
armor_shop["empty"] = (0,0,0)

_rings_shop =\
"""
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""
rings_shop = dict()
for item, cost, damage, defense in shop_re.findall(_rings_shop):
    rings_shop[item] = (int(cost), int(damage), int(defense))
rings_shop["empty1"] = (0,0,0)
rings_shop["empty2"] = (0,0,0)

boss = (100, 8, 2) #input
base_hp = 100

def ttk(enemy, attacker):
    dmg = max(1, attacker[1]-enemy[2])
    return ceil(enemy[0]/dmg)

best = float("inf")
gear = []
for weapon in weapons_shop:
    for armor in armor_shop:
        for r1, r2 in itertools.combinations(rings_shop, 2):            
            cost = weapons_shop[weapon][0] + armor_shop[armor][0] + rings_shop[r1][0] + rings_shop[r2][0]
            damage = weapons_shop[weapon][1] + armor_shop[armor][1] + rings_shop[r1][1] + rings_shop[r2][1]
            defense = weapons_shop[weapon][2] + armor_shop[armor][2] + rings_shop[r1][2] + rings_shop[r2][2]
            player = (base_hp, damage, defense)
            if ttk(boss, player) <= ttk(player, boss):
                if cost < best:
                    best = cost
                    gear = [weapon, armor, r1, r2]
print(best, gear)

best = 0
gear = []
for weapon in weapons_shop:
    for armor in armor_shop:
        for r1, r2 in itertools.combinations(rings_shop, 2):            
            cost = weapons_shop[weapon][0] + armor_shop[armor][0] + rings_shop[r1][0] + rings_shop[r2][0]
            damage = weapons_shop[weapon][1] + armor_shop[armor][1] + rings_shop[r1][1] + rings_shop[r2][1]
            defense = weapons_shop[weapon][2] + armor_shop[armor][2] + rings_shop[r1][2] + rings_shop[r2][2]
            player = (base_hp, damage, defense)
            if ttk(boss, player) > ttk(player, boss):
                if cost > best:
                    best = cost
                    gear = [weapon, armor, r1, r2]
print(best, gear)
