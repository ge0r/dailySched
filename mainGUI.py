import time
from PyQt5 import QtCore
from PyQt5.QtCore import QObject

from PyQt5.QtWidgets import QTableWidgetItem, QProgressBar, QHeaderView

from activity import Activity
from uiModule import gTableWidget


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

    def setup(self, daily_schedule):
        self.setupUi(daily_schedule)

        # initialize tableWidget
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Activity", "Duration"])

        # connect slots to signals
        self.tableWidget.cellClicked.connect(self.handle_cell_click)
        self.tableWidget.cellDoubleClicked.connect(self.handle_cell_double_click)
        self.thread.time_signal.connect(self.update_progressbar)
        self.stop_thread_signal.connect(self.thread.stop)
        # self.pushButton.clicked.connect(self.handle_click)
        # self.tableWidget.cellChanged.connect(self.handle_change)

    def arrange_activities(self):
        count = 0

        self.activities.sort(key=lambda x: x.duration)

        # fill tableWidget
        for activity in self.activities:
            item = QTableWidgetItem()
            print(activity.name)
            item.setText(activity.name)

            # make activity text not editable
            item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)

            self.tableWidget.insertRow(self.tableWidget.rowCount())
            self.tableWidget.setItem(count, 0, item)

            # add progress bar note, remove self
            progressbar = QProgressBar()
            progressbar.setMaximum(activity.duration)
            progressbar.setMinimum(0)
            progressbar.setValue(progressbar.maximum())
            progressbar.setTextVisible(True)
            progressbar.setFormat(str(activity.return_minute_format()))
            self.tableWidget.setCellWidget(count, 1, progressbar)

            count += 1

        # resize headers to fit
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def create_some_activities(self):
        self.activities = [Activity("piano", 15, 3, 3), Activity("coding", 90, 4, 5), Activity("study", 10, 1, 2)]

    # slots
    def update_progressbar(self):
        row = self.active_row

        # update activity time
        self.activities[row].update_time()
        time_left = self.activities[row].time_left

        self.tableWidget.cellWidget(row, 1).setValue(time_left)
        self.tableWidget.cellWidget(row, 1).setFormat(self.activities[row].return_minute_format())

    def handle_cell_click(self, row, col):
        self.tableWidget.selectRow(row)

    def handle_cell_double_click(self, row, col):

        # if it's the first time, the active_row is the current row
        if self.active_row is None:
            self.active_row = row

        # store if the activity was running or not before the stop signal is sent
        running = self.activities[row].is_running

        # If an activity is running, stop it.
        if running is True:
            self.stop_thread_signal.emit()
            self.activities[self.active_row].stop_time_update()
            print("stopping activity")

        # if the double clicked row is not the active row, or if it is, if the activity was not running, start it.
        if row != self.active_row or not running:

            # wait for thread to finish before starting
            self.thread.wait()
            self.thread.start()

            self.active_row = row


class ThreadClass(QtCore.QThread):
    time_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)
        self.loop = True

    def run(self):
        self.loop = True

        # Execution ends when you return from run(), just as an application does when it leaves main()
        while self.loop is True:
            self.time_signal.emit()

            # time step is twice the frequency of the activity timer to avoid sampling inaccuracies (Nyquist frequency)
            time.sleep(0.5)

    def stop(self):
        # Don't use terminate() to terminate threads.
        self.loop = False
