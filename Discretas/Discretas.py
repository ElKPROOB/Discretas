import os

from Modules.Functions import *


if __name__ == "__main__":
    index = 0
    code = 0
    identifier = 0
    suggestion = ""
    content = ReadCSV('Discretas/Files/Operations.csv')
    maxId = len(content)
    while True:
        if maxId > 0:
            identifier = identifier % maxId
        else:
            identifier = 0
        os.system("cls")
        if index == 0:
            print("Seleccione la operación que desea realizar: " + suggestion +
                  "\n" + Suggestions(content, suggestion, identifier, False, False))
        else:
            print("Seleccione la operación que desea realizar: " + (suggestion[:len(suggestion)+index] + "|" + suggestion[len(
                suggestion)+index:]) + "\n" + Suggestions(content, suggestion, identifier, False, False))
        code, suggestion, index = RequestData(suggestion, index)
        if code == 1:
            Execute(Suggestions(content, suggestion, identifier, False, True))
        elif code == -1:
            break
        elif code == 2:
            identifier = (identifier + 1) % maxId
        elif code == 3:
            identifier = (identifier - 1) % maxId
        maxId = Suggestions(content, suggestion, identifier, True, False)
