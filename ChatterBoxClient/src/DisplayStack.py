import sys
from PyQt4 import QtGui, QtCore
#from test_ui import Ui_Form


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        # self.ui = Ui_Form()
        self.ui.setupUi(self)