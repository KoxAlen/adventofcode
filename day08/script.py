#Written for Python 3.4.2

import re

data =  [line.rstrip('\n') for line in open("input.txt")]
nCharCode = 0
nCharMem = 0
nCharEscaped = 0
for line in data:
    nCharCode += len(line)
    nCharMem += len(re.sub(r"\\x[a-f0-9]{2}", "U", line[1:-1].replace("\\\"", "Q").replace("\\\\", "S")))
    nCharEscaped += len(re.escape(line))+2

print(nCharCode - nCharMem)
print(nCharEscaped - nCharCode)
