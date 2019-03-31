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
        ConfigDialog.resize(469, 225)
        self.BconfigLabel = QtWidgets.QLabel(ConfigDialog)
        self.BconfigLabel.setGeometry(QtCore.QRect(71, 94, 96, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BconfigLabel.setFont(font)
        self.BconfigLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.BconfigLabel.setObjectName("BconfigLabel")
        self.textEdit = QtWidgets.QTextEdit(ConfigDialog)
        self.textEdit.setGeometry(QtCore.QRect(176, 91, 81, 31))
        self.textEdit.setObjectName("textEdit")
        self.line = QtWidgets.QFrame(ConfigDialog)
        self.line.setGeometry(QtCore.QRect(267, 89, 31, 39))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textEdit_2 = QtWidgets.QTextEdit(ConfigDialog)
        self.textEdit_2.setGeometry(QtCore.QRect(310, 91, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(ConfigDialog)
        self.label.setGeometry(QtCore.QRect(70, 47, 156, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit_3 = QtWidgets.QTextEdit(ConfigDialog)
        self.textEdit_3.setGeometry(QtCore.QRect(237, 42, 161, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.buttonBox = QtWidgets.QDialogButtonBox(ConfigDialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 150, 241, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.raise_()
        self.BconfigLabel.raise_()
        self.textEdit.raise_()
        self.line.raise_()
        self.textEdit_2.raise_()
        self.label.raise_()
        self.textEdit_3.raise_()
        self.buttonBox.raise_()

        self.retranslateUi(ConfigDialog)
        self.buttonBox.accepted.connect(ConfigDialog.accept)
        self.buttonBox.rejected.connect(ConfigDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigDialog)

    def retranslateUi(self, ConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        ConfigDialog.setWindowTitle(_translate("ConfigDialog", "配置"))
        self.BconfigLabel.setText(_translate("ConfigDialog", "B值范围:"))
        self.label.setText(_translate("ConfigDialog", "结果小数位数:"))

