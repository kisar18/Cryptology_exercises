letters = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9, 'k' : 10, 'l' : 11,
    'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17, 's' : 18, 't' : 19, 'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23,
    'y' : 24, 'z' : 25}

reversed_Letters = {v: k for k, v in letters.items()}
modulo = 26

keyA = int(input("Enter value for key 'a': "))

while keyA % 2 == 0 or keyA % 13 == 0:
    print("Greatest common divisor of the key 'a' and 26 has to be 1, please enter new value for key 'a': ")
    keyA = int(input("Enter value for key 'a': "))

keyB = int(input("Enter value for key 'b': "))

userInput = list(input("Enter text for encoding: "))
encodedInput = [None] * len(userInput)
decodedInput = [None] * len(userInput)

def encrypt(a, b, OT, ST):
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

    counter = 0

    for i in range(len(OT)):
        if OT[i] == " ":
            ST[i] = "XMEZERAX"
            print("XMEZERAX", end='')
        else:
            ST[i] = (a * letters[OT[i]] + b) % modulo
            counter += 1

            if counter % 5 == 0:
                print(reversed_Letters[ST[i]] + " ", end='')
            else:
                print(reversed_Letters[ST[i]], end='')

def decipher(a, b, OT, ST):
    counter = 0

    """
    For this function is needed inverse modulo
    A mod B = C,
    when A * C mod B = 1, C is inverse modulo
    for key 'a' = 3 => 3 * !9! mod 26 = 1
    """
    for i in range(modulo - 1):
        candidate = (a * i) % modulo
        if candidate == 1:
            inverseModulo = i
            break

    for i in range(len(ST)):
        if ST[i] == "XMEZERAX":
            OT[i] = " "
            print(" ", end='')
        else:
            OT[i] = (ST[i] - b) * inverseModulo % modulo
            counter += 1

            if counter % 5 == 0:
                print(reversed_Letters[OT[i]] + " ", end='')
            else:
                print(reversed_Letters[OT[i]], end='')

encrypt(keyA, keyB, userInput, encodedInput)
print()
decipher(keyA, keyB, decodedInput, encodedInput)