from gui_suply import Gui
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from data_process import CurveData, DataProcess
import os

class GuiFunction(Gui):
    '''该类继承可运行的gui的Py文件，主要功能为对gui空间行为
    进行定义'''

    def __init__(self):
        super().__init__()
        self.files = []

    def setupUi(self, Form):
        Gui.setupUi(self, Form)
        self.ChooseDir.triggered.connect(lambda: self.get_dir())
        self.ChooseFile.triggered.connect(lambda: self.get_files())
        self.CurveFiles.triggered.connect(lambda: self.data_process())
        self.FeatureValue.triggered.connect(lambda: self.uniq_values())
        self.CleanMenu.triggered.connect(lambda: self.clean())


    def get_files(self):
        files, _ = QFileDialog.getOpenFileNames(self,
                                                '选择文件', './data', )
        if not files: return
        self.files.extend(files)
        for f in files:
            self.FileList.append(os.path.basename(f))

    def get_dir(self):
        d = QFileDialog.getExistingDirectory(self,
                                             '选择目录', './')
        if not d: return
        files = os.listdir(d)
        for f in files:
            self.FileList.append(f)
            self.files.append(os.path.join(d, f))

    def clean(self):
        self.files = []
        self.FileList.setText('')
        self.ResultList.setText('')

    def data_process(self):
        dist_dir = QFileDialog.getExistingDirectory(self,
                                                '选择保存目录', './')
        for f in self.files:
            source_dir, file_name = os.path.split(f)
            try:
                curve_data = CurveData(f)
                curve_data.get_data()
                curve_data.all_curve_files(dist_dir, file_name)
                r = '%s..........done' % file_name
                if r: self.ResultList.append(r)
            except Exception as e:
                continue

    def uniq_values(self):
        _translate = QtCore.QCoreApplication.translate
        for i, f in enumerate(self.files):
            filename = os.path.basename(f)
            try:
                data_proceser = DataProcess(f)
                datas = data_proceser.LB_data()
                if i == 0:
                    for j, d in enumerate(datas):
                        item = self.ResultTable.verticalHeaderItem(0)
                        item.setText(_translate("Form", filename))
                        item = self.ResultTable.item(i, j)
                        item.setText(_translate("Form", str(round(d, 4))))
                elif i > 0:
                    rows = self.ResultTable.rowCount()
                    self.ResultTable.insertRow(rows)
                    for j, d in enumerate(datas):
                        self.ResultTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(round(d, 4))))
                    self.ResultTable.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem(filename))
            except Exception as err:
                raise err
