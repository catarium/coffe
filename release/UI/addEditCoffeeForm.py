# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 371, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.description = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.description.setObjectName("description")
        self.gridLayout.addWidget(self.description, 8, 2, 1, 1)
        self.calibre = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.calibre.setObjectName("calibre")
        self.gridLayout.addWidget(self.calibre, 3, 2, 1, 1)
        self.price = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.price.setObjectName("price")
        self.gridLayout.addWidget(self.price, 9, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 12, 0, 1, 3)
        self.durationlabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.durationlabel.setObjectName("durationlabel")
        self.gridLayout.addWidget(self.durationlabel, 9, 0, 1, 1)
        self.namelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.namelabel.setObjectName("namelabel")
        self.gridLayout.addWidget(self.namelabel, 0, 0, 1, 1)
        self.genrelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.genrelabel.setObjectName("genrelabel")
        self.gridLayout.addWidget(self.genrelabel, 8, 0, 1, 1)
        self.yearlabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.yearlabel.setObjectName("yearlabel")
        self.gridLayout.addWidget(self.yearlabel, 3, 0, 1, 1)
        self.getname = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.getname.setObjectName("getname")
        self.gridLayout.addWidget(self.getname, 0, 2, 1, 1)
        self.size = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.size.setObjectName("size")
        self.gridLayout.addWidget(self.size, 10, 2, 1, 1)
        self.durationlabel_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.durationlabel_2.setObjectName("durationlabel_2")
        self.gridLayout.addWidget(self.durationlabel_2, 10, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 270, 47, 13))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(6, 263, 131, 20))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.btn = QtWidgets.QPushButton(Dialog)
        self.btn.setGeometry(QtCore.QRect(280, 250, 101, 41))
        self.btn.setObjectName("btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox.setText(_translate("Dialog", "Молотый"))
        self.durationlabel.setText(_translate("Dialog", "Цена"))
        self.namelabel.setText(_translate("Dialog", "Название"))
        self.genrelabel.setText(_translate("Dialog", "Описание"))
        self.yearlabel.setText(_translate("Dialog", "Степень обжарки"))
        self.durationlabel_2.setText(_translate("Dialog", "Размер"))
        self.btn.setText(_translate("Dialog", "Добавить"))
