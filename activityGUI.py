import os.path
from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView

import pyglet
import json
import jsonpickle

from activity import Activity
from pyQtUi import Ui_q_dialog
from tools import ThreadClass, MyProgressBar


class ActivityGUI(Ui_q_dialog, QObject):

    # pyqtSignal as class variable
    stop_thread_signal = QtCore.pyqtSignal()

    def __init__(self):
        # don't forget, needed for QObject signal
        super(ActivityGUI, self).__init__()

        self.ui = Ui_q_dialog()
        self.activities = None

        # active_row is the row in the tableWidget with a progress bar currently running
        self.active_row = None
        self.thread = ThreadClass()

        # decode audio file in memory, since sound is going to be played more than once
        self.song = pyglet.media.load("activity_completed.wav", streaming=False)

        # if True, plays the self.song alert when an activity is over
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
        self.resetButton.clicked.connect(self.handle_reset_click)

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
            progressbar.setValue(activity.time_left)

            progressbar.setTextVisible(True)

            # if the activity has already been completed write completed message
            if activity.ended is True:
                progressbar.setFormat("Completed")
            else:
                progressbar.setFormat(str(activity.return_hour_minute_format()))
                progressbar.setToolTip("duration: " + activity.return_hour_minute_format())

            self.tableWidget.setRowHeight(count, 65)

            self.tableWidget.setCellWidget(count, 1, progressbar)

            self.thicken_activity_bar(activity, count)

            count += 1

        # resize headers to fit
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def thicken_activity_bar(self, activity, count):
        # arrange row height according to initial duration
        if activity.duration <= 3600:
            print("60")
            self.tableWidget.setRowHeight(count, 65)
        elif activity.duration <= 7200:
            print("120")
            self.tableWidget.setRowHeight(count, 80)
        elif activity.duration <= 14400:
            self.tableWidget.setRowHeight(count, 95)
        else:
            self.tableWidget.setRowHeight(count, 110)

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

    def create_activities(self):
        if os.path.isfile("data.json") is False:
            # if no json file is found, create new activities
            self.activities = [Activity("music", 30, 3, 3), Activity("mail", 0.3, 3, 3), Activity("a", 0.1, 3, 3),
                               Activity("b", 60, 3, 3), Activity("coding", 60, 4, 5), Activity("other", 60, 4, 5),
                               Activity("study", 180, 1, 2), Activity("food1", 20, 4, 5), Activity("food2", 30, 4, 5),
                               Activity("duolingo", 25, 3, 3), Activity("sailing", 20, 3, 3)]

        else:
            # else load the data from the json file
            with open('data.json', encoding='utf-8') as data_file:
                pickled = json.loads(data_file.read())
                self.activities = jsonpickle.loads(pickled)

            # find running activity, if there is one
            for activity in self.activities:
                activity.stop_time_update()



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

            # store current activities state to JSON file
            self.obj_to_json()

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

    def handle_reset_click(self):
        print("reset button clicked")
        row = 0
        # for activity in self.activities:
        #     # reset each activity
        #     activity.reset()
        #
        #     # repaint progressbar
        #     self.tableWidget.cellWidget(row, 1).setValue(activity.time_left)
        #     self.tableWidget.cellWidget(row, 1).setFormat(self.activities[row].return_hour_minute_format())
        #
        #     if not activity.is_running:
        #         self.tableWidget.cellWidget(row, 1).change_color("#008000")
        #     row += 1

    def obj_to_json(self):
        pickled = jsonpickle.dumps(self.activities)

        # write pickled activities to json
        with open('data.json', 'w') as fp:
            # json.dump(activity, fp, default=jdefault)
            json.dump(pickled, fp)


def jdefault(o):
    return o.__dict__

