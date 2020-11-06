import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, uic
import math
 
qtCreatorFile = "gui.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QMainWindow, Ui_MainWindow):

    defaultTextEncrypt = "Encrypted user input:"
    warning = "Bad input"

    letters = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9, 'k' : 10, 'l' : 11,
    'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17, 's' : 18, 't' : 19, 'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23,
    'y' : 24, 'z' : 25}

    reversed_Letters = {v: k for k, v in letters.items()}
    modulo = 26

    def Encrypt(self):
        
        keyA = int(self.keyA_input.text())

        while math.gcd(keyA, self.modulo) != 1:
            self.encrypt_result.setText("Greatest common divisor of the key 'a' and 26 has to be 1,\n please enter new value for key 'a'")
            self.keyA_input.clear()
            return
        
        keyB = int(self.keyB_input.text())
        OT = list(self.encrypt_input.text())
        ST = [None] * len(OT)
        ST_Text = ""
        counter= 0
        
        for i in range(len(OT)):
            if OT[i] == 'á': OT[i] = 'a'
            elif OT[i] == 'č': OT[i] = 'c'
            elif OT[i] == 'ď': OT[i] = 'd'
            elif OT[i] == 'ě': OT[i] = 'e'
            elif OT[i] == 'é': OT[i] = 'e'
            elif OT[i] == 'í': OT[i] = 'i'
            elif OT[i] == 'ň': OT[i] = 'n'
            elif OT[i] == 'ř': OT[i] = 'r'
            elif OT[i] == 'š': OT[i] = 's'
            elif OT[i] == 'ť': OT[i] = 't'
            elif OT[i] == 'ů': OT[i] = 'u'
            elif OT[i] == 'ý': OT[i] = 'y'
            elif OT[i] == 'ž': OT[i] = 'z'
        removable = str.maketrans('', '', '`~!@#$%^&*()_-+={["'']}|\:;<,>.?/')
        OT = [s.translate(removable) for s in OT]

        for i in range(len(OT)):
            try:
                y = int(OT[i])
                ST[i] = str(9 - y)
                if counter % 5 == 0 and counter != 0:
                    ST_Text += " "
                    ST_Text += str(9 - y)
                else:
                    ST_Text += str(9 - y)
                counter += 1

            except:
                if OT[i] == " ":
                    ST[i] = "XMEZERAX"
                    ST_Text += "XMEZERAX"
                elif OT[i] == '':
                    continue
                else:
                    ST[i] = (keyA * self.letters[OT[i].lower()] + keyB) % self.modulo
                    if counter % 5 == 0 and counter != 0:
                        ST_Text += " "
                        ST_Text += self.reversed_Letters[ST[i]]
                    else:
                        ST_Text += self.reversed_Letters[ST[i]]
                    counter += 1
        encAplhabet = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9, 'k' : 10, 'l' : 11,
            'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17, 's' : 18, 't' : 19, 'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23,
            'y' : 24, 'z' : 25}

        enc_alph_string = ""
        c = 0

        for i in self.letters:
            encAplhabet[i] = self.reversed_Letters[(keyA * self.letters[i] + keyB) % self.modulo]
            enc_alph_string += "'" + str(self.reversed_Letters[c]) + "'" + " " + ":" + " " + encAplhabet[i] + "," + " "
            c += 1
            if c % 12 == 0:
                enc_alph_string += "\n"

        self.encrypt_result.setText(ST_Text.upper())
        self.encryptedAlphabet.setText(enc_alph_string)

    def CopyEncryptResult(self):
        self.decipher_input.setText(self.encrypt_result.text())

    def Decipher(self):

        ST_Text = self.decipher_input.text()
        ST = list(ST_Text.replace("XMEZERAX", "-"))

        OT = [None] * len(ST)
        keyA = int(self.keyA_input.text())
        keyB = int(self.keyB_input.text())
        OT_Text = ""


        for i in range(self.modulo - 1):
            candidate = (keyA * i) % self.modulo
            if candidate == 1:
                inverseModulo = i
                break

        for i in range(len(ST)):
            try:
                y = int(ST[i])
                OT[i] = str(9 - y)
                OT_Text += str(9 - y)
            except:
                if ST[i] == "-":
                    OT[i] = " "
                    OT_Text += " "
                elif ST[i] == " ":
                    continue
                else:
                    OT[i] = (self.letters[ST[i].lower()] - keyB) * inverseModulo % self.modulo
                    OT_Text += self.reversed_Letters[OT[i]]

        self.decipher_result.setText(OT_Text.upper())


    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.encrypt_btn.clicked.connect(self.Encrypt)
        self.copy_btn.clicked.connect(self.CopyEncryptResult)
        self.decipher_btn.clicked.connect(self.Decipher)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())