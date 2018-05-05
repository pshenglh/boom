# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'procs.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from data_process import handle_source_file, get_LB
import os

class Ui_Form(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.files = []
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(741, 632)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(27, 20, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 20, 112, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(313, 20, 112, 34))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(457, 20, 112, 34))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(600, 20, 112, 34))
        self.pushButton_5.setObjectName("pushButton_5")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 60, 707, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(30, 130, 311, 471))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 309, 469))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 321, 481))
        self.textBrowser.setObjectName("textBrowser")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(Form)
        self.scrollArea_2.setGeometry(QtCore.QRect(370, 130, 331, 471))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 329, 469))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 341, 481))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 90, 241, 18))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(410, 90, 241, 18))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(lambda :self.get_dir())
        self.pushButton_2.clicked.connect(lambda :self.get_files())
        self.pushButton_3.clicked.connect(lambda :self.data_pro())
        self.pushButton_4.clicked.connect(lambda :self.uniq_values())
        self.pushButton_5.clicked.connect(lambda :self.clean())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "数据处理"))
        self.pushButton.setText(_translate("Form", "选择目录"))
        self.pushButton_2.setText(_translate("Form", "选择文件"))
        self.pushButton_3.setText(_translate("Form", "数据处理"))
        self.pushButton_4.setText(_translate("Form", "特征值"))
        self.pushButton_5.setText(_translate("Form", "清除"))
        self.label.setText(_translate("Form", "文件列表"))
        self.label_2.setText(_translate("Form", "处理结果"))

    def get_files(self):
        files, _ = QFileDialog.getOpenFileNames(self,
                                                '选择文件', './data',)
        if not files: return
        self.files.extend(files)
        for f in files:
            self.textBrowser.append(os.path.basename(f))

    def get_dir(self):
        d = QFileDialog.getExistingDirectory(self,
                                             '选择目录', './')
        if not d: return
        files = os.listdir(d)
        for f in files:
            self.textBrowser.append(f)
            self.files.append(os.path.join(d, f))

    def clean(self):
        self.files = []
        self.textBrowser.setText('')
        self.textBrowser_2.setText('')

    def data_pro(self):
        for f in self.files:
            basedir, file = os.path.split(f)
            r = handle_source_file(basedir, file)
            if r: self.textBrowser_2.append(r)

    def uniq_values(self):
        if len(self.files) == 0:
            rst = ['选择文件']
        else:
            rst = get_LB(os.path.dirname(self.files[0]))
        for r in rst:
            self.textBrowser_2.append(r)

