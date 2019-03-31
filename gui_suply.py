from gui.gui_bak import Ui_Form
from gui.config import Ui_ConfigDialog
from gui.info import Ui_InfoDialog
from gui.process import Ui_ProcessDialog
from PyQt5 import QtWidgets

class Gui(QtWidgets.QMainWindow, Ui_Form):
    '''该类继承由ui文件直接生成的py文件，补充直接生成文件
    到可运行文件中所需的部分，就可以在做修改gui的时候直接
    替换相关的py文件，不用在对代码作补充'''

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.ResultTable.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.ResultTable.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.ResultTable.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.ResultTable.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.retranslateUi(self)

    def setupUi(self, Form):
        Ui_Form.setupUi(self, Form)


class ConfigDialog(QtWidgets.QDialog, Ui_ConfigDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, ConfigDialog):
        Ui_ConfigDialog.setupUi(self, ConfigDialog)


class InfoDialog(QtWidgets.QDialog, Ui_InfoDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, ConfigDialog):
        Ui_InfoDialog.setupUi(self, ConfigDialog)


class ProcessDialog(QtWidgets.QDialog, Ui_ProcessDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        self.retranslateUi(self)

    def setupUi(self, ConfigDialog):
        Ui_ProcessDialog.setupUi(self, ConfigDialog)
