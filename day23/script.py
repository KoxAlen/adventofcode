#Written for Python 3.4.2
import re

code = []
with open("input.txt", "r") as f:
    matcher = re.compile(r"([a-z]{3})\s*(?:([ab]))?(?:,?\s*([+-]\d+))?")
    for l in f:
        opcode, reg, offset = matcher.match(l).groups()
        if offset:
            offset = int(offset)
        code.append((opcode, reg, offset))

def half(r, _):
    regs[r] //= 2
    return 1
def triple(r, _):
    regs[r] *= 3
    return 1
def increment(r, _):
    regs[r] += 1
    return 1
def jump(_, offset):
    return offset
def jump_if_even(r, offset):
    if regs[r] % 2 == 0:
        return offset
    return 1
def jump_if_one(r, offset):
    if regs[r] == 1:
        return offset
    return 1
ops = {
    "hlf": half,
    "tpl": triple,
    "inc": increment,
    "jmp": jump,
    "jie": jump_if_even,
    "jio": jump_if_one
}  

def run():
    pc = 0
    try:
        while True:
            ins = code[pc]
            pc += ops[ins[0]](ins[1], ins[2]) 
    except IndexError:
        pass

#Part 1
regs = {"a": 0, "b": 0}
run()
print(regs["b"])
#Part 2
regs = {"a": 1, "b": 0}
run()
print(regs["b"])
