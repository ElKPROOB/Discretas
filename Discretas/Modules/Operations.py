import os
import pprint

import readchar


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
            elif userInput == "\x08":
                set = set[:-1]
            elif userInput == "\x1b":
                return -1
            elif ord(userInput) > 31 and ord(userInput) < 127:
                set += userInput
        except:
            pass
    try:
        setDef=[]
        ignore=False
        i=0
        while i < len(set):
            if set[i] == '(':
                ignore=True
            elif set[i] == ')':
                ignore=False
            elif set[i] == ',' and not ignore:
                setDef.append(set[:i])
                set=set[i+1:]
                i=-1
            elif i == len(set)-1:
                setDef.append(set)
            i+=1
        return setDef
    except:
        print("Hubo un error en la entrada")
    return -1



def Cartesian():
    x=RequestASet("X")
    y=RequestASet("Y")
    lst = []
    for i in range(len(x)):
        for j in range(len(y)):
            lst.append((x[i], y[j]))
    print(lst)


def PowerSet():
    fullset=RequestASet("1")
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
    print(subsets)


if __name__ == "__main__":
    """a1 = []
    a2 = [1]
    z = Cartesian(a1, a2)
    print("Cartesian: ", z)
    z = PowerSet(z)
    print("Power Set: ", z)
    print("Length: ", len(z))
    print("-----------------------------------------------------")
    a1 = PowerSet(a1)
    print("Power Set a1: ", a1)
    a2 = PowerSet(a2)
    print("Power Set a2: ", a2)
    z1 = Cartesian(a1, a2)
    print("Cartesian: ", z1)
    print("Length: ", len(z1))
    print("-----------------------------------------------------")
    print("z: ", len(z))
    print("z1: ", len(z1))"""
