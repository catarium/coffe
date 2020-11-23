import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication


class Dialog(QDialog):
    def __init__(self, parent):
        super(Dialog, self).__init__()
        uic.loadUi('dialog.ui', self)
        self.parent = parent
        # self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.btn.clicked.connect(self.ret_data)
        cur = self.parent.con.cursor()
        for i in ['слабая', 'средняя', 'средне-темная', 'темная', 'наиболее темная']:
            self.calibre.addItem(i)

    def ret_data(self):
        data = [self.getname.text(), self.calibre.currentText(), self.description.text(),
                self.price.text(), self.size.text(),
                'молотый' if self.checkBox.isChecked() else 'не молотый']
        if len(set([bool(i) for i in data[:-1]])) == 1:
            self.parent.add_item(*data)
            self.label_6.setText('')
            self.close()
        else:
            self.label_6.setText('Данные введены неверно')
        print(data)
