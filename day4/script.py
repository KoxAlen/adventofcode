import hashlib

def genNext(crypto, number):
    crypto.update(str(number).encode())
    return crypto.hexdigest()
    

key = b"bgvyzdsv"
md5 = hashlib.md5()
md5.update(key)

number = 1
digest = genNext(md5.copy(), number)
while not digest.startswith("00000"):
    number += 1
    digest = genNext(md5.copy(), number)

print(digest, "|", number)

while not digest.startswith("000000"):
    number += 1
    digest = genNext(md5.copy(), number)

print(digest, "|", number)


