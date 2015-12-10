#Written for Python 3.4.2

data =  [line.rstrip('\n') for line in open("input.txt")]
blacklist = ["ab", "cd", "pq", "xy"]
vowels = ['a', 'e', 'i', 'o', 'u']

def contains(string, samples):
    for sample in samples:
        if string.find(sample) > -1:
            return True
    return False

def isNicePart1(string):
    if contains(string, blacklist):
        return False
    
    vowelcount = 0
    for vowel in vowels:
        vowelcount += string.count(vowel)
    if vowelcount < 3:
        return False

    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

def isNicePart2(string):
    for i in range(len(string)-3):
        pair = string[i]+string[i+1]
        if string.find(pair, i+2) > -1:
            for j in range(len(string)-2):
                if string[j] == string[j+2]:
                    return True
            return False
    return False

nicePart1Count = 0
nicePart2Count = 0
for string in data:
    if isNicePart1(string):
        nicePart1Count += 1
    if isNicePart2(string):
        nicePart2Count += 1

print(nicePart1Count)
print(nicePart2Count)

#Test cases part1
##print(isNicePart1("ugknbfddgicrmopn"), True)
##print(isNicePart1("aaa"), True)
##print(isNicePart1("jchzalrnumimnmhp"), False)
##print(isNicePart1("haegwjzuvuyypxyu"), False)
##print(isNicePart1("dvszwmarrgswjxmb"), False)

#Test cases part1
##print(isNicePart2("qjhvhtzxzqqjkmpb"), True)
##print(isNicePart2("xxyxx"), True)
##print(isNicePart2("uurcxstgmygtbstg"), False)
##print(isNicePart2("ieodomkazucvgmuy"), False)
