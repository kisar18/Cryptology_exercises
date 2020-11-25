import Crypto.Util.number
from Crypto.Util.number import isPrime
import random
import math
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QMenuBar
from PyQt5 import QtGui, uic

from wolframclient.evaluation import WolframLanguageSession
session=WolframLanguageSession()
from wolframclient.language import wl

# !!! IMPORTANT !!! IMPORTANT !!! IMPORTANT !!! IMPORTANT !!! IMPORTANT !!! IMPORTANT !!! IMPORTANT !!!
# You need to use commands below in your terminal (command line) to run this application
# pip install pycryptodome
# pip install wolframclient
# !!! IMPORTANT !!! IMPORTANT !!! IMPORTANT !!! IMPORTANT !!! IMPORTANT !!! IMPORTANT !!! IMPORTANT !!!

class Cipher:

    def __init__(self, name, encXdec, message = None, p = None, q = None, n = None, phiN = None, e = None, d = None,
    ST_result = None, OT_result = None, bitsOptions = None):
        self.name = name
        self.encXdec = encXdec

    def generateKeys(self):
        self.bitsOptions = [40, 41, 42, 43, 44]
        self.p = Crypto.Util.number.getPrime(self.bitsOptions[random.randint(0, 4)], randfunc=Crypto.Random.get_random_bytes)
        self.q = Crypto.Util.number.getPrime(self.bitsOptions[random.randint(0, 4)], randfunc=Crypto.Random.get_random_bytes)

        while len(str(self.p)) != 13 or len(str(self.q)) != 13:
            if len(str(self.p)) != 13:
                self.p=Crypto.Util.number.getPrime(self.bitsOptions[random.randint(0, 4)], randfunc=Crypto.Random.get_random_bytes)
            elif len(str(self.q)) != 13:
                self.q=Crypto.Util.number.getPrime(self.bitsOptions[random.randint(0, 4)], randfunc=Crypto.Random.get_random_bytes)

    def otherAttribs(self):

        self.n = self.p * self.q
        self.phiN = (self.p - 1) * (self.q - 1)

        self.e = random.randint(2, self.phiN + 1)
        while math.gcd(self.e, self.phiN) != 1:
            self.e = random.randint(2, self.phiN - 1)

        self.d = session.evaluate(wl.PowerMod(self.e, -1, self.phiN))
        session.terminate()

        self.ST_result = ""
        self.OT_result = ""

qtCreatorFile = "gui.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

myCipher = Cipher("myRSA", "Encrypt")
myCipher.generateKeys()
myCipher.otherAttribs()

class MyApp(QMainWindow, Ui_MainWindow):

    def OnRadioButton(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            myCipher.encXdec = radioBtn.text()

    def buttonFunction(self):
        if myCipher.encXdec == "Decipher":
            self.Decipher()
        else:
            self.Encrypt()

    def TextToNumbers(self):
        OT = []
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

        return OT

    def NumbersToText(self, OT_binary):

        OT_binary_decomposed = []
        OT_int_decomposed = []
    
        newListCounter = 0
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

        OT_int_decomposed = OT_binary_decomposed
        for i in range(len(OT_binary_decomposed)):
            for j in range(len(OT_binary_decomposed[i])):
                OT_int_decomposed[i][j] = chr(int(OT_binary_decomposed[i][j], 2))         

        return OT_int_decomposed

    def Encrypt(self):

        myCipher.message = self.messageInput.text()
        myCipher.ST_result = ""
        
        if len(myCipher.message) == 0:
            self.encResult.setText("Nothing to encrypt")
            myCipher.ST_result == ""
        else:
            OT = self.TextToNumbers()
            ST = []
            if len(self.keyE_n.text()) != 0 and len(self.keyE_n.text()) != 0:
                if len(self.keyE_n.text()) != 13 or isPrime(int(self.keyE_n.text())) == False:
                    self.encResult.setText("Part n has not a correct length (13) or is not a prime")
                    return
                elif len(self.keyE_e.text()) != 13 or isPrime(int(self.keyE_e.text())) == False:
                    self.encResult.setText("Part e has not a correct length (13) or is not a prime")
                    return
                else:
                    myCipher.n = int(self.keyE_n.text())
                    myCipher.e = int(self.keyE_e.text())

            self.keyE.setText(str(myCipher.e))
            for i in range(len(OT)):
                ST.append(session.evaluate(wl.PowerMod(OT[i][0], myCipher.e, myCipher.n)))
            session.terminate()

            printedNumbers = 0
            for i in range(len(ST)):
                myCipher.ST_result += str(ST[i])
                printedNumbers += 1
                if i != len(ST):
                    myCipher.ST_result += " "
                if printedNumbers % 3 == 0 and printedNumbers != 0:
                    myCipher.ST_result += "\n"
            
            self.encResult.setText(myCipher.ST_result)
            return myCipher.ST_result

    def CopyEncryptResult(self):
        self.messageInput.setText(self.encResult.text())

    def Decipher(self):

        myCipher.OT_result = ""

        if len(self.messageInput.text()) < 1:
            self.decResult.setText("Nothing to decipher")
        else:
            decMessage = list(self.messageInput.text())
            ST_int = []
            OT_int = []
            OT_binary = []
            OT_letters = []
            number = ""
            c = 0

            for i in range(len(decMessage)):
                if decMessage[i] != " ":
                    try:
                        int(decMessage[i])
                    except:
                        self.decResult.setText("Cant decipher text, all characters must be numbers")
                        return

            for i in range(len(decMessage)):
                if decMessage[i] != " ":
                    number += decMessage[i]
                else:
                    ST_int.append(int(number))
                    number = ""

            if len(self.keyD_n.text()) != 0 and len(self.keyD_d.text()) != 0:
                if len(self.keyD_n.text()) != 13 or isPrime(int(self.keyD_n.text())) == False:
                    self.decResult.setText("Part n has not a correct length (13) or is not a prime")
                    return
                elif len(self.keyD_d.text()) != 13 or isPrime(int(self.keyD_d.text())) == False:
                    self.decResult.setText("Part d has not a correct length (13) or is not a prime")
                    return
                else:
                    myCipher.n = int(self.keyD_n.text())
                    myCipher.d = int(self.keyD_d.text())

            self.keyD.setText(str(myCipher.d))
            for i in range(len(ST_int)):
                OT_int.append(session.evaluate(wl.PowerMod(ST_int[i], myCipher.d, myCipher.n)))
                OT_binary.append('{0:060b}'.format(OT_int[i]))
            session.terminate()

            OT_letters = self.NumbersToText(OT_binary)

            for i in range(len(OT_letters)):
                for j in range(len(OT_letters[i])):
                    myCipher.OT_result += OT_letters[i][j]

            self.decResult.setText(myCipher.OT_result)
            return(myCipher.OT_result)

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.r_enc.setChecked(True)
        self.r_enc.toggled.connect(self.OnRadioButton)
        self.r_dec.toggled.connect(self.OnRadioButton)
        self.enc_dec_btn.clicked.connect(self.buttonFunction)
        self.btn_copy.clicked.connect(self.CopyEncryptResult)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())