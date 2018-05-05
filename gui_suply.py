from gui import Ui_Form
from PyQt5 import QtWidgets

class Gui(QtWidgets.QWidget, Ui_Form):
    '''该类继承由ui文件直接生成的py文件，补充直接生成文件
    到可运行文件中所需的部分，就可以在做修改gui的时候直接
    替换相关的py文件，不用在对代码作补充'''

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Form):
        Ui_Form.setupUi(self, Form)

