#! /usr/bin/env python3

import sys

from uiModule import *
from mainGUI import ActivityGUI

styleData = """
QWidget
{
    color: white;
    background-color: #323232;
}
QHeaderView::section {
    background-color: #323232;
    padding: 4px;
    border: 0px;
    font-size: 10pt;
    color: #b1b1b1
}
QTableWidget {
    gridline-color: #323232;
    border: 1px solid #323232;
    font-size: 12pt;
}
QTableWidget QTableCornerButton::section {
    background-color: #323232;
    border: 1px solid #323232;
}
QTableView
{
    color: #b1b1b1
}
QTableView::item:selected
{
    color: #f5f5ef;
    background: #323232;
}
QProgressBar
{
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center;
    font-size: 14pt;
    font-weight: 400;
    padding : 1px
}
QProgressBar::chunk
{
    background-color: #008000;
    width: 2.15px;
    margin: 0.5px;
}
QPushButton:pressed
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);
}
QPushButton
{
    color: #b1b1b1;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);
    border-width: 1px;
    border-color: #1e1e1e;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 14px;
    padding-left: 5px;
    padding-right: 5px;
}"""

# setup ui2
app = QtWidgets.QApplication(sys.argv)
DailySchedule = QtWidgets.QDialog()
DailySchedule.setStyleSheet(styleData)

# initialize tableWidget
gui = ActivityGUI()
gui.setup(DailySchedule)
gui.create_some_activities()
gui.arrange_activities()

# show the window
DailySchedule.show()
sys.exit(app.exec_())
