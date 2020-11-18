import Crypto.Util.number
import random
import math
import sys

from wolframclient.evaluation import WolframLanguageSession
session=WolframLanguageSession()
from wolframclient.language import wl, wlexpr

#pip install pycryptodome is needed

bitsOptions = [40, 41, 42, 43, 44]

if (len(sys.argv)>1):
        bits=int(sys.argv[1])

p=Crypto.Util.number.getPrime(bitsOptions[random.randint(0, 4)], randfunc=Crypto.Random.get_random_bytes)
q=Crypto.Util.number.getPrime(bitsOptions[random.randint(0, 4)], randfunc=Crypto.Random.get_random_bytes)

while len(str(p)) != 13 or len(str(q)) != 13:
    if len(str(p)) != 13:
        p=Crypto.Util.number.getPrime(bitsOptions[random.randint(0, 4)], randfunc=Crypto.Random.get_random_bytes)
    elif len(str(q)) != 13:
        q=Crypto.Util.number.getPrime(bitsOptions[random.randint(0, 4)], randfunc=Crypto.Random.get_random_bytes)

print ("\nRandom n-bit Prime (p): ",p, len(str(p)))
print ("\nRandom n-bit Prime (q): ",q, len(str(q)))

n = p * q
print("Value of n (p * q) ", n, len(str(n)))

phiN = (p - 1) * (q - 1)
print("Value of phiN (p - 1) * (q - 1) ", phiN, len(str(phiN)))

e = random.randint(2, phiN + 1)
while math.gcd(e, phiN) != 1:
    e = random.randint(2, phiN - 1)

print("Value of e ", e, len(str(e)))

d = Crypto.Util.number.inverse(e, phiN)

print("Value of d ", d, len(str(d)))

def Encrypt():
    text = "Ahoj pepo jak se máš?"

    OT = []
    ST = []
    c = 0
    parts = -1

    for i in range(len(text)):
        if c % 5 == 0 or i == 0:
            OT.append([])
            parts += 1
            c += 1
            OT[parts].append('{0:012b}'.format(ord(text[i])))
        else:
            OT[parts].append('{0:012b}'.format(ord(text[i])))
            c += 1

    for i in range(len(OT)):
        for j in range(len(OT[i])):
            if j != 0:
                OT[i][0] += OT[i][j]
    
    for i in range(len(OT)):
        while len(OT[i]) != 1:
            OT[i].remove(OT[i][-1])
        OT[i][0] = int(OT[i][j], 2)

    for i in range(len(OT)):
        ST.append(session.evaluate(wl.PowerMod(OT[i][0], e, n)))
    session.terminate()

    print("OT: ",OT)
    print("ST: ",ST)
    return(ST)
Encrypt()