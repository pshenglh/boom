# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfigDialog(object):
    def setupUi(self, ConfigDialog):
        ConfigDialog.setObjectName("ConfigDialog")
        ConfigDialog.resize(431, 202)
        self.buttonBox = QtWidgets.QDialogButtonBox(ConfigDialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 150, 241, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.BconfigLabel = QtWidgets.QLabel(ConfigDialog)
        self.BconfigLabel.setGeometry(QtCore.QRect(50, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BconfigLabel.setFont(font)
        self.BconfigLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.BconfigLabel.setObjectName("BconfigLabel")
        self.textEdit = QtWidgets.QTextEdit(ConfigDialog)
        self.textEdit.setGeometry(QtCore.QRect(170, 70, 71, 31))
        self.textEdit.setObjectName("textEdit")
        self.line = QtWidgets.QFrame(ConfigDialog)
        self.line.setGeometry(QtCore.QRect(250, 80, 41, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textEdit_2 = QtWidgets.QTextEdit(ConfigDialog)
        self.textEdit_2.setGeometry(QtCore.QRect(300, 70, 71, 31))
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(ConfigDialog)
        self.buttonBox.accepted.connect(ConfigDialog.accept)
        self.buttonBox.rejected.connect(ConfigDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigDialog)

    def retranslateUi(self, ConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        ConfigDialog.setWindowTitle(_translate("ConfigDialog", "配置"))
        self.BconfigLabel.setText(_translate("ConfigDialog", "B值范围:"))

