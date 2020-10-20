import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QMenuBar
from PyQt5 import QtGui, uic
import math
 
qtCreatorFile = "gui.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QMainWindow, Ui_MainWindow):

    twinLetter1 = 'X'
    twinLetter2 = 'Q'
    notInAlphabetLetter = 'J'
    substituteLetter = 'I'

    def language(self, name):
        if name == "czech":
            self.twinLetter1 = 'X'
            self.twinLetter2 = 'W'
            self.notInAlphabetLetter = 'Q'
            self.substituteLetter = 'O'
            self.language_label.setText("Language: Czech")
        else:
            self.twinLetter1 = 'X'
            self.twinLetter2 = 'Q'
            self.notInAlphabetLetter = 'J'
            self.substituteLetter = 'I'
            self.language_label.setText("Language: English")

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
            if txtInput[i] != '':
                repairedInput.append(txtInput[i].upper())
            else:
                continue
        
        return repairedInput

    def Encrypt(self):
 
        OT  = []
        counterOfOT = 0
        table = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]

        alphabet = list(map(chr, range(ord('a'), ord('z')+1)))
        alphabet.remove(self.notInAlphabetLetter.lower())

        for i in range(len(alphabet)):
            alphabet[i] = alphabet[i].upper()

        num = 0 #counter of numbers in table for cipher key
        alp = 0 #counter of numbers in table for other letters  

        cipherKey = self.keyCipher_input.text()
        repCipherKey = self.RepairInput(cipherKey)
        userInput = self.openText_input.text()
        repUserInput = self.RepairInput(userInput)

        ST = []
        counterOfOT = 0
        spacesAndNumbers = 0

        for i in range(len(repUserInput)):
            #if len(repUserInput[i]) == 1:
            if i != (len(repUserInput) - 2) and i != (len(repUserInput) - 1):
                if len(repUserInput[i]) == 1 and len(repUserInput[i + 1]) > 1:
                    if repUserInput[i] == repUserInput[i + 2] and counterOfOT % 2 == 0:
                        if repUserInput[i] != self.twinLetter1:
                            OT.append(repUserInput[i])
                            OT.append(self.twinLetter1)
                            counterOfOT += 2
                        else:
                            OT.append(repUserInput[i])
                            OT.append(self.twinLetter2)
                            counterOfOT += 2
                    else:
                        OT.append(repUserInput[i])
                        counterOfOT += 1
                elif len(repUserInput[i]) > 1:
                    OT.append(repUserInput[i])
                    spacesAndNumbers += 1
                else:
                    if repUserInput[i] == repUserInput[i + 1] and counterOfOT % 2 == 0:
                        if repUserInput[i] != self.twinLetter1:
                            OT.append(repUserInput[i])
                            OT.append(self.twinLetter1)
                            counterOfOT += 2
                        else:
                            OT.append(repUserInput[i])
                            OT.append(self.twinLetter2)
                            counterOfOT += 2
                    else:
                        OT.append(repUserInput[i])
                        counterOfOT += 1
            else:
                if len(repUserInput[i]) > 1:
                    OT.append(repUserInput[i])
                    spacesAndNumbers += 1
                else:
                    OT.append(repUserInput[i])

        if (len(OT) - spacesAndNumbers) % 2 != 0:
            if OT[-1] != self.twinLetter1:
                OT.append(self.twinLetter1)
            else:
                OT.append(self.twinLetter2)
    

        for i in range(5):
            j = 0
            while j != 5:
                if num < len(repCipherKey):
                    if repCipherKey[num] not in table[0] and repCipherKey[num] not in table[1] \
                    and repCipherKey[num] not in table[2] and repCipherKey[num] not in table[3] \
                    and repCipherKey[num] not in table[4] and len(repCipherKey[num]) == 1:
                        table[i][j] = repCipherKey[num].upper()
                        self.tableWithKey.setItem(i, j, QTableWidgetItem(repCipherKey[num].upper()))
                        num += 1
                        j += 1
                    else:
                        num += 1
                else:
                    if alphabet[alp] not in table[0] and alphabet[alp] not in table[1] \
                    and alphabet[alp] not in table[2] and alphabet[alp] not in table[3] \
                    and alphabet[alp] not in table[4]:
                        table[i][j] = alphabet[alp].upper()
                        self.tableWithKey.setItem(i, j, QTableWidgetItem(alphabet[alp].upper()))
                        alp += 1
                        j += 1
                    else:
                        alp += 1

        spacesAndNumbers = 0
        wasSpace = False
        was2Spaces = False
        skipElement = False
        skip2Elements = False

        for i in range(len(OT)):
            if(i + spacesAndNumbers) % 2 == 1 and skipElement == False:
                continue
            elif skipElement == True:
                skipElement = False
                continue
            elif skip2Elements == True:
                skip2Elements = False
                skipElement = True
                continue
            else:
                if len(OT[i]) > 1 and wasSpace == False:
                    ST.append(OT[i])
                    spacesAndNumbers += 1
                    continue
                else:
                    first = OT[i]
                    if len(OT[i + 1]) > 1 and len(OT[i + 2]) == 1:
                        second = OT[i + 2]
                        spacesAndNumbers += 1
                        wasSpace = True
                        skipElement = True
                    elif len(OT[i + 1]) > 1 and len(OT[i + 2]) > 1:
                        second = OT[i + 3]
                        spacesAndNumbers += 2
                        was2Spaces = True
                        skip2Elements = True
                    else:
                        second = OT[i + 1]

                    if first == self.notInAlphabetLetter:
                        first = self.substituteLetter
                    elif second == self.notInAlphabetLetter:
                        second = self.substituteLetter


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
                ST.append(OT[i + 1])
                ST.append(table[secondRow][secondColumn])
                wasSpace = False
            elif was2Spaces == True:
                ST.append(table[firstRow][firstColumn])
                ST.append(OT[i + 1])
                ST.append(OT[i + 2])
                ST.append(table[secondRow][secondColumn])
                was2Spaces = False
            else:
                ST.append(table[firstRow][firstColumn])
                ST.append(table[secondRow][secondColumn])

        ST_string = ""
        c = 1
        for i in range(len(ST)):
            if c % 31 == 0 and c != 1:
                ST_string += "\n"

            if c % 5 == 0 and len(ST[i]) == 1:
                ST_string += ST[i]
                ST_string += " "
                c += 1
            elif len(ST[i]) != 1:
                continue
            else:
                ST_string += ST[i]
                c += 1
        if len(repUserInput) == 0:
            self.encrypt_result.setText("Nothing to encrypt")
        else:
            self.encrypt_result.setText(ST_string)
        return(ST)

    def CopyEncryptResult(self):
        self.ST_input.setText(self.encrypt_result.text())

    def Decipher(self):

        table = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]

        alphabet = list(map(chr, range(ord('a'), ord('z')+1)))
        alphabet.remove(self.notInAlphabetLetter.lower())

        for i in range(len(alphabet)):
            alphabet[i] = alphabet[i].upper()

        num = 0 #counter of numbers in table for cipher key
        alp = 0 #counter of numbers in table for other letters

        cipherKey = self.keyCipher_input.text()
        repCipherKey = self.RepairInput(cipherKey)

        ST = self.Encrypt()
        spacesCounter = 0

        for i in range(5):
            j = 0
            while j != 5:
                if num < len(repCipherKey):
                    if repCipherKey[num] not in table[0] and repCipherKey[num] not in table[1] \
                    and repCipherKey[num] not in table[2] and repCipherKey[num] not in table[3] \
                    and repCipherKey[num] not in table[4] and len(repCipherKey[i]) == 1:
                        table[i][j] = repCipherKey[num].upper()
                        self.tableWithKey.setItem(i, j, QTableWidgetItem(repCipherKey[num].upper()))
                        num += 1
                        j += 1
                    else:
                        num += 1
                else:
                    if alphabet[alp] not in table[0] and alphabet[alp] not in table[1] \
                    and alphabet[alp] not in table[2] and alphabet[alp] not in table[3] \
                    and alphabet[alp] not in table[4]:
                        table[i][j] = alphabet[alp].upper()
                        self.tableWithKey.setItem(i, j, QTableWidgetItem(alphabet[alp].upper()))
                        alp += 1
                        j += 1
                    else:
                        alp += 1

        OT = []
        spacesAndNumbers = 0
        wasSpace = False
        was2Spaces = False
        skipElement = False
        skip2Elements = False

        for i in range(len(ST)):
            if(i + spacesAndNumbers) % 2 == 1 and skipElement == False:
                continue
            elif skipElement == True:
                skipElement = False
                continue
            elif skip2Elements == True:
                skip2Elements = False
                skipElement = True
                continue
            else:
                if len(ST[i]) > 1 and wasSpace == False:
                    OT.append(ST[i])
                    spacesAndNumbers += 1
                    continue
                else:
                    first = ST[i]
                    if len(ST[i + 1]) > 1 and len(ST[i + 2]) == 1:
                        second = ST[i + 2]
                        spacesAndNumbers += 1
                        wasSpace = True
                        skipElement = True
                    elif len(ST[i + 1]) > 1 and len(ST[i + 2]) > 1:
                        second = ST[i + 3]
                        spacesAndNumbers += 2
                        was2Spaces = True
                        skip2Elements = True
                    else:
                        second = ST[i + 1]

                    if first == self.notInAlphabetLetter:
                        first = self.substituteLetter
                    elif second == self.notInAlphabetLetter:
                        second = self.substituteLetter


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
                OT.append(ST[i + 1])
                OT.append(table[secondRow][secondColumn])
                wasSpace = False
            elif was2Spaces == True:
                OT.append(table[firstRow][firstColumn])
                OT.append(ST[i + 1])
                OT.append(ST[i + 2])
                OT.append(table[secondRow][secondColumn])
                was2Spaces = False
            else:
                OT.append(table[firstRow][firstColumn])
                OT.append(table[secondRow][secondColumn])

        OT_string = ""
        c = 1
        for i in range(len(OT)):
            if c % 31 == 0 and c != 1:
                OT_string += "\n"

            if len(OT[i]) > 1:
                if OT[i] == "XMEZERAX":
                    OT_string += " "
                else:
                    for j in range(10):
                        if OT[i][0] == alphabet[j]:
                            OT_string += str(j)
            else:
                OT_string += OT[i]
            c += 1

        if len(ST) == 0:
            self.decipher_result.setText("Nothing to decipher")
        else:
            self.decipher_result.setText(OT_string)
        return(OT)

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.encrypt_btn.clicked.connect(self.Encrypt)
        self.copy_btn.clicked.connect(self.CopyEncryptResult)
        self.decipher_btn.clicked.connect(self.Decipher)
        self.ENG.triggered.connect(lambda: self.language("english"))
        self.CZE.triggered.connect(lambda: self.language("czech"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())