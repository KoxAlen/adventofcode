#Written for Python 3.4.2

data =  [line.rstrip('\n') for line in open("input.txt")]
totalpaper = 0
totalribbon = 0
for present in data:
    dimensions = sorted([int(x) for x in present.split('x')])
    f1 = dimensions[0]*dimensions[1]
    f2 = dimensions[1]*dimensions[2]
    f3 = dimensions[2]*dimensions[0]
    extra = min(f1,f2,f3)
    wraplenght = 2*(dimensions[0]+dimensions[1])
    bow = dimensions[0]*dimensions[1]*dimensions[2]
    totalpaper += 2*(f1+f2+f3)+extra
    totalribbon += wraplenght+bow
    
print(totalpaper)
print(totalribbon)
    
