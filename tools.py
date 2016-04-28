from PyQt5 import QtCore, QtGui, QtWidgets
import time


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


class MyProgressBar(QtWidgets.QProgressBar):

    def change_color(self, color):
        template_css = """QProgressBar::chunk { background: %s; }"""
        css = template_css % color
        self.setStyleSheet(css)
