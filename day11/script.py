#Written for Python 3.4.2

data =  "hxbxwxba"

blacklist = [ord(x) for x in ["i", "o", "l"]]

def nextPassword(seed):
    lb = ord('a')
    ub = ord('z')
    def increase(l, p = 0):
        try:
            c = l[p]+1
        except IndexError:
            return
        while c in blacklist:
            c += 1
        if c > ub:
            c = lb
            increase(l, p+1)
        l[p] = c
        
    out = list(map(ord, seed))
    out.reverse()
    increase(out)
    out.reverse()
    return ''.join(map(chr,out))

def elfCheck(password):
    p = list(map(ord, password))
    pairs = 0
    increase = False
    for i in range(len(p)):
        if p[i] in blacklist:
            return False
        try:
            if not pairs >= 2 and p[i] == p[i+1] and p[i-1] != p[i]:
                pairs += 1
            if not increase and p[i+1] == p[i]+1 and p[i+2] == p[i]+2:
                increase = True
        except IndexError:
            pass
    return (pairs >= 2) & increase

password = data[:]
while not elfCheck(password):
    password = nextPassword(password)

print(password) #part1

password = nextPassword(password)
while not elfCheck(password):
    password = nextPassword(password)

print(password) #part2
