# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DailySchedule.ui'
#
# Created: Fri Jul  8 16:15:27 2016
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
        self.resetButton = QtWidgets.QPushButton(q_dialog)
        self.resetButton.setObjectName("resetButton")
        self.gridLayout.addWidget(self.resetButton, 2, 0, 1, 1)
        self.testButton = QtWidgets.QPushButton(q_dialog)
        self.testButton.setObjectName("testButton")
        self.gridLayout.addWidget(self.testButton, 3, 0, 1, 1)

        self.retranslateUi(q_dialog)
        QtCore.QMetaObject.connectSlotsByName(q_dialog)

    def retranslateUi(self, q_dialog):
        _translate = QtCore.QCoreApplication.translate
        q_dialog.setWindowTitle(_translate("q_dialog", "Form"))
        self.resetButton.setText(_translate("q_dialog", "Reset"))
        self.testButton.setText(_translate("q_dialog", "Test"))

