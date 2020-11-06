#userInput = list(input("Enter text to be encrypted: "))
#cipherKey = list(input("Enter key for encryption / decription: "))
#userInput = "Ahoj Pepo jak se máš?"
userInput = "Ahoj Pepo jak se mášo?"
cipherKey = "petrklic"
#result = "pa ax ax ar aq qx xq xz zw wx wx"

OT  = []
counterOfOT = 0

def RepairInput(txtInput):

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
        elif txtInput[i].lower() == 'ý': txtInput[i] = 'y'
        elif txtInput[i].lower() == 'ž': txtInput[i] = 'z'
        elif txtInput[i] == " ": txtInput[i] = "XMEZERAX"

    repairedInput = []
    """
    for i in range(len(txtInput)):
        if txtInput[i] != '':
            try:
                number = int(txtInput[i])
                if number == 0: substituteNumber = "x0"
                elif number == 1: substituteNumber = "x1"
                elif number == 2: substituteNumber = "x2"
                elif number == 3: substituteNumber = "x3"
                elif number == 4: substituteNumber = "x4"
                elif number == 5: substituteNumber = "x5"
                elif number == 6: substituteNumber = "x6"
                elif number == 7: substituteNumber = "x7"
                elif number == 8: substituteNumber = "x8"
                elif number == 9: substituteNumber = "x9"
                repairedInput.append(substituteNumber)
                elif txtInput[i] == " ":
                    repairedInput.append("XMEZERAX")
    """
    for i in range(len(txtInput)):
        if txtInput[i] != '':
            repairedInput.append(txtInput[i].upper())
        else:
            continue
    
    return repairedInput

repUserInput = RepairInput(userInput)
spaces = 0

for i in range(len(repUserInput)):
    #if len(repUserInput[i]) == 1:
    if i != (len(repUserInput) - 1):
        if len(repUserInput[i]) == 1 and repUserInput[i + 1] == "XMEZERAX":
            if repUserInput[i] == repUserInput[i + 2] and counterOfOT % 2 == 0:
                if repUserInput[i] != 'X':
                    OT.append(repUserInput[i])
                    OT.append('X')
                    counterOfOT += 2
                else:
                    OT.append(repUserInput[i])
                    OT.append('Q')
                    counterOfOT += 2
            else:
                OT.append(repUserInput[i])
                counterOfOT += 1
        elif repUserInput[i] == "XMEZERAX":
            OT.append("XMEZERAX")
            spaces += 1
        else:
            if repUserInput[i] == repUserInput[i + 1] and counterOfOT % 2 == 0:
                if repUserInput[i] != 'X':
                    OT.append(repUserInput[i])
                    OT.append('X')
                    counterOfOT += 2
                else:
                    OT.append(repUserInput[i])
                    OT.append('Q')
                    counterOfOT += 2
            else:
                OT.append(repUserInput[i])
                counterOfOT += 1
    else:
        OT.append(repUserInput[i])
        if (len(OT) - spaces) % 2 != 0:
            if OT[-1] != 'X':
                OT.append('X')
            else:
                OT.append('Q')

repCipherKey = RepairInput(cipherKey)

table = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]

alphabet = list(map(chr, range(ord('a'), ord('z')+1)))
alphabet.remove('j')

for i in range(len(alphabet)):
    alphabet[i] = alphabet[i].upper()

num = 0 #counter of numbers in table for cipher key
alp = 0 #counter of numbers in table for other letters

for i in range(5):
    j = 0
    while j != 5:
        if num < len(repCipherKey):
            if repCipherKey[num] not in table[0] and repCipherKey[num] not in table[1] \
            and repCipherKey[num] not in table[2] and repCipherKey[num] not in table[3] and repCipherKey[num] not in table[4]:
                table[i][j] = repCipherKey[num].upper()
                num += 1
                j += 1
            else:
                num += 1
        else:
            if alphabet[alp] not in table[0] and alphabet[alp] not in table[1] and alphabet[alp] not in table[2] \
            and alphabet[alp] not in table[3] and alphabet[alp] not in table[4]:
                table[i][j] = alphabet[alp].upper()
                alp += 1
                j += 1
            else:
                alp += 1

print("Open text: ")
print(OT)
print("\n")
print("Table for encrypting: ")
print(table[0])
print(table[1])
print(table[2])
print(table[3])
print(table[4])

ST = []

def Encrypt():
    spaces = 0
    wasSpace = False
    skipElement = False

    for i in range(len(OT)):
        if(i + spaces) % 2 == 1 and skipElement == False:
            continue
        elif skipElement == True:
            skipElement = False
            continue
        else:
            if OT[i] == "XMEZERAX" and wasSpace == False:
                ST.append("XMEZERAX")
                spaces += 1
                continue
            else:
                first = OT[i]
                if OT[i + 1] == "XMEZERAX":
                    second = OT[i + 2]
                    spaces += 1
                    wasSpace = True
                    skipElement = True
                else:
                    second = OT[i + 1]
                if first == 'J':
                    first = 'I'
                elif second == 'J':
                    second = 'I'


        for j in range(len(table)):
            for k in range(len(table[j])):
                if first == table[j][k]:
                    firstRow = j
                    firstColumn = k
                if second == table[j][k]:
                    secondRow = j
                    secondColumn = k
        
        if firstRow == secondRow:
            firstColumn = (firstColumn + 1) % 5
            secondColumn = (secondColumn + 1) % 5
        elif firstColumn == secondColumn:
            firstRow = (firstRow + 1) % 5
            secondRow = (secondRow + 1) % 5
        else:
            tmp = firstColumn
            firstColumn = secondColumn
            secondColumn = tmp
        
        if wasSpace == True:
            ST.append(table[firstRow][firstColumn])
            ST.append("XMEZERAX")
            ST.append(table[secondRow][secondColumn])
            wasSpace = False
        else:
            ST.append(table[firstRow][firstColumn])
            ST.append(table[secondRow][secondColumn])


def Decipher():
    OT = []
    spaces = 0
    wasSpace = False
    skipElement = False

    for i in range(len(ST)):
        if(i + spaces) % 2 == 1 and skipElement == False:
            continue
        elif skipElement == True:
            skipElement = False
            continue
        else:
            if ST[i] == "XMEZERAX" and wasSpace == False:
                OT.append("XMEZERAX")
                spaces += 1
                continue
            else:
                first = ST[i]
                if ST[i + 1] == "XMEZERAX":
                    second = ST[i + 2]
                    spaces += 1
                    wasSpace = True
                    skipElement = True
                else:
                    second = ST[i + 1]
                if first == 'J':
                    first = 'I'
                elif second == 'J':
                    second = 'I'


        for j in range(len(table)):
            for k in range(len(table[j])):
                if first == table[j][k]:
                    firstRow = j
                    firstColumn = k
                if second == table[j][k]:
                    secondRow = j
                    secondColumn = k
        
        if firstRow == secondRow:
            firstColumn = (firstColumn - 1) % 5
            secondColumn = (secondColumn - 1) % 5
        elif firstColumn == secondColumn:
            firstRow = (firstRow - 1) % 5
            secondRow = (secondRow - 1) % 5
        else:
            tmp = firstColumn
            firstColumn = secondColumn
            secondColumn = tmp
        
        if wasSpace == True:
            OT.append(table[firstRow][firstColumn])
            OT.append("XMEZERAX")
            OT.append(table[secondRow][secondColumn])
            wasSpace = False
        else:
            OT.append(table[firstRow][firstColumn])
            OT.append(table[secondRow][secondColumn])

    print("\n")
    print(ST)
    print(OT)
    return(OT)

Encrypt()
Decipher()