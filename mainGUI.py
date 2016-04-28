from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView

import pyglet

from activity import Activity
from uiModule import gTableWidget
from tools import ThreadClass, MyProgressBar


class ActivityGUI(gTableWidget, QObject):

    # pyqtSignal as class variable
    stop_thread_signal = QtCore.pyqtSignal()

    def __init__(self):
        # don't forget, needed for QObject signal
        super(ActivityGUI, self).__init__()

        self.ui = gTableWidget()
        self.activities = None
        self.thread = None
        self.active_row = None
        self.thread = ThreadClass()

        # decode audio file in memory, since sound is going to be played more than once
        self.song = pyglet.media.load("activity_completed.wav", streaming=False)

        self.play_alert = True

    def setup(self, daily_schedule):
        self.setupUi(daily_schedule)

        # initialize tableWidget
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Activity", "Time Left"])

        # connect slots to signals
        self.tableWidget.cellClicked.connect(self.handle_cell_click)
        self.tableWidget.cellDoubleClicked.connect(self.handle_cell_double_click)
        self.thread.time_signal.connect(self.update_progressbar)
        self.stop_thread_signal.connect(self.thread.stop)
        # self.pushButton.clicked.connect(self.handle_click)

    def arrange_activities(self):
        count = 0

        self.activities.sort(key=lambda x: x.duration)

        # fill tableWidget
        for activity in self.activities:
            item = QTableWidgetItem()
            print(activity.name+" "+str(activity.duration))
            item.setText(activity.name)

            # make activity text not editable
            item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)

            self.tableWidget.insertRow(self.tableWidget.rowCount())
            self.tableWidget.setItem(count, 0, item)

            # add progress bar note, remove self
            progressbar = MyProgressBar()
            progressbar.setMaximum(activity.duration)
            progressbar.setMinimum(0)
            progressbar.setValue(progressbar.maximum())

            progressbar.setTextVisible(True)
            progressbar.setFormat(str(activity.return_hour_minute_format()))
            progressbar.setToolTip("duration: " + activity.return_hour_minute_format())

            self.tableWidget.setRowHeight(count, 65)

            self.tableWidget.setCellWidget(count, 1, progressbar)

            # # arrange row height according to initial duration
            # if activity.duration <= 3600:
            #     print("60")
            #     self.tableWidget.setRowHeight(count, 30)
            # elif activity.duration <= 7200:
            #     print("120")
            #     self.tableWidget.setRowHeight(count, 40)
            # elif activity.duration <= 14400:
            #     self.tableWidget.setRowHeight(count, 50)
            # else:
            #     self.tableWidget.setRowHeight(count, 60)

            count += 1

        # resize headers to fit
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def start_activity(self, row):
        # wait for thread to finish before starting
        self.thread.wait()
        self.thread.start()

        self.tableWidget.cellWidget(row, 1).change_color("#b34700")
        self.active_row = row
        print("starting "+str(row))

    def stop_activity(self):
        self.stop_thread_signal.emit()
        self.activities[self.active_row].stop_time_update()
        self.tableWidget.cellWidget(self.active_row, 1).change_color("#008000")
        print("stopping activity")

    def end_activity(self):
        # do the required actions to stop the progressbar activity
        self.stop_thread_signal.emit()
        self.tableWidget.cellWidget(self.active_row, 1).setFormat("Completed")

        # if the user has selected it, play the alert
        if self.play_alert is True:
            self.song.play()

        print(self.activities[self.active_row].name+" completed")

    def create_some_activities(self):
        self.activities = [Activity("test", 0.05, 3, 3), Activity("mail", 0.1, 3, 3), Activity("cleaning", 10, 3, 3),
                           Activity("write music", 600, 3, 3), Activity("coding", 120, 4, 5),
                           Activity("study", 180, 1, 2)]

    # slots
    def update_progressbar(self):

        row = self.active_row

        # if the activity has not ended keep updating the progressbar
        if self.activities[row].ended is False:
            # update activity time
            self.activities[row].update_time()
            time_left = self.activities[row].time_left

            self.tableWidget.cellWidget(row, 1).setValue(time_left)
            self.tableWidget.cellWidget(row, 1).setFormat(self.activities[row].return_hour_minute_format())

        else:
            # do required actions to end the activity
            self.end_activity()

    def handle_cell_click(self, row, col):
        self.tableWidget.selectRow(row)

    def handle_cell_double_click(self, row, col):

        # if it's the first time, the active_row is the current row
        if self.active_row is None:
            self.active_row = row

        # store if the activity was running or not before the stop signal is sent
        running = self.activities[self.active_row].is_running

        # If an activity is running, stop it.
        if running is True:
            self.stop_activity()

        # if the double clicked row is not the active row, or if the activity was not running, start it.
        if row != self.active_row or not running:
            # if the activity has not already ended start it
            if not self.activities[row].ended:
                self.start_activity(row)
