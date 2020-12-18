import Crypto.Util.number
from Crypto.Util.number import isPrime
import random
import math
import sys
import hashlib
import zipfile
from os.path import basename
import base64

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5 import QtGui, uic
from PyQt5.QtCore import QFileInfo

from wolframclient.evaluation import WolframLanguageSession
session=WolframLanguageSession()
from wolframclient.language import wl

# !!! IMPORTANT !!! IMPORTANT !!! IMPORTANT !!! IMPORTANT !!! IMPORTANT !!! IMPORTANT !!! IMPORTANT !!!
# You need to use commands below in your terminal (command line) to run this application
# pip install pycryptodome
# pip install wolframclient
# !!! IMPORTANT !!! IMPORTANT !!! IMPORTANT !!! IMPORTANT !!! IMPORTANT !!! IMPORTANT !!! IMPORTANT !!!

class Cipher:

    def __init__(self, name, message = None, p = None, q = None, n = None, phiN = None, e = None, d = None,
    ST_result = None, OT_result = None, bitsOptions = None, fileToBeSigned = None, signFilePath = None,
    privPath = None, pubPath = None, zipPath = None, fileToBeVerified = None, toVerifyMessage = None, userFile = None):
        self.name = name
        self.e = 0
        self.d = 0

    def generateKeys(self):
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

    def otherAttribs(self):
        self.ST_result = ""
        self.OT_result = ""

myCipher = Cipher("myRSA")

