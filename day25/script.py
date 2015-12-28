#Written for Python 3.4.2

def index(row, col):
    N = row+col - 2
    Tn = (N*(N+1))//2 #Triangular number
    return Tn + col-1 

def calculate(seed, row, col, base=252533, modulo=33554393):
    return pow(base, index(row, col), modulo)*seed % modulo
seed = 20151125
print(calculate(seed, 2981, 3075)) #Input row=2981, col=3075
