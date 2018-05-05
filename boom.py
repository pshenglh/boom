# encoding:utf8

from PyQt5 import QtWidgets
from gui_function import GuiFunction
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = GuiFunction()
    myshow.show()
    sys.exit(app.exec_())