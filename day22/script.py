#Written for Python 3.4.2
from collections import defaultdict

spells = {
    "Magic Missile": {"cost": 53,  "damage": 4, "heal": 0, "armor": 0,
                      "turns": 0, "mana": 0},
    "Drain":         {"cost": 73,  "damage": 2, "heal": 2, "armor": 0,
                      "turns": 0, "mana": 0},
    "Shield":        {"cost": 113, "damage": 0, "heal": 0, "armor": 7,
                      "turns": 6, "mana": 0},
    "Poison":        {"cost": 173, "damage": 3, "heal": 0, "armor": 0,
                      "turns": 6, "mana": 0},
    "Recharge":      {"cost": 229, "damage": 0, "heal": 0, "armor": 0,
                      "turns": 5, "mana": 101}
}

class GameState():
    def __init__(self, player_hp, player_mana, boss_hp, boss_dmg, hard_mode, spent = 0, timers = defaultdict(int), actions = []):
        self.player_hp = player_hp
        self.player_mana = player_mana
        self.boss_hp = boss_hp
        self.boss_dmg = boss_dmg
        self.hard_mode = hard_mode
        self.spent = spent
        self.timers = timers
        self.actions = actions
    def __str__(self):
        return "%d: %s" % (self.spent, self.actions)
    def copy(self):
        return GameState(self.player_hp, self.player_mana, self.boss_hp, self.boss_dmg, self.hard_mode, self.spent, self.timers.copy(), self.actions[:])
    def turn(self, spell):
        #Player turn
        if self.hard_mode:
            self.player_hp -= 1
            if self.player_hp <= 0:
                return 2 #Loss
        for effect in self.timers:
            if self.timers[effect] > 0:
                self.timers[effect] -= 1
                self.boss_hp -= spells[effect]["damage"]
                self.player_mana += spells[effect]["mana"]
        if self.boss_hp <= 0:
            return 1 #Win
        
        self.actions.append(spell)
        self.spent += spells[spell]["cost"]
        self.player_mana -= spells[spell]["cost"]
        if spells[spell]["turns"] > 0:
            self.timers[spell] = spells[spell]["turns"]
        else:
            self.boss_hp -= spells[spell]["damage"]
            self.player_hp += spells[spell]["heal"]

        #Boss turn
        armor = 0
        for effect in self.timers:
            if self.timers[effect] > 0:
                self.timers[effect] -= 1
                self.boss_hp -= spells[effect]["damage"]
                self.player_mana += spells[effect]["mana"]
                armor += spells[effect]["armor"]
        if self.boss_hp <= 0:
            return 1 #win
        self.player_hp -= max(1, self.boss_dmg - armor)
        if self.player_hp <= 0:
            return 2 #Loss
        return 0 #continue
    def getNextSpells(self):
        mana = self.player_mana #Calculate mana on next round
        for effect in self.timers:
            if self.timers[effect] >0:
                mana += spells[effect]["mana"]
        for spell in spells:
            if self.timers[spell] > 1: #Effect still active
                continue
            if spells[spell]["cost"] > mana: #Not enough mana
                continue
            yield spell

def bfs_gameStates(player, boss, hard_mode=False):
    player_hp, player_mana = player
    boss_hp, boss_dmg = boss
    bfs = []
    bfs.append(GameState(player_hp, player_mana, boss_hp, boss_dmg, hard_mode))
    best = bfs[-1].copy()
    best.spent = float("inf")
    while len(bfs) > 0:
        prevState = bfs.pop()
        if prevState.spent >= best.spent:
            continue
        for spell in prevState.getNextSpells():
            newState = prevState.copy()
            result = newState.turn(spell)
            if result == 0:
                bfs.append(newState)
            elif result == 1:
                if newState.spent < best.spent:
                    best = newState
    return best

player = (50, 500)
boss = (55, 8) #Input
#Part 1
print(bfs_gameStates(player, boss))
#Part 2
print(bfs_gameStates(player, boss, hard_mode=True))
