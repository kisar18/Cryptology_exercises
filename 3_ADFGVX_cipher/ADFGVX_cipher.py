import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QMenuBar
from PyQt5 import QtGui, uic
import math
import random

class Cipher:

    def __init__(self, name, language, message, repairedMessage = None, size = None, alphabet = None, table = None,
    NotInAplhabet = None, SubstituteLetter = None, positios = None):
        self.name = name
        self.language = language
        self.message = message

    def otherAttribs(self):

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
                        window.tableWidget.setItem(i, j, QTableWidgetItem(self.alphabet[positionInAlp].upper()))
                        j += 1
                else:
                    if len(self.alphabet[positionInAlp]) == 1 and self.alphabet[positionInAlp] not in self.table[0] and \
                    self.alphabet[positionInAlp] not in self.table[1] and self.alphabet[positionInAlp] not in self.table[2] and \
                    self.alphabet[positionInAlp] not in self.table[3] and self.alphabet[positionInAlp] not in self.table[4] and \
                    self.alphabet[positionInAlp] not in self.table[5]:
                        self.table[i][j] = self.alphabet[positionInAlp]
                        window.tableWidget.setItem(i, j, QTableWidgetItem(self.alphabet[positionInAlp].upper()))
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

        priority = 1
        for i in range(len(myCipher.alphabet)):
            for j in range(len(self.repairedKey)):
                if myCipher.alphabet[i] == self.repairedKey[j]:
                    self.priorities[j] = priority
                    priority += 1

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
 
qtCreatorFile = "gui.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

myCipher = Cipher("ADFGX","ENG", "Ahoj Pepo šejdeme se v 5 u mostů?")
myKey = Key("klicik")
#myCipher.otherAttribs()
#myCipher.fillTable()
#myKey.otherAttribs()

class MyApp(QMainWindow, Ui_MainWindow):

    def appType(self, typeName):
        if typeName == "ADFGVX":
            myCipher.name = typeName
            myCipher.otherAttribs()
            self.type_label.setText("Type: ADFGVX")
        else:
            myCipher.name = typeName
            myCipher.otherAttribs()
            self.type_label.setText("Type: ADFGX")

    def appLanguage(self, language):
        if language == "czech":
            myCipher.language = "CZE"
            myCipher.otherAttribs()
            self.language_label.setText("Language: Czech")
        else:
            myCipher.language = "ENG"
            myCipher.otherAttribs()
            self.language_label.setText("Language: English")

    def Encrypt(self):

        myCipher.otherAttribs()
        myKey.otherAttribs()
        myCipher.fillTable()
        
        OT = []
        ST = []
        beforeTransposition = []
        afterTransposition = []
        elements = 0
        STcounter = 0
        afterTransposition_OneList = []
        badchars = 0
        printingCounter = 1
        printout = ""

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
            while j != len(myKey.repairedKey):
                try:
                    if len(ST[STcounter]) == 1:
                        beforeTransposition[i].append(ST[STcounter])
                        STcounter += 1
                        j += 1
                    else:
                        STcounter += 1
                except:
                    beforeTransposition[i].append(None)
                    j += 1

        for i in range(len(myKey.repairedKey)):
            for j in range(len(myKey.repairedKey)):
                if priority == myKey.priorities[j]:
                    for k in range(len(beforeTransposition)):
                        afterTransposition[k].append(beforeTransposition[k][j])
            priority += 1

        for i in range(len(myKey.key)):
            for j in range(len(afterTransposition)):
                if afterTransposition[j][i] != None:
                    afterTransposition_OneList.append(afterTransposition[j][i])

        for i in range(len(ST)):
            if len(ST[i]) == 1:
                ST[i] = afterTransposition_OneList[i - badchars]
            else:
                badchars += 1

        for i in range(len(ST)):
            if len(ST[i]) == 1:
                if printingCounter % 5 == 0 and i != 0:
                    printout += ST[i]
                    printout += " "
                    printingCounter += 1
                else:
                    printout += ST[i]
                    printingCounter += 1

        if len(myCipher.message) == 0:
            self.encryptResult.setText("Nothing to encrypt")
        else:
            self.encryptResult.setText(printout)
        return(ST)

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.ADFGX.triggered.connect(lambda: self.appType("ADFGX"))
        self.ADFGVX.triggered.connect(lambda: self.appType("ADFGVX"))
        self.ENG.triggered.connect(lambda: self.appLanguage("english"))
        self.CZE.triggered.connect(lambda: self.appLanguage("czech"))
        self.encrypt_btn.clicked.connect(self.Encrypt)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())