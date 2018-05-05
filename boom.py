# encoding:utf8

from PyQt5 import QtWidgets
from procs import Ui_Form
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = Ui_Form()
    myshow.show()
    sys.exit(app.exec_())