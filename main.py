import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
import sqlite3


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffe.sqlite")
        self.initUI()
        # self.dialog = Dialog(self)

    def initUI(self):
        # self.pushButton.clicked.connect(self.show_dialog)
        self.update_table()

    def update_table(self):
        cur = self.con.cursor()
        result = cur.execute('''
        SELECT id, name, calibre, is_ground, price, size FROM coffe
        ''').fetchall()
        if result:
            self.tableWidget.setColumnCount(len(result[0]))
            self.tableWidget.setRowCount(len(result))
            headers = [description[0] for description in cur.description]
            self.tableWidget.setHorizontalHeaderLabels(headers)

            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    # def show_dialog(self):
    #     self.dialog.show()
    #
    # def add_item(self, *args):
    #     cur = self.con.cursor()
    #     cur.execute('''INSERT INTO coffe(id, title, year, genre, duration)
    #     VALUES((SELECT id FROM films ORDER BY id DESC LIMIT 1) + 1, ?, ?, ?, ?)''', (*args,))
    #     self.con.commit()
    #     self.update_table()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainForm()
    ex.show()
    sys.exit(app.exec())
