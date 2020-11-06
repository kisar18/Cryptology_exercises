import random
import math

class Cipher:

    def __init__(self, name, language, message, repairedMessage = None, size = None, alphabet = None, table = None,
    NotInAplhabet = None, SubstituteLetter = None, positios = None):
        self.name = name
        self.language = language
        self.message = message

    def otherAttribs(self):
        while self.name != "ADFGX" and self.name != "ADFGVX":
            self.name = input("Enter type of cipher ADFGX or ADFGVX: ")

        if self.language == "ENG":
            self.NotInAplhabet = 'J'
            self.SubstituteLetter = 'I'
        else:
            self.NotInAplhabet = 'W'
            self.SubstituteLetter = 'V'

        if self.name == "ADFGX":
            self.size = 5
            self.positios = {0 : 'A', 1 : 'D', 2 : 'F', 3 : 'G', 4 : 'X'}
            self.table = table = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]
            self.alphabet = list(map(chr, range(ord('a'), ord('z') + 1)))
            self.repairedMessage = self.RepairInput(self.message)

            for i in range(len(self.alphabet)):
                self.alphabet[i] = self.alphabet[i].upper()

            self.alphabet.remove(self.NotInAplhabet)
        else:
            self.size = 6
            self.positios = {0 : 'A', 1 : 'D', 2 : 'F', 3 : 'G', 4 : 'V', 5 : 'X'}
            self.table = [['', '', '', '', '', ''], ['', '', '', '', '', ''], ['', '', '', '', '', ''], ['', '', '', '', '', ''],
                ['', '', '', '', '', ''], ['', '', '', '', '', '']]
            self.alphabet = list(map(chr, range(ord('a'), ord('z') + 1)))
            self.repairedMessage = self.RepairInput(self.message)

            for i in range(len(self.alphabet)):
                self.alphabet[i] = self.alphabet[i].upper()

            for i in range(10):
                self.alphabet.append(str(i))

    def fillTable(self):
        for i in range(self.size):
            j = 0
            while j != self.size:
                positionInAlp = random.randint(0, math.pow(self.size, 2) - 1)
                if self.size == 5:
                    if len(self.alphabet[positionInAlp]) == 1 and self.alphabet[positionInAlp] not in self.table[0] and \
                    self.alphabet[positionInAlp] not in self.table[1] and self.alphabet[positionInAlp] not in self.table[2] and \
                    self.alphabet[positionInAlp] not in self.table[3] and self.alphabet[positionInAlp] not in self.table[4]:
                        self.table[i][j] = self.alphabet[positionInAlp]
                        j += 1
                else:
                    if len(self.alphabet[positionInAlp]) == 1 and self.alphabet[positionInAlp] not in self.table[0] and \
                    self.alphabet[positionInAlp] not in self.table[1] and self.alphabet[positionInAlp] not in self.table[2] and \
                    self.alphabet[positionInAlp] not in self.table[3] and self.alphabet[positionInAlp] not in self.table[4] and \
                    self.alphabet[positionInAlp] not in self.table[5]:
                        self.table[i][j] = self.alphabet[positionInAlp]
                        j += 1

    def RepairInput(self, txtInput):

        removable = str.maketrans('', '', '`~!@#$%^&*()_-+={["'']}|\:;<,>.?/')
        txtInput = [s.translate(removable) for s in txtInput]

        for i in range(len(txtInput)):
            if txtInput[i].lower() == 'á': txtInput[i] = 'a'
            elif txtInput[i].lower() == 'č': txtInput[i] = 'c'
            elif txtInput[i].lower() == 'ď': txtInput[i] = 'd'
            elif txtInput[i].lower() == 'ě': txtInput[i] = 'e'
            elif txtInput[i].lower() == 'é': txtInput[i] = 'e'
            elif txtInput[i].lower() == 'í': txtInput[i] = 'i'
            elif txtInput[i].lower() == 'ň': txtInput[i] = 'n'
            elif txtInput[i].lower() == 'ř': txtInput[i] = 'r'
            elif txtInput[i].lower() == 'š': txtInput[i] = 's'
            elif txtInput[i].lower() == 'ť': txtInput[i] = 't'
            elif txtInput[i].lower() == 'ů': txtInput[i] = 'u'
            elif txtInput[i].lower() == 'ú': txtInput[i] = 'u'
            elif txtInput[i].lower() == 'ý': txtInput[i] = 'y'
            elif txtInput[i].lower() == 'ž': txtInput[i] = 'z'
            elif txtInput[i] == " ": txtInput[i] = "XMEZERAX"

        repairedInput = []
        
        if self.size == 5:
            for i in range(len(txtInput)):
                if txtInput[i] != '':
                    try:
                        number = int(txtInput[i])
                        if number == 0: txtInput[i] = "axa"
                        elif number == 1: txtInput[i] = "bxb"
                        elif number == 2: txtInput[i] = "cxc"
                        elif number == 3: txtInput[i] = "dxd"
                        elif number == 4: txtInput[i] = "exe"
                        elif number == 5: txtInput[i] = "fxf"
                        elif number == 6: txtInput[i] = "gxg"
                        elif number == 7: txtInput[i] = "hxh"
                        elif number == 8: txtInput[i] = "ixi"
                        elif number == 9: txtInput[i] = "jxj"
                    except:
                        continue

        for i in range(len(txtInput)):
            if txtInput[i] != '':
                repairedInput.append(txtInput[i].upper())
            else:
                continue
        
        return repairedInput

