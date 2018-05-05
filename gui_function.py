from gui_suply import Gui
from PyQt5.QtWidgets import QFileDialog
from data_process import handle_source_file, get_LB
from data_process_new import CurveData
import os

class GuiFunction(Gui):
    '''该类继承可运行的gui的Py文件，主要功能为对gui空间行为
    进行定义'''

    def __init__(self):
        super().__init__()
        self.files = []

    def setupUi(self, Form):
        Gui.setupUi(self, Form)
        self.pushButton.clicked.connect(lambda: self.get_dir())
        self.pushButton_2.clicked.connect(lambda: self.get_files())
        self.pushButton_3.clicked.connect(lambda: self.data_process())
        self.pushButton_4.clicked.connect(lambda: self.uniq_values())
        self.pushButton_5.clicked.connect(lambda: self.clean())


    def get_files(self):
        files, _ = QFileDialog.getOpenFileNames(self,
                                                '选择文件', './data', )
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

    def data_process(self):
        try:
            dist_dir = QFileDialog.getExistingDirectory(self,
                                                    '选择保存目录', './')
            for f in self.files:
                source_dir, file_name = os.path.split(f)
                curve_data = CurveData(f)
                curve_data.get_data()
                curve_data.all_curve_files(dist_dir, file_name)
                r = '%s..........done' % file_name
                if r: self.textBrowser_2.append(r)
        except Exception as e:
            print(e)

    def uniq_values(self):
        if len(self.files) == 0:
            rst = ['选择文件']
        else:
            rst = get_LB(os.path.dirname(self.files[0]))
        for r in rst:
            self.textBrowser_2.append(r)