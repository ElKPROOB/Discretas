from AuxFunctions import *


def SumNumbers(lst, base):
    if base < 2:
        return -3
    lst.sort(key=len, reverse=True)
    maxL = len(lst[0])
    resd = 0
    sobr = 0
    res = []
    strResd=[]
    cantRes=0
    minCant=maxL+1
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
        cantRes=minCant
    strResd=strResd[::-1]
    strResd=NumInBaseTenToBaseX(strResd)
    for i in range(len(lst)):
        strResd+="\n"+" "*(cantRes-len(lst[i]))+lst[i]
    strResd+="\n"+"-"*(cantRes)
    res = res[::-1]
    res = NumInBaseTenToBaseX(res)
    strResd += "\n"+" "*(cantRes-len(res))+res
    print(strResd)


if __name__ == "__main__":
    SumNumbers(["34243","42342","44324","34214","34213"],5)
    # SumNumbers(["34243","4234","443","34","3"],5)
    # SumNumbers(["57A2", "8B26", "7A57", "BABA"], 13)
    # SumNumbers(["2222","1"], 13)
    # SumNumbers(["2313","1324"], 5)
