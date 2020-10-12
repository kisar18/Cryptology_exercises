userInput = list(input("Enter text to be encrypted: "))
cipherKey = list(input("Enter key for encryption / decription: "))
#userInput = "paaaaraqqxxxzzwww"
#result = "pa ax ax ar aq qx xq xz zw wx wx"

OT  = []
counterOfOT = 0

def RepairInput(txtInput):
    for i in range(len(txtInput)):
        if txtInput[i] == 'á': txtInput[i] = 'a'
        elif txtInput[i] == 'č': txtInput[i] = 'c'
        elif txtInput[i] == 'ď': txtInput[i] = 'd'
        elif txtInput[i] == 'ě': txtInput[i] = 'e'
        elif txtInput[i] == 'é': txtInput[i] = 'e'
        elif txtInput[i] == 'í': txtInput[i] = 'i'
        elif txtInput[i] == 'ň': txtInput[i] = 'n'
        elif txtInput[i] == 'ř': txtInput[i] = 'r'
        elif txtInput[i] == 'š': txtInput[i] = 's'
        elif txtInput[i] == 'ť': txtInput[i] = 't'
        elif txtInput[i] == 'ů': txtInput[i] = 'u'
        elif txtInput[i] == 'ý': txtInput[i] = 'y'
        elif txtInput[i] == 'ž': txtInput[i] = 'z'

    removable = str.maketrans('', '', '`~!@#$%^&*()_-+={["'']}|\:;<,>.?/')
    txtInput = [s.translate(removable) for s in txtInput]

    repairedInput = []
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

            except:
                if txtInput[i] == " ":
                    repairedInput.append("XMEZERAX")
                else:
                    repairedInput.append(txtInput[i])
                    
    return repairedInput

repUserInput = RepairInput(userInput)

for i in range(len(repUserInput)):
    if i != (len(repUserInput) - 1):
        if repUserInput[i] == repUserInput[i + 1] and counterOfOT % 2 == 0:
            if repUserInput[i] != 'x':
                OT.append(repUserInput[i])
                OT.append('x')
                counterOfOT += 2
            else:
                OT.append(repUserInput[i])
                OT.append('q')
                counterOfOT += 2
        else:
            OT.append(repUserInput[i])
            counterOfOT += 1
    else:
        OT.append(repUserInput[i])
        if len(OT) % 2 != 0:
            if OT[-1] != 'x':
                OT.append('x')
            else:
                OT.append('q')
print(OT)

repCipherKey = RepairInput(cipherKey)
print(repCipherKey)