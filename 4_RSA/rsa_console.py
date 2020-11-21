import Crypto.Util.number
import random
import math
import sys

from wolframclient.evaluation import WolframLanguageSession
session=WolframLanguageSession()
from wolframclient.language import wl, wlexpr

#pip install pycryptodome is needed

class Cipher:

    def __init__(self, name, message, p = None, q = None, n = None, phiN = None, e = None, d = None,
    ST_result = None, OT_result = None, bitsOptions = None):
        self.name = name
        self.message = message

    def otherAttribs(self):
        self.bitsOptions = [40, 41, 42, 43, 44]
        self.p = Crypto.Util.number.getPrime(self.bitsOptions[random.randint(0, 4)], randfunc=Crypto.Random.get_random_bytes)
        self.q = Crypto.Util.number.getPrime(self.bitsOptions[random.randint(0, 4)], randfunc=Crypto.Random.get_random_bytes)

        while len(str(self.p)) != 13 or len(str(self.q)) != 13:
            if len(str(self.p)) != 13:
                self.p=Crypto.Util.number.getPrime(self.bitsOptions[random.randint(0, 4)], randfunc=Crypto.Random.get_random_bytes)
            elif len(str(self.q)) != 13:
                self.q=Crypto.Util.number.getPrime(self.bitsOptions[random.randint(0, 4)], randfunc=Crypto.Random.get_random_bytes)

        self.n = self.p * self.q
        self.phiN = (self.p - 1) * (self.q - 1)

        self.e = random.randint(2, self.phiN + 1)
        while math.gcd(self.e, self.phiN) != 1:
            self.e = random.randint(2, self.phiN - 1)

        self.d = session.evaluate(wl.PowerMod(self.e, -1, self.phiN))
        session.terminate()

        self.ST_result = ""
        self.OT_result = ""

if (len(sys.argv)>1):
        bits=int(sys.argv[1])

myCipher = Cipher("myRSA","Hello Pepo")
myCipher.otherAttribs()

def Encrypt():

    OT = []
    ST = []
    c = 0
    parts = -1

    for i in range(len(myCipher.message)):
        if c % 5 == 0 or i == 0:
            OT.append([])
            parts += 1
            c += 1
            OT[parts].append('{0:012b}'.format(ord(myCipher.message[i])))
        else:
            OT[parts].append('{0:012b}'.format(ord(myCipher.message[i])))
            c += 1

    for i in range(len(OT)):
        for j in range(len(OT[i])):
            if j != 0:
                OT[i][0] += OT[i][j]
    
    for i in range(len(OT)):
        while len(OT[i]) != 1:
            OT[i].remove(OT[i][-1])
        OT[i][0] = int(OT[i][0], 2)

    for i in range(len(OT)):
        ST.append(session.evaluate(wl.PowerMod(OT[i][0], myCipher.e, myCipher.n)))
    session.terminate()

    print("ST:", ST)

    for i in range(len(ST)):
        myCipher.ST_result += str(ST[i])
        if i != len(ST):
            myCipher.ST_result += " "
    
    #print(myCipher.ST_result)
    return myCipher.ST_result

Encrypt()

def Decipher():

    ST = []
    OT = []
    OT_binary = []
    OT_binary_decomposed = []
    number = ""
    c = 0

    for i in range(len(myCipher.ST_result)):
        if myCipher.ST_result[i] != " ":
            number += myCipher.ST_result[i]
        else:
            ST.append(int(number))
            number = ""

    for i in range(len(ST)):
        OT.append(session.evaluate(wl.PowerMod(ST[i], myCipher.d, myCipher.n)))
        OT_binary.append('{0:060b}'.format(OT[i]))
    session.terminate()

    # [ celek [ petice [ prvek petice ] petice ] celek ]

    newListCounter = 0
    #partsCounter = -1
    number12bit = ""
    for i in range(len(OT_binary)):
        OT_binary_decomposed.append([])
        newListCounter = 0
        for j in range(len(OT_binary[i])):
            if newListCounter % 12 == 0 and newListCounter != 0:
                OT_binary_decomposed[i].append(number12bit)
                number12bit = ""
                number12bit += OT_binary[i][j]
                newListCounter += 1
            elif newListCounter == 0:
                number12bit += OT_binary[i][j]
                newListCounter += 1
            else:
                number12bit += OT_binary[i][j]
                newListCounter += 1
                if newListCounter == len(OT_binary[i]):
                    OT_binary_decomposed[i].append(number12bit)
                    number12bit = ""

    for i in range(len(OT_binary_decomposed)):
        for j in range(len(OT_binary_decomposed[i])):
            OT_binary_decomposed[i][j] = chr(int(OT_binary_decomposed[i][j], 2))
            myCipher.OT_result += OT_binary_decomposed[i][j]

    print(myCipher.OT_result)
    return(myCipher.OT_result)
    
Decipher()