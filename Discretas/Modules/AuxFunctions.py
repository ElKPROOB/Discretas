import os
import string

import readchar
import pyperclip as clp
from numpy import ones


def AuxRequestData(str, index=0):
    index2 = len(str)+index
    try:
        code = 0
        userInput = readchar.readkey()
        if userInput == "\r":
            code = 1
        elif userInput == "\x08":
            str2 = str[:index2]
            str2 = str2[:-1]
            str = str2+str[index2:]
        elif userInput == "\x1b":
            code = -1
        elif userInput == readchar.key.LEFT:
            if index2 > 0:
                index -= 1
        elif userInput == readchar.key.RIGHT:
            if index2 < len(str):
                index += 1
        elif userInput == readchar.key.CTRL_V:
            str += clp.paste()
        elif ord(userInput) > 31 and ord(userInput) < 127:
            str = str[:index2] + userInput + str[index2:]
        return code, str, index
    except:
        return -2, str, index


def AuxIterateRequestData(msg="", postMsg=""):
    code = 0
    index = 0
    enter = False
    var = ""
    while True:
        os.system("cls")
        if enter:
            print(
                msg + "(Aún no has escrito nada, presiona ENTER de nuevo para continuar)" + postMsg)
        elif index == 0:
            print(msg + var + postMsg)
        else:
            print(msg+var[:len(var)+index] + "|" + var[len(var)+index:])
        code, var, index = AuxRequestData(var, index)
        if code == 1:
            if var == "":
                if enter:
                    break
                else:
                    enter = True
            else:
                break
        elif code == -1:
            return -1
        else:
            if enter:
                enter = False
    return var


def RequestASet(id):
    index = 0
    code = 0
    set = ""
    while True:
        os.system("cls")
        if index == 0:
            print("Ingrese el conjunto " + id + ": {" + set + "}")
        else:
            print("Ingrese el conjunto " + id +
                  ": {" + set[:len(set)+index] + "|" + set[len(set)+index:] + "}")
        print("Ejemplo de conjunto: {{}, 2, (3, 4), A}")
        code, set, index = AuxRequestData(set, index)
        if code == 1:
            break
        elif code == -1:
            return -1
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


def ObtainSub(number, parenthesis=True):
    base=""
    if parenthesis:
        base = u'\u208D'
    for i in str(number):
        if i == ' ':
            base += ' '
        else:
            base += '{}'.format(chr(0x2080+int(i)))
    if parenthesis:
        base += u'\u208E'
    return base


def ObtainSup(number):
    base = ""
    for i in str(number):
        if i == '0' or i >= '4':
            base += '{}'.format(chr(0x2070+int(i)))
        elif i == '1':
            base += '{}'.format(chr(0x00B9))
        elif i == ' ':
            base += ' '
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
    number = int(number)
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


def NumInBaseXToBaseTen(chr):
    if type(chr) == int:
        return chr
    if ord(chr) >= 48 and ord(chr) <= 57:
        return ord(chr)-48
    elif ord(chr) >= 65 and ord(chr) <= 90:
        return ord(chr)-55
    else:
        return -3


def NumInBaseTenToBaseX(lst):
    num = ""
    for i in lst:
        if i == "":
            num += " "
        elif int(i) < 10:
            num += str(i)
        else:
            num += chr(int(i)+55)
    return num


def SumNumbers(lst, base):
    if base < 2:
        return -3
    lst.sort(key=len, reverse=True)
    maxL = len(lst[0])
    resd = 0
    sobr = 0
    res = []
    strResd = []
    cantRes = 0
    minCant = maxL+1
    for i in range(maxL):
        sum = 0
        sum += resd
        for j in range(len(lst)):
            if len(lst[j])-(i+1) >= 0:
                tmp = NumInBaseXToBaseTen(lst[j][len(lst[j])-(i+1)])
                if tmp == -3:
                    return -3
                sum += int(tmp)
        resd = int(sum/base)
        if resd != 0:
            strResd.append(str(resd))
        else:
            strResd.append("")
        sobr = sum % base
        res.append(str(sobr))
        cantRes += 1
    while int(resd/base) > 0:
        sobr = resd % base
        res.append(str(sobr))
        cantRes += 1
        resd = int(resd/base)
        if resd != 0:
            strResd.append(str(resd))
        else:
            strResd.append("")
    if resd != 0:
        res.append(str(resd))
        cantRes += 1
    if cantRes < minCant:
        cantRes = minCant
    strResd = strResd[::-1]
    strResd = NumInBaseTenToBaseX(strResd)
    strResd=ObtainSub(strResd, False)
    for i in range(len(lst)):
        strResd += "\n"+" "*(cantRes-len(lst[i]))+lst[i]+ObtainSub(base)
    strResd += "\n"+"-"*(cantRes)
    res = res[::-1]
    res = NumInBaseTenToBaseX(res)
    strResd += "\n"+" "*(cantRes-len(res))+res+ObtainSub(base)
    return strResd, res
