from gui_suply import Gui, ConfigDialog, InfoDialog
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from data_process import CurveData, DataProcess
from data_process import config
import os


class ConfigDialogFunction(ConfigDialog):
    def __init__(self):
        super().__init__()
        self.textEdit.setText(str(config.B_low))
        self.textEdit_2.setText(str(config.B_high))

    def accept(self):
        low = float(self.textEdit.toPlainText())
        hight = float(self.textEdit_2.toPlainText())
        if low >= hight:
            return
        else:
            config.B_low = low
            config.B_high = hight
        config.save()
        self.close()

class GuiFunction(Gui):
    '''该类继承可运行的gui的Py文件，主要功能为对gui空间行为
    进行定义'''

    def __init__(self):
        super().__init__()
        self.files = []
        self.config_dialog = ConfigDialogFunction()
        self.info_dialog = InfoDialog()
        self.row_count = 0

    def setupUi(self, Form):
        Gui.setupUi(self, Form)
        self.ChooseDir.triggered.connect(lambda: self.get_dir())
        self.ChooseFile.triggered.connect(lambda: self.get_files())
        self.CurveFiles.triggered.connect(lambda: self.data_process())
        self.FeatureValue.triggered.connect(lambda: self.uniq_values())
        self.CleanResult.triggered.connect(lambda: self.clean_results())
        self.CleanAll.triggered.connect(lambda: self.clean_all())
        self.B0Set.triggered.connect(lambda: self.show_config_dialog())
        self.Info.triggered.connect(lambda: self.show_info_dialog())

    def show_config_dialog(self):
        self.config_dialog.show()

    def show_info_dialog(self):
        self.info_dialog.show()

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

    def clean_all(self):
        self.files = []
        self.FileList.setText('')
        # self.ResultTable.clear()
        for r in range(self.ResultTable.rowCount(), 0, -1):
            self.ResultTable.removeRow(r)
        self.row_count = 0

    def clean_results(self):
        # self.ResultTable.clear()
        for r in range(self.ResultTable.rowCount(), 0, -1):
            self.ResultTable.removeRow(r)
        self.row_count = 0

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
        for f in self.files:
            filename = os.path.basename(f)
            try:
                data_proceser = DataProcess(f)
                datas = data_proceser.LB_data()

                if self.row_count == 0:
                    try:
                        for j, d in enumerate(datas):
                            item = self.ResultTable.verticalHeaderItem(0)
                            item.setText(_translate("Form", filename))
                            item = self.ResultTable.item(0, j)
                            item.setText(_translate("Form", str(round(d, 4))))
                        item = self.ResultTable.item(0, j+1)
                        item.setText(_translate("Form", '{}-{}'.format(config.B_low, config.B_high)))
                    except:
                        for j, d in enumerate(datas):
                            self.ResultTable.setItem(0, j, QtWidgets.QTableWidgetItem(str(round(d, 4))))
                        self.ResultTable.setItem(0, j+1, QtWidgets.QTableWidgetItem('{}-{}'.format(config.B_low, config.B_high)))
                        self.ResultTable.setVerticalHeaderItem(0, QtWidgets.QTableWidgetItem(filename))
                else:
                    rows = self.ResultTable.rowCount()
                    self.ResultTable.insertRow(rows)
                    for j, d in enumerate(datas):
                        self.ResultTable.setItem(rows, j, QtWidgets.QTableWidgetItem(str(round(d, 4))))
                    self.ResultTable.setItem(rows, j + 1,
                                             QtWidgets.QTableWidgetItem('{}-{}'.format(config.B_low, config.B_high)))
                    self.ResultTable.setVerticalHeaderItem(rows, QtWidgets.QTableWidgetItem(filename))
                self.row_count += 1
            except Exception as err:
                raise err
