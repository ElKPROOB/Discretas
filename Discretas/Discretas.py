import os

import readchar

from Modules.Functions import *


if __name__ == "__main__":
    identifier = 0
    userInput = ""
    suggestion = ""
    content = ReadCSV('Discretas/Files/Operations.csv')
    maxId = len(content)
    while True:
        try:
            if maxId > 0:
                identifier = identifier % maxId
            else:
                identifier = 0
            os.system("cls")
            print("Seleccione la operación que desea realizar: " + suggestion + "\n" +
                  Suggestions(content, suggestion, identifier, False, False))
            userInput = readchar.readkey()
            if userInput == "\r":
                Execute(Suggestions(content, suggestion, identifier, False, True))
            elif userInput == "\x08":
                suggestion = suggestion[:-1]
            elif userInput == "\x1b":
                break
            elif userInput == readchar.key.DOWN:
                identifier = (identifier + 1) % maxId
            elif userInput == readchar.key.UP:
                identifier = (identifier - 1) % maxId
            elif ord(userInput) > 31 and ord(userInput) < 127:
                suggestion += userInput
                
            maxId = Suggestions(content, suggestion, identifier, True, False)
        except:
            pass
