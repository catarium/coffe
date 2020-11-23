import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from dialog import Dialog
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
import sqlite3
from UI.main_form import Ui_MainWindow


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("data/coffe.sqlite")
        self.initUI()
        self.dialog = Dialog(self)

    def initUI(self):
        self.pushButton.clicked.connect(self.show_dialog)
        self.update_table()

    def update_table(self):
        cur = self.con.cursor()
        result = cur.execute('''
        SELECT id, name, calibre, description, price, size, is_ground FROM coffe
        ''').fetchall()
        if result:
            self.tableWidget.setColumnCount(len(result[0]))
            self.tableWidget.setRowCount(len(result))
            headers = [description[0] for description in cur.description]
            self.tableWidget.setHorizontalHeaderLabels(headers)

            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def show_dialog(self):
        self.dialog.show()

    def add_item(self, *args):
        cur = self.con.cursor()
        cur.execute('''INSERT INTO coffe(name, calibre, description, price, size, is_ground)
        VALUES(?, ?, ?, ?, ?, ?)''', (*args,))
        self.con.commit()
        self.update_table()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainForm()
    ex.show()
    sys.exit(app.exec())
