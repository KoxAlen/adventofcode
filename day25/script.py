#Written for Python 3.4.2

def index(row, col):
    return (row+col-2)*(row+col-1)//2+col

def calculate(seed, row, col, base=252533, modulo=33554393):
    return pow(base, index(row, col)-1, modulo)*seed % modulo
seed = 20151125
print(calculate(seed, 2981, 3075)) #Input row=2981, col=3075
