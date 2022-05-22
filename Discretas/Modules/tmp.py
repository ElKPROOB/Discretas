from AuxFunctions import *


def MultiplyNumbers(lst, base):
    if base < 2:
        return -3
    if len(lst[0]) < len(lst[1]):
        lst[0], lst[1] = lst[1], lst[0]
    maxL = len(lst[0])
    sums = []
    res = []
    strResd = []
    for i in range(len(lst[1])):
        mult = 0
        resd = 0
        strResd.append([])
        sums.append([])
        termB = NumInBaseXToBaseTen(lst[1][len(lst[1])-(i+1)])
        if termB == -3:
            return -3
        termB = int(termB)
        for j in range(maxL):
            termA = NumInBaseXToBaseTen(lst[0][len(lst[0])-(j+1)])
            if termA == -3:
                return -3
            termA = int(termA)
            mult = (termA*termB)+resd
            sums[i].append(str(mult % base))
            resd = mult//base
            if resd != 0:
                strResd[i].append(str(resd))
            else:
                strResd[i].append("")
        if resd != 0:
            sums[i].append(str(resd))
    maxSL=0
    for i in range(len(sums)):
        sums[i] = NumInBaseTenToBaseX(sums[i], True)
        sums[i] += " "*i
        if len(sums[i]) > maxSL:
            maxSL = len(sums[i])
    maxRL=0
    for i in range(len(strResd)):
        strResd[i] = NumInBaseTenToBaseX(strResd[i], True)
        strResd[i] += " "
        strResd[i] = ObtainSub(strResd[i], False)
        if len(strResd[i]) > maxRL:
            maxRL = len(strResd[i])
    maxT=max(maxSL, maxRL, maxL)
    strRes = ""
    j=0
    for i in range(len(strResd)-1, -1, -1):
        strRes += " "*(maxT-len(strResd[i]))+strResd[i] + \
            " <- residuos del termino \""+lst[1][j]+"\"\n"
        j+=1
    strRes += " "*(maxT-maxL)+lst[0] + ObtainSub(base) + "\n"
    strRes += " "*(maxT-len(lst[1]))+lst[1] + ObtainSub(base)+"\n"
    strRes += "-"*(maxT)+"\n"
    strRes2, res=SumNumbers(sums, base, True)
    if res == -3:
        return -3
    strRes += strRes2
    return strRes, res


if __name__ == "__main__":
    resul, resRet = MultiplyNumbers(["D040", "AA"], 16)
    print(resul, resRet)
    pass
