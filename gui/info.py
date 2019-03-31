# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InfoDialog(object):
    def setupUi(self, InfoDialog):
        InfoDialog.setObjectName("InfoDialog")
        InfoDialog.resize(478, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(InfoDialog)
        self.buttonBox.setGeometry(QtCore.QRect(130, 230, 241, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(InfoDialog)
        self.label.setGeometry(QtCore.QRect(60, 50, 381, 18))
        self.label.setMouseTracking(False)
        self.label.setScaledContents(False)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(InfoDialog)
        self.label_2.setGeometry(QtCore.QRect(140, 90, 221, 18))
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(InfoDialog)
        self.label_3.setGeometry(QtCore.QRect(140, 130, 211, 18))
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(InfoDialog)
        self.label_4.setGeometry(QtCore.QRect(200, 170, 111, 18))
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(InfoDialog)
        self.buttonBox.accepted.connect(InfoDialog.accept)
        self.buttonBox.rejected.connect(InfoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(InfoDialog)

    def retranslateUi(self, InfoDialog):
        _translate = QtCore.QCoreApplication.translate
        InfoDialog.setWindowTitle(_translate("InfoDialog", "关于"))
        self.label.setText(_translate("InfoDialog", "项目地址:https://github.com/pshenglh/boom"))
        self.label_2.setText(_translate("InfoDialog", "如有建议或发现bug请联系："))
        self.label_3.setText(_translate("InfoDialog", "邮箱:psheng@outlook.com"))
        self.label_4.setText(_translate("InfoDialog", "QQ:674799317"))