qtCreatorFile = "gui.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QMainWindow, Ui_MainWindow):

    def encodeToBase64(self, text):
        base64Text = text.encode("ascii")
        base64Bytes = base64.b64encode(base64Text)
        noBytesText = base64Bytes.decode("ascii")
        return noBytesText

    def decodeFromBase64(self, text):
        base64BytesText = text.encode("ascii")
        textBytes = base64.b64decode(base64BytesText)
        decodedBase64 = textBytes.decode("ascii")
        return decodedBase64

    def GetFile(self, typeOfFile, suff):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"Open {} File".format(typeOfFile), "","{}".format(suff), options=options)
        if fileName:
            if typeOfFile == "any":
                myCipher.fileToBeSigned = fileName
                f = QFileInfo(fileName)
                n = f.fileName()
                file_info = "Informations about the file:\n \n"
                file_info += "Name: " + n + "\n"
                p = f.filePath()
                file_info += "Path: " + p + "\n"
                suf = f.suffix()
                file_info += "Suffix: " + suf + "\n"
                size = f.size()
                file_info += "Size (in bytes): " + str(size) + "\n"
                lastModify = f.lastModified().toPyDateTime()
                file_info += "Date of last change: " + str(lastModify)
                self.fileInfo.setText(file_info)
            elif typeOfFile == "Signed":
                myCipher.userFile = fileName
            elif typeOfFile == "Private key":
                myCipher.privPath = fileName
                with open(fileName, "r") as f:
                    f.seek(4)
                    base64Text = f.readline()
                    decodedBase64D = self.decodeFromBase64(base64Text)
                    myCipher.d = int(decodedBase64D, 10)
                    base64Text2 = f.readline()
                    decodedBase64N = self.decodeFromBase64(base64Text2)
                    myCipher.n = int(decodedBase64N, 10)
            elif typeOfFile == "Public key":
                myCipher.pubPath = fileName
                with open(fileName, "r") as f:
                    f.seek(4)
                    base64Text = f.readline()
                    decodedBase64E = self.decodeFromBase64(base64Text)
                    myCipher.e = int(decodedBase64E, 10)
                    base64Text2 = f.readline()
                    decodedBase64N = self.decodeFromBase64(base64Text2)
                    myCipher.n = int(decodedBase64N, 10)
            elif typeOfFile == "Zip":
                myCipher.zipPath = fileName
                with zipfile.ZipFile(fileName, "r") as z:
                    z.extractall("Extracted_files")
            elif typeOfFile == "Sign":
                myCipher.fileToBeVerified = fileName
                with open(fileName, "r") as f:
                    f.seek(13)
                    base64Text = f.readline()
                    decodedBase64 = self.decodeFromBase64(base64Text)
                    myCipher.toVerifyMessage = list(decodedBase64)

    def SaveFile(self, text, typeOfFile, suff):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(window, "Save {} file".format(typeOfFile), "","{}".format(suff), options=options)
        if fileName:
            if typeOfFile == "Zip":
                myCipher.zipPath = fileName
                with zipfile.ZipFile(fileName, "w") as z:
                    if myCipher.fileToBeSigned and myCipher.signFilePath:
                        z.write(myCipher.fileToBeSigned, basename(myCipher.fileToBeSigned))
                        z.write(myCipher.signFilePath, basename(myCipher.signFilePath))
            elif typeOfFile == "Sign":
                myCipher.signFilePath = fileName
                with open(fileName, "w") as f:
                    textInBase64 = self.encodeToBase64(text)
                    f.write("RSA_SHA3-512 " + str(textInBase64))
            elif typeOfFile == "Private key":
                myCipher.privPath = fileName
                with open(fileName, "w") as f:
                    dInBase64 = self.encodeToBase64(str(text))
                    nInbase64 = self.encodeToBase64(str(myCipher.n))
                    f.writelines(["RSA " + dInBase64, "\n" + nInbase64])
            elif typeOfFile == "Public key":
                myCipher.pubPath = fileName
                with open(fileName, "w") as f:
                    eInBase64 = self.encodeToBase64(str(text))
                    nInbase64 = self.encodeToBase64(str(myCipher.n))
                    f.writelines(["RSA " + eInBase64, "\n" + nInbase64])
            else:
                with open(fileName, "w") as f:
                    f.write(str(text))

    def HashFile(self, fileToHash):
        BLOCK_SIZE = 512
        file_hash = hashlib.sha3_512()
        fName = fileToHash
        with open(fName, 'rb') as f:
            fb = f.read(BLOCK_SIZE)
            while len(fb) > 0:
                file_hash.update(fb)
                fb = f.read(BLOCK_SIZE)
        myCipher.message = file_hash.hexdigest()
        self.signResult.setText("Hash is complete")

        return file_hash.hexdigest()

    def KeyPair(self):
        if myCipher.e == 0 and myCipher.d == 0:
            myCipher.generateKeys()
            myCipher.otherAttribs()
        self.SaveFile(myCipher.d, "Private key", "Private key (*.priv)")
        self.SaveFile(myCipher.e, "Public key", "Public key (*.pub)")

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
        badNumbers = 0
        OT_int_decomposed = OT_binary_decomposed
        for i in range(len(OT_binary_decomposed)):
            for j in range(len(OT_binary_decomposed[i])):
                if OT_binary_decomposed[i][j] != "000000000000":
                    OT_int_decomposed[i][j - badNumbers] = chr(int(OT_binary_decomposed[i][j], 2))
                else:
                    badNumbers += 1

        for i in range(badNumbers):
            OT_int_decomposed[-1].pop()

        return OT_int_decomposed

    def Compare(self):
        if myCipher.OT_result == self.HashFile(myCipher.userFile):
            self.verResult.setText("File was not damaged")
        else:
            self.verResult.setText("File was damaged")

    def Encrypt(self):

        myCipher.ST_result = ""

        OT = self.TextToNumbers()
        ST = []

        for i in range(len(OT)):
            ST.append(session.evaluate(wl.PowerMod(OT[i][0], myCipher.d, myCipher.n)))
        session.terminate()

        printedNumbers = 0
        for i in range(len(ST)):
            myCipher.ST_result += str(ST[i])
            printedNumbers += 1
            if i != len(ST):
                myCipher.ST_result += " "
        
        f = QFileInfo(myCipher.fileToBeSigned)
        n = f.fileName()
        self.signResult.setText("File {} was succesfully signed".format(n))

    def Decipher(self):

        myCipher.OT_result = ""

        if len(myCipher.toVerifyMessage) < 1:
            self.verifyResult.setText("Nothing to decipher")
        else:
            ST_int = []
            OT_int = []
            OT_binary = []
            OT_letters = []
            number = ""
            c = 0

            for i in range(len(myCipher.toVerifyMessage)):
                if myCipher.toVerifyMessage[i] != " ":
                    number += myCipher.toVerifyMessage[i]
                else:
                    try:
                        ST_int.append(int(number))
                        number = ""
                    except:
                        self.verResult.setText("File was damaged")
                        return

            for i in range(len(ST_int)):
                OT_int.append(session.evaluate(wl.PowerMod(ST_int[i], myCipher.e, myCipher.n)))
                OT_binary.append('{0:060b}'.format(OT_int[i]))
            session.terminate()
            
            OT_letters = self.NumbersToText(OT_binary)

            for i in range(len(OT_letters)):
                for j in range(len(OT_letters[i])):
                    myCipher.OT_result += OT_letters[i][j]

            return(myCipher.OT_result)
        
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.choose_btn.clicked.connect(lambda: self.GetFile("any", "All Files (*)"))
        self.hash_btn.clicked.connect(lambda: self.HashFile(myCipher.fileToBeSigned))
        self.saveKey_btn.clicked.connect(self.KeyPair)
        self.openPriv_btn.clicked.connect(lambda: self.GetFile("Private key", "Private key (*.priv)"))
        self.encrypt_btn.clicked.connect(self.Encrypt)
        self.saveSign_btn.clicked.connect(lambda: self.SaveFile(myCipher.ST_result, "Sign", "Sign files (*.sign)"))
        self.zip_btn.clicked.connect(lambda: self.SaveFile("None", "Zip", "Zip files (*.zip)"))
        self.extract_btn.clicked.connect(lambda: self.GetFile("Zip", "Zip files (*.zip)"))
        self.openSign_btn.clicked.connect(lambda: self.GetFile("Sign", "Sign files (*.sign)"))
        self.openPub_btn.clicked.connect(lambda: self.GetFile("Public key", "Public key (*.pub)"))
        self.decipher_btn.clicked.connect(self.Decipher)
        self.openOriginal_btn.clicked.connect(lambda: self.GetFile("Signed", "All Files (*)"))
        self.compare_btn.clicked.connect(self.Compare)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())