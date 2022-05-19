import os

import readchar
import pyperclip as clp
from numpy import ones

primes = []


def RequestASet(id):
    """Funcion auxiliar"""
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
    global primes
    primes = []
    primesTmp = ones(num+1, dtype=int)
    primesTmp[0] = primesTmp[1] = 0
    for i in range(2, num+1):
        if primesTmp[i] == 1:
            primes.append(i)
            for j in range(2*i, num+1, i):
                primesTmp[j] = 0
    os.system("cls")


def Cartesian():
    sets = input("¿Cuántos conjuntos desea operar?: ")
    if sets == "":
        sets = 2
    else:
        sets = int(sets)
        if sets <= 0:
            return 0
    strR = "Conj1"
    lst = []
    lstSets = [RequestASet("1")]
    for i in range(1, sets):
        lstSets.append(RequestASet(str(i+1)))
    x = lstSets[0]
    for conj in range(1, sets):
        y = lstSets[conj]
        for i in range(len(x)):
            for j in range(len(y)):
                lst.append([x[i], y[j]])
        strR = "("+strR+" X Conj"+str(conj+1)+")"
        print("-> "+strR+": ", PrintASet(lst))
        x = lst
        lst = []


def PowerSet():
    fullset = RequestASet("1")
    listsub = list(fullset)
    subsets = []
    for i in range(2**len(listsub)):
        subset = []
        for k in range(len(listsub)):
            if i & 1 << k:
                subset.append(listsub[k])
        subsets.append(subset)
    for i in range(1, len(subsets)):
        j = i
        while len(subsets[j]) < len(subsets[j-1]) and j-1 > 0:
            subsets[j-1], subsets[j] = subsets[j], subsets[j-1]
            j -= 1
    print("P(Conj1): "+PrintASet(subsets))


def SetsCardinality():
    set = RequestASet("1")
    print("|Conj1|: ", len(set))


def Gcd():
    print("MCD(a, b)")
    a = int(input("Ingrese a -> "))
    b = int(input("Ingrese b -> "))
    print("\nMCD("+str(a)+", "+str(b)+") = ", end="")
    if a < 0 or b < 0:
        a = abs(a)
        b = abs(b)
        print("MCD("+str(a)+", "+str(b)+") = ", end="")
    if a < b:
        a, b = b, a
        print("MCD("+str(a)+", "+str(b)+") = ", end="")
    print("\n")
    c = a % b
    aL = len(str(a))
    bL = len(str(b))
    cL = len(str(c))
    divL = len(str(int(a/b)))
    print(str(a)+" "*(aL-len(str(a)))+" = "+str(b)+" "*(bL-len(str(b)))+"(" +
          str(int(a/b))+" "*(divL-len(str((int(a/b)))))+") + "+str(c)+" "*(cL-len(str(c))))
    while c != 0:
        a, b = b, c
        c = a % b
        print(str(a)+" "*(aL-len(str(a)))+" = "+str(b)+" "*(bL-len(str(b)))+"(" +
              str(int(a/b))+" "*(divL-len(str((int(a/b)))))+") + "+str(c)+" "*(cL-len(str(c))))
    print("\nMCD(a, b) =", abs(b), end="")


def Decompose():
    global primes
    descomposicion = []
    try:
        a = input("Ingrese el numero que desea descomponer: ")
        a = int(float(a))
        a = abs(a)
    except:
        a = 0

    a2 = str(a)
    table=""
    p = 1
    q = 0
    if a > 1:
        GeneratePrimes(a)
        cont=1
        while q != 1:
            for i in primes:
                # print((int(a/i)==a/i))
                # if ((i <= a) and (int(a/i) == a/i)):
                if ((i <= a) and a % i == 0):
                    table=table+(" "*(len(a2)-len(str(int(a))))+str(int(a))+"|"+str(i)+"\n")
                    print(str(cont)+"-> "+"a = "+str(int(a))+", p = "+str(i)+", q = "+str(int(a/i)))
                    p = i
                    q = a/p
                    descomposicion.append(str(p))
                    a = q
                    cont+=1
                    break
        table = table+(" "*(len(a2)-1)+"1"+"|"+"\n")
        print("\n-------------------------\n")
        print(table, end="")
        print("\n-------------------------\n")
        print(a2+" = ", end="")
        for i in range(len(descomposicion)-1):
            print(descomposicion[i]+"*", end="")
        print(descomposicion[len(descomposicion)-1]+"\n")
    else:
        print("No es posible descomponer el numero que ingresaste")


if __name__ == "__main__":
    Decompose()
