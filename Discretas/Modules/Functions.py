import os
import csv

import readchar

from Modules.Operations import *


def RequestData(str, index=0):
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
        elif userInput == readchar.key.DOWN:
            code = 2
        elif userInput == readchar.key.UP:
            code = 3
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


def Execute(Id):
    os.system("cls")
    if type(Id) == int:
        if Id == -4:
            return -4
    if Id == "01":
        strR = PowerSet()
        if type(strR) == str:
            strR = strR[1:-1]
    elif Id == "02":
        strR = Cartesian()
        if type(strR) == str:
            strR = strR[1:-1]
    elif Id == "03":
        strR = SetsCardinality()
    elif Id == "04":
        strR = Gcd()
    elif Id == "05":
        strR = Decompose()
    elif Id == "06":
        strR = BaseChangeGeneralAlgorythm()
    elif Id == "07":
        strR = Sum()
    elif Id == "08":
        strR = Sub()
    elif Id == "09":
        strR = Mult()
    elif Id == "10":
        strR = Div()
    if type(strR) == str:
        clp.copy(strR)
        print("\nResultado copiado al portapapeles\n\n")
    elif strR == -1:
        return -1
    elif strR == -2:
        print("\nError en la ejecución, comprueba que has introducido los datos correctamente\n\n")
    elif strR == -3:
        print("\nSe han detectado algunos errores en los datos ingresados\n\n")
    input("\nPresione ENTER para continuar...")


def ReadCSV(route):
    dictionary = {}
    csv.register_dialect('personal', delimiter=';',
                         quotechar='"', quoting=csv.QUOTE_ALL)
    with open(route) as csvfile:
        content = csv.reader(csvfile, dialect='personal')
        for data in content:
            lst = []
            for subData in data:
                lst.append(subData)
            lst = list(lst)
            aux = str(lst[0])
            if aux != "ID":
                dictionary[aux] = lst[1:]
    csvfile.close()
    return dictionary


def Suggestions(dictionary, suggestion, identifier, retLim_t, retElemID_t):
    suggestions = ""
    i = j = 0
    for key, value in dictionary.items():
        if PurifyTxt(suggestion) in PurifyTxt(key) or PurifyTxt(suggestion) in PurifyTxt(value[0]):
            j += 1
            if i == identifier:
                if retElemID_t:
                    return key
                suggestions += "->"
                suggestions += key + ": " + \
                    value[0] + " - " + value[1] + " - " + value[2] + "\n"
            else:
                suggestions += "  "
                suggestions += key + ": " + value[0] + " - " + value[1] + "\n"
            i += 1
    suggestions += "  ESC: Salir\n"
    if retLim_t:
        return j
    if retElemID_t:
        return -4
    return suggestions


def PurifyTxt(text1: str = " ", strip: bool = True, change: bool = True,
              upp_f_low_t: bool = True, removeAccents: bool = True,
              prohiC_f_permiC_t: bool = True,
              chars: list = ["+ áéíóúñ", [97, 122], [65, 90], [48, 57]]) -> str:
    text2 = ""
    if strip == True:
        text1 = text1.strip()
    if change == True:
        if upp_f_low_t == True:
            text1 = text1.lower()
        else:
            text1 = text1.upper()
    if removeAccents == True:
        text1 = text1.replace("á", "a")
        text1 = text1.replace("é", "e")
        text1 = text1.replace("í", "i")
        text1 = text1.replace("ó", "o")
        text1 = text1.replace("ú", "u")
        text1 = text1.replace("ñ", "n")
    if prohiC_f_permiC_t == True:
        for i in range(len(text1)):
            if text1[i] in chars[0]:
                text2 += text1[i]
                continue
            else:
                for j in range(len(chars)):
                    if j > 0:
                        lim_i = chars[j][0]
                        lim_s = chars[j][1]
                        if ord(text1[i]) >= lim_i and ord(text1[i]) <= lim_s:
                            text2 += text1[i]
                            break
    else:
        for i in range(len(text1)):
            adding = True
            if text1[i] in chars[0]:
                continue
            else:
                for j in range(len(chars)):
                    if j > 0:
                        lim_i = chars[j][0]
                        lim_s = chars[j][1]
                        if ord(text1[i]) >= lim_i and ord(text1[i]) <= lim_s:
                            adding = False
                            break
            if adding == True:
                text2 += text1[i]
    return text2
