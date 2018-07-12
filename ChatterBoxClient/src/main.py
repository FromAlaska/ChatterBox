from NetworkStack import *
from SavedIPAddressStack import *
from DisplayStack import *
from PyQt4 import QtGui
import sys

if __name__ == "__main__":
    # Advanced input commands using sys.argv
    # if(argc > 0):
    #     startConnection(sys.argv)

    # Check for input from the user
    AskUserForYes = raw_input("Would you like to connect to the server? (y/n)")
    ifValidAnswer = True
    invalidAnswerCounter = 0

    while (ifValidAnswer == True):
        if(AskUserForYes == "y" or AskUserForYes == "Y"):
            startConnection()
            ifValidAnswer = False
        if(invalidAnswerCounter == 2):
            break
        else:
            AskUserForYes = input("Would you like to connect to the server? (y/n)")
            invalidAnswerCounter = invalidAnswerCounter + 1

    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())