class Key:

    def __init__(self, key, repairedKey = None, priorities = None):
        self.key = key

    def otherAttribs(self):
        self.repairedKey = self.RepairInput(self.key)
        self.priorities = [None] * len(self.repairedKey)

    def RepairInput(self, txtInput):

        removable = str.maketrans('', '', '`~!@#$%^&*()_-+={["'']}|\:;<,>.?/')
        txtInput = [s.translate(removable) for s in txtInput]

        for i in range(len(txtInput)):
            if txtInput[i].lower() == 'á': txtInput[i] = 'a'
            elif txtInput[i].lower() == 'č': txtInput[i] = 'c'
            elif txtInput[i].lower() == 'ď': txtInput[i] = 'd'
            elif txtInput[i].lower() == 'ě': txtInput[i] = 'e'
            elif txtInput[i].lower() == 'é': txtInput[i] = 'e'
            elif txtInput[i].lower() == 'í': txtInput[i] = 'i'
            elif txtInput[i].lower() == 'ň': txtInput[i] = 'n'
            elif txtInput[i].lower() == 'ř': txtInput[i] = 'r'
            elif txtInput[i].lower() == 'š': txtInput[i] = 's'
            elif txtInput[i].lower() == 'ť': txtInput[i] = 't'
            elif txtInput[i].lower() == 'ů': txtInput[i] = 'u'
            elif txtInput[i].lower() == 'ú': txtInput[i] = 'u'
            elif txtInput[i].lower() == 'ý': txtInput[i] = 'y'
            elif txtInput[i].lower() == 'ž': txtInput[i] = 'z'
            elif txtInput[i] == " ": txtInput[i] = "XMEZERAX"

        repairedInput = []
        
        for i in range(len(txtInput)):
            if txtInput[i] != '':
                try:
                    number = int(txtInput[i])
                    if number == 0: txtInput[i] = "axa"
                    elif number == 1: txtInput[i] = "bxb"
                    elif number == 2: txtInput[i] = "cxc"
                    elif number == 3: txtInput[i] = "dxd"
                    elif number == 4: txtInput[i] = "exe"
                    elif number == 5: txtInput[i] = "fxf"
                    elif number == 6: txtInput[i] = "gxg"
                    elif number == 7: txtInput[i] = "hxh"
                    elif number == 8: txtInput[i] = "ixi"
                    elif number == 9: txtInput[i] = "jxj"
                except:
                    continue

        for i in range(len(txtInput)):
            if len(txtInput[i]) == 1 and txtInput[i] != '':
                repairedInput.append(txtInput[i].upper())
            else:
                continue
        
        return repairedInput

myCipher = Cipher(input("Enter type of cipher ADFGX or ADFGVX: "),"ENG", "Ahoj Pepo šejdeme se v 5 u mostů?")
myKey = Key("klicik")
myCipher.otherAttribs()
myCipher.fillTable()
myKey.otherAttribs()

def Encrypt():

    OT = []
    ST = []
    beforeTransposition = []
    afterTransposition = []
    elements = 0
    STcounter = 0
    afterTransposition_OneList = []
    badchars = 0
    printingCounter = 0

    for i in range(len(myCipher.repairedMessage)):
        if myCipher.repairedMessage[i] == myCipher.NotInAplhabet and myCipher.size == 5:
            OT.append(myCipher.SubstituteLetter)
        else:
            OT.append(myCipher.repairedMessage[i])

    for i in range(len(OT)):
        if len(OT[i]) == 1:
            for j in range(len(myCipher.table)):
                for k in range(myCipher.size):
                    if OT[i] == myCipher.table[j][k]:
                        ST.append(myCipher.positios[j])
                        ST.append(myCipher.positios[k])
        else:
            ST.append(OT[i])

    for i in range(len(ST)):
        if len(ST[i]) == 1:
            elements += 1

    rows = math.ceil(elements / len(myKey.repairedKey))
    priority = 1

    for i in range(rows):
        beforeTransposition.append([])
        afterTransposition.append([])
    
    for i in range(len(beforeTransposition)):
        j = 0
        while j != len(myKey.repairedKey) and STcounter != len(ST):
            if len(ST[STcounter]) == 1:
                beforeTransposition[i].append(ST[STcounter])
                STcounter += 1
                j += 1
            else:
                STcounter += 1

    for i in range(len(myCipher.alphabet)):
        for j in range(len(myKey.repairedKey)):
            if myCipher.alphabet[i] == myKey.repairedKey[j]:
                myKey.priorities[j] = priority
                priority += 1

    priority = 1

    for i in range(len(myKey.repairedKey)):
        for j in range(len(myKey.repairedKey)):
            if priority == myKey.priorities[j]:
                for k in range(len(beforeTransposition)):
                    try:
                        afterTransposition[k].append(beforeTransposition[k][j])
                    except:
                        continue
        priority += 1

    for i in range(len(myKey.key)):
        for j in range(len(afterTransposition)):
            try:
                afterTransposition_OneList.append(afterTransposition[j][i])
            except:
                continue

    for i in range(len(ST)):
        if len(ST[i]) == 1:
            ST[i] = afterTransposition_OneList[i - badchars]
        else:
            badchars += 1

    for i in range(len(ST)):
        if len(ST[i]) == 1:
            if printingCounter % 5 == 0 and i != 0:
                print(" " + ST[i], end='')
                printingCounter += 1
            else:
                print(ST[i], end='')
                printingCounter += 1

Encrypt()