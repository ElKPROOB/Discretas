import os
import string

import readchar
import pyperclip as clp
from numpy import ones

def RequestASet(id):
    set = ""
    while True:
        try:
            os.system("cls")
            print("Ingrese el conjunto " + id + ": {" + set + "}")
            print("Ejemplo de conjunto: {{}, 2, (3, 4), A}")
            userInput = readchar.readkey()
            if userInput == "\r":
                break
            elif userInput == readchar.key.CTRL_V:
                set += clp.paste()
            elif userInput == "\x08":
                set = set[:-1]
            elif userInput == "\x1b":
                return -1
            elif ord(userInput) > 31 and ord(userInput) < 127:
                set += userInput
        except:
            pass
    # try:
    set = set.replace(" ", "")
    setDef = []
    subs = []
    ignore = 0
    i = 0
    while i < len(set):
        if set[i] == '(' or set[i] == '{' or set[i] == '[':
            if i == 0:
                ignore += 1
                subs.append([])
                set = set[1:]
                i = -1
        elif set[i] == ')' or set[i] == '}' or set[i] == ']':
            if i > 0:
                subs[ignore-1].append(set[:i])
                set = set[i+1:]
            if i == 0:
                set = set[1:]
            i = -1
            if ignore == 1:
                setDef.append(subs[ignore-1])
            else:
                subs[ignore-2].append(subs[ignore-1])
            subs.pop()
            ignore -= 1
        elif set[i] == ',':
            if i > 0:
                if ignore == 0:
                    setDef.append(set[:i])
                    set = set[i+1:]
                    i = -1
                else:
                    subs[ignore-1].append(set[:i])
                    set = set[i+1:]
                    i = -1
            else:
                set = set[1:]
                i = -1
        elif i == len(set)-1:
            setDef.append(set)
        i += 1
    os.system("cls")
    return setDef
    # except:
    #    print("Hubo un error en la entrada")
    return -1

def PrintASet(lst, sub=False):
    strR = ""
    if len(lst) == 0:
        #print("{}", end="")
        return "{}"
    if sub:
        #print("(", end="")
        strR = strR+"("
    else:
        #print("{", end="")
        strR = strR+"{"
    for element in range(len(lst)-1):
        # print(type(element),end="")
        if type(lst[element]) == list:
            #PrintASet(lst[element], True)
            strR = strR+PrintASet(lst[element], True)+", "
            #print(", ", end="")
        else:
            #print(lst[element], end=", ")
            strR = strR+str(lst[element])+", "
    if type(lst[len(lst)-1]) == list:
        #PrintASet(lst[len(lst)-1], True)
        strR = strR+PrintASet(lst[len(lst)-1], True)
    else:
        #print(lst[len(lst)-1], end="")
        strR = strR+str(lst[len(lst)-1])
    if sub:
        #print(")", end="")
        strR = strR+")"
    else:
        # print("}")
        strR = strR+"}"
    clp.copy(strR[1:-1])
    return strR


def GeneratePrimes(num):
    os.system("cls")
    print("Espere mientras se generan los primos...")
    #global primes
    primes = []
    primesTmp = ones(num+1, dtype=int)
    primesTmp[0] = primesTmp[1] = 0
    for i in range(2, num+1):
        if primesTmp[i] == 1:
            primes.append(i)
            for j in range(2*i, num+1, i):
                primesTmp[j] = 0
    os.system("cls")
    return primes


def ObtainSub(number):
    base = u'\u208D'
    for i in str(number):
        base += '{}'.format(chr(0x2080+int(i)))
    base += u'\u208E'
    return base


def ObtainSup(number):
    base = ""
    for i in str(number):
        if i == '0' or i >= '4':
            base += '{}'.format(chr(0x2070+int(i)))
        elif i == '1':
            base += '{}'.format(chr(0x00B9))
        else:
            base += '{}'.format(chr(0x00B0+int(i)))
    return base


def BaseChangeToTenAlgorythm(number, base):
    res = []
    number = str(number)
    for i in number:
        if i in string.ascii_letters:
            res.append(ord(i)-55)
        else:
            res.append(int(i))
    res = res[::-1]
    res2 = 0
    txt1 = number+ObtainSub(base)+" = "
    txt2 = number+ObtainSub(base)+" = "
    for i in range(len(res)):
        res2 += res[i]*(base**i)
        txt1 = txt1+str(res[i])+"*"+str(base)+ObtainSup(i)
        txt2 = txt2+str(res[i])+"*"+str(base**i)
        if i < len(res)-1:
            txt1 = txt1+" + "
            txt2 = txt2+" + "
    print(txt1)
    print(txt2)
    print(number+ObtainSub(base)+" = "+str(res2)+ObtainSub(10))
    return res2


def BaseChangeAlgorythm(number, base):
    q = 1
    res = []
    number=int(number)
    number2 = number
    nL = len(str(number))
    qL = len(str(int(number/base)))
    while q > 0:
        q = int(number/base)
        r = number - base * q
        if r >= 10:
            r = chr(55+r)
        print(str(number)+" "*(nL-len(str(number))) + " = " + str(base) +
              "(" + str(q) + ")"+" "*(qL-len(str(q))) + " + " + str(r))
        number = q
        res.append(r)
    j = 1
    res = res[::-1]
    print(str(number2)+ObtainSub(10)+" = ", end="")
    finalNum = ""
    for i in res:
        finalNum += str(i)
    print(finalNum, end="")
    print(ObtainSub(base))
    return finalNum
