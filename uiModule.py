#! /usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DailySchedule.ui'
#
# Created: Tue Apr 19 00:33:27 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class gTableWidget(object):
    def setupUi(self, q_dialog):
        q_dialog.setObjectName("DailySchedule")
        q_dialog.resize(460, 300)
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
        self.pushButton = QtWidgets.QPushButton(q_dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.retranslateUi(q_dialog)
        QtCore.QMetaObject.connectSlotsByName(q_dialog)

    def retranslateUi(self, q_dialog):
        _translate = QtCore.QCoreApplication.translate
        q_dialog.setWindowTitle(_translate("DailySchedule", "Form"))
        self.pushButton.setText(_translate("DailySchedule", "test"))

