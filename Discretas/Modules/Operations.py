from Modules.AuxFunctions import *
#from AuxFunctions import *


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
    primes=[]
    descomposicion = []
    try:
        a = input("Ingrese el numero que desea descomponer: ")
        a = int(float(a))
        a = abs(a)
    except:
        a = 0

    a2 = str(a)
    table = ""
    p = 1
    q = 0
    if a > 1:
        primes=GeneratePrimes(a)
        cont = 1
        while q != 1:
            for i in primes:
                # print((int(a/i)==a/i))
                # if ((i <= a) and (int(a/i) == a/i)):
                if ((i <= a) and a % i == 0):
                    table = table+(" "*(len(a2)-len(str(int(a)))
                                        )+str(int(a))+"|"+str(i)+"\n")
                    print(str(cont)+"-> "+"a = "+str(int(a)) +
                          ", p = "+str(i)+", q = "+str(int(a/i)))
                    p = i
                    q = a/p
                    descomposicion.append(str(p))
                    a = q
                    cont += 1
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


def BaseChangeGeneralAlgorythm():
    number = input("Ingresa el número a cambiar de base -> ")
    numberRes = number
    base = input("Ingresa la base del número original -> ")
    base2 = input("Ingresa la base a la que lo quieres cambiar -> ")
    print("\n", end="")
    if base != "10":
        print("\nConversión de base "+str(base)+" a base 10:\n")
        numberRes = BaseChangeToTenAlgorythm(numberRes, int(base))
    if base2 != "10":
        print("\nConversión de base 10 a base "+str(base2)+":\n")
        numberRes = BaseChangeAlgorythm(numberRes, int(base2))
    print("\n")
    print(str(number)+ObtainSub(base)+" = "+str(numberRes)+ObtainSub(base2))


if __name__ == "__main__":
    pass
