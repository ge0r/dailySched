# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DailySchedule.ui'
#
# Created: Mon Jul 11 18:35:52 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_q_dialog(object):
    def setupUi(self, q_dialog):
        q_dialog.setObjectName("q_dialog")
        q_dialog.resize(700, 500)
        self.gridLayout = QtWidgets.QGridLayout(q_dialog)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(q_dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(q_dialog)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.deleteButton = QtWidgets.QPushButton(q_dialog)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.resetButton = QtWidgets.QPushButton(q_dialog)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout.addWidget(self.resetButton)
        self.moreButton = QtWidgets.QPushButton(q_dialog)
        self.moreButton.setObjectName("moreButton")
        self.horizontalLayout.addWidget(self.moreButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(q_dialog)
        QtCore.QMetaObject.connectSlotsByName(q_dialog)

    def retranslateUi(self, q_dialog):
        _translate = QtCore.QCoreApplication.translate
        q_dialog.setWindowTitle(_translate("q_dialog", "Form"))
        self.addButton.setText(_translate("q_dialog", "Add new"))
        self.deleteButton.setText(_translate("q_dialog", "Delete selected"))
        self.resetButton.setText(_translate("q_dialog", "Reset time"))
        self.moreButton.setText(_translate("q_dialog", "About"))

