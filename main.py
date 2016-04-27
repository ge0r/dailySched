#! /usr/bin/env python3

import sys

from uiModule import *
from mainGUI import ActivityGUI

# setup ui2
app = QtWidgets.QApplication(sys.argv)
DailySchedule = QtWidgets.QDialog()


# initialize tableWidget
gui = ActivityGUI()
gui.setup(DailySchedule)
gui.create_some_activities()
gui.arrange_activities()


# show the window
DailySchedule.show()
sys.exit(app.exec_())
