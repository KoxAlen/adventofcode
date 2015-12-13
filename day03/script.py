#Written for Python 3.4.2

data = [c for c in open("input.txt").readline()]
def move(moves):
    def step(house, d):
        x,y = house
        return {'^':(x,y+1),'v':(x,y-1),
                '>':(x+1,y),'<':(x-1,y)}[d]
    
    house = (0,0)
    visited = set([house])
    for d in moves:
        house = step(house, d)
        visited.add(house)

    return visited

print(len(move(data)))
print(len(move(data[::2]) | move(data[1::2])))
