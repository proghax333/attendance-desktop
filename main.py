
from typing import Any
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QThread, QObject, QRunnable, QThreadPool

import sys
import sqlite3

from generated.main_window_ui import Ui_MainWindow
from generated.device_logs_ui import Ui_Form as UI_DeviceLogsWindow

class Runner(QObject):
  finished = pyqtSignal(object)

  def __init__(self, fn, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    self.fn = fn

  def run(self, *args, **kwargs):
    result = self.fn(*args, **kwargs)
    self.finished.emit(result)


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

  
class DeviceLogsWindow(QWidget, UI_DeviceLogsWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)

    self.load_data()

    # tableLoader = Runner(self.load_data)
    # self.thread = QThread()

    # self.thread.finished.connect(lambda: print("Done!!"))
    # self.thread.started.connect(tableLoader.run)

    # tableLoader.moveToThread(self.thread)
    # self.thread.start()

    # Load data from db into the table
    # tableLoader = Runner(self.load_data)
    # pool = QThreadPool.globalInstance()
    # pool.start(tableLoader)

    
  def load_data(self):
    con = sqlite3.connect("contacts.db")

    query = con.cursor()
    query.execute("select * from contacts;")

    data = query.fetchall()

    self.on_load_data(data)

    con.close()
    return data
  
  def on_load_data(self, data):
    self.model = TableModel(data)
    self.table.setModel(self.model)

class MainApplicationWindow(QMainWindow, Ui_MainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)

    self.actionDeviceLogs.triggered.connect(self.deviceLogsShow)

  def deviceLogsShow(self):
    win = QMdiSubWindow(parent=self.mdiArea)
    mditest = DeviceLogsWindow(parent=win)
    win.setWidget(mditest)
    win.show()
    win.setWindowState(Qt.WindowState.WindowMaximized)

    # mditest.show()
    # self.mdiArea.addSubWindow(win)
    
    return 0


if __name__ == "__main__":
  app = QApplication(sys.argv)

  window = MainApplicationWindow(parent=None)
  window.show()
  window.setWindowState(Qt.WindowState.WindowMaximized)

  # window.load_data()

  sys.exit(app.exec())
