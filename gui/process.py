# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'process.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProcessDialog(object):
    def setupUi(self, ProcessDialog):
        ProcessDialog.setObjectName("ProcessDialog")
        ProcessDialog.resize(416, 332)
        self.pushButton = QtWidgets.QPushButton(ProcessDialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 290, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(ProcessDialog)
        self.widget.setGeometry(QtCore.QRect(30, 40, 361, 231))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.ProcessList = QtWidgets.QListWidget(self.widget)
        self.ProcessList.setObjectName("ProcessList")
        self.verticalLayout.addWidget(self.ProcessList)

        self.retranslateUi(ProcessDialog)
        QtCore.QMetaObject.connectSlotsByName(ProcessDialog)

    def retranslateUi(self, ProcessDialog):
        _translate = QtCore.QCoreApplication.translate
        ProcessDialog.setWindowTitle(_translate("ProcessDialog", "进度"))
        self.pushButton.setText(_translate("ProcessDialog", "确定"))
        self.label.setText(_translate("ProcessDialog", "转换进度:"))

