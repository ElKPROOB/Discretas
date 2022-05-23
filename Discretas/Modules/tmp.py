from AuxFunctions import *


def SimpleDivision(lst, base):
    lst = lst[::-1]
    resul = 0
    resulResd = "0"
    sumando = lst[1]
    ignore, resulRes = SubtractNumbers(lst, base)
    while(resulRes[0] != '-'):
        resulResd = resulRes
        resul += 1
        ignore, lst[1] = SumNumbers([lst[1], sumando], base)
        ignore, resulRes = SubtractNumbers(lst, base)
    ignore, resul = BaseChangeAlgorythm(resul, base)
    resd = ""
    ceroI = True
    for i in range(len(resulResd)):
        if resulResd[i] == '0':
            if ceroI:
                continue
            else:
                resd += '0'
        else:
            ceroI = False
            resd += resulResd[i]
    if resd == "":
        resd = "0"
    return resul, resd


def DivideNumbers(lst, base):
    divisor = lst[0]
    dividendo = ""
    lstCoc = []
    strBase= ObtainSub(base)
    strRes = ""
    strRes2 = ""
    resd="0"
    primDiv=False
    for i in range(len(lst[1])):
        dividendo += lst[1][i]
        cociente, ignore = SimpleDivision([divisor, dividendo], base)
        if cociente == "0" and primDiv==False:
            lstCoc.append(" ")
        else:
            if primDiv:
                strRes2 += dividendo+"\n"
            else:
                primDiv = True
            lstCoc.append(cociente)
            ignore, resulMult = MultiplyNumbers([cociente, divisor], base)
            strRes2 += " "*((len(divisor)+len(strBase)+1+i)-(len(resulMult)))+"-"+resulMult+"\n"
            ignore, dividendo = SubtractNumbers([dividendo, resulMult], base)
            strRes2 += "-"*(len(divisor)+len(strBase)+len(lst[1])+1)+"\n"
            strRes2 += " "*((len(divisor)+len(strBase)+2+i)-(len(dividendo)))
            if i == len(lst[1])-1:
                resd = ""
                ceroI = True
                for i in range(len(dividendo)):
                    if dividendo[i] == '0':
                        if ceroI:
                            resd+=' '
                        else:
                            resd += '0'
                    else:
                        ceroI = False
                        resd += dividendo[i]
                if resd == (" "*len(resd)):
                    resd = resd[:-1]+"0"
                strRes2 += resd
    strRes = " "*(len(divisor)+1+len(strBase)) + "".join(lstCoc) + strBase + "\n" + " " * (len(divisor)+1+len(strBase)) + "_"*len(lst[1]) + "\n" + divisor + strBase + "|" + lst[1] + strBase + "\n"+strRes2+" <- residuo"
    resd = "Cociente: " + "".join(lstCoc)  + " Residuo: " + resd.replace(" ", "")
    return strRes, resd


if __name__ == "__main__":
    # resul, resRet = MultiplyNumbers(["D040", "AA"], 16)
    # print(resul, resRet)
    # res, resd = SimpleDivision(["2", "4563"], 7)
    # print(res, resd)
    res, resd = DivideNumbers(["42", "60322"], 8)
    #res, resd=SimpleDivision(["10", "11001100"], 2)
    print(res+"\n"+ resd)
    pass
