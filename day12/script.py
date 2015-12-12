#Written for Python 3.4.2
import re

with open("input.txt", "r") as f:
    data = f.read()

count = sum(map(int, re.findall(r"(-?[0-9]+)", data)))

print(count)

import json

obj = json.loads(data)

def elfCount(obj):
    if type(obj) == dict:
        if "red" in obj.values():
            return 0
        return sum(map(elfCount, obj.values()))
    if type(obj) == list:
        return sum(map(elfCount, obj))
    if type(obj) == int:
        return obj

    return 0

print(elfCount(obj))
