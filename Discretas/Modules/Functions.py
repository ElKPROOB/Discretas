import os
import csv

from Modules.Operations import *


def Execute(Id):
    os.system("cls")
    if Id == "01":
        PowerSet()
    elif Id == "02":
        Cartesian()
    elif Id == "03":
        SetsCardinality()
    elif Id == "04":
        Gcd()
    elif Id == "05":
        Decompose()
    input("\nPresione cualquier tecla para continuar...")


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


"""def ListOperations():
    operationsDict = ReadCSV('Discretas/Files/Operations.csv')
    operations = ""
    for i in operationsDict.keys():
        operations += operationsDict[i][0] + ": " + \
            operationsDict[i][1] + " - " + \
            operationsDict[i][2] + "\n"
    return operations"""


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
    if retLim_t:
        return j
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
