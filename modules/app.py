
from typing import Any
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QThread, QObject, QRunnable, QThreadPool

import sys
import sqlite3
import time
import typing

from modules.generated.pagination_bar_ui import Ui_Form as UI_PaginationBar

from modules.generated.main_window_ui import Ui_MainWindow
from modules.generated.device_logs_ui import Ui_Form as UI_DeviceLogsWindow
from modules.generated.devices_ui import Ui_Form as UI_DevicesWindow
from modules.generated.manage_base_ui import Ui_Dialog as UI_ManageBase

class Worker(QObject):
    finished = pyqtSignal(object)
    # progress = pyqtSignal(int)

    def __init__(self, **kwargs) -> None:
      super().__init__(**kwargs)
      self.task = lambda: None

    def set_task(self, task):
      self.task = task
    
    def get_task(self):
      return self.task

    def run(self):
      result = self.task()
      self.finished.emit(result)

class SimpleTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(SimpleTableModel, self).__init__()
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

class DevicesWindow(QWidget, UI_DevicesWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)

    self.paginationBar = PaginationBar()

    self.mainLayout.addWidget(self.paginationBar, 3, 0, 1, 1)

class AsyncTask(QObject):
  finished = pyqtSignal(object)

  def __init__(self, task, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.task = task

    self.thread = QThread()
    
    self.worker = Worker()
    self.worker.set_task(self.task)
    self.worker.moveToThread(self.thread)

    self.thread.started.connect(self.worker.run)
    self.worker.finished.connect(self.finished)
    self.worker.finished.connect(self.thread.quit)
    self.worker.finished.connect(self.worker.deleteLater)
    self.thread.finished.connect(self.thread.deleteLater)
  
  def start(self):
    return self.thread.start()
  
class DeviceLogsWindow(QWidget, UI_DeviceLogsWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)

    self.paginationBar = PaginationBar() \
      .setAddButtonText("Assign Employee Manual Entries") \
      .setEditButtonText("Edit") \
      .setDeleteButtonText("Delete all selected records")

    self.gridLayout.addWidget(self.paginationBar, 3, 0, 1, 1)

    self.dataLoadTask = AsyncTask(self.load_data)
    self.dataLoadTask.finished.connect(self.on_load_data)
    self.dataLoadTask.start()

  #   self.inputEmployeeCode.changed.connect(self.handleEmployeeCodeChange)

  # def handleEmployeeCodeChange(self):
  #   print(self.inputEmployeeCode)
    
  def load_data(self):
    con = sqlite3.connect("contacts.db")

    query = con.cursor()
    query.execute("select * from contacts;")

    data = query.fetchall()
    
    con.close()

    return data
  
  def on_load_data(self, data):
    self.model = SimpleTableModel(data)
    self.table.setModel(self.model)

class PaginationBar(QWidget, UI_PaginationBar):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)

    # Default texts
    self.setAddButtonText("Add New") \
      .setEditButtonText("Edit") \
      .setEditButtonText("Delete")

  def setAddButtonText(self, text):
    self.buttonAdd.setText(text)
    return self

  def setEditButtonText(self, text):
    self.buttonEdit.setText(text)
    return self

  def setDeleteButtonText(self, text):
    self.buttonDelete.setText(text)
    return self

class DialogManageBase(QDialog, UI_ManageBase):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)

    self.title = "Title"
    self.paginationBar = PaginationBar()
    self.mainLayout.addWidget(self.paginationBar)

    self.refreshUi()
  
  def getManageTitle(self):
    return self.title
  
  def setManageTitle(self, title):
    self.title = title
    self.refreshUi()
    return self
  
  def refreshUi(self):
    self.titleLabel.setText(self.title)
    self.setWindowTitle(self.title)

    return self


class MainApplicationWindow(QMainWindow, Ui_MainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)

    self.actionDeviceLogs.triggered.connect(
      lambda: self.showWindow(
        lambda parent: DeviceLogsWindow(parent=parent)
      )
    )

    self.actionDeviceLogs.trigger()
    
    self.actionDevices.triggered.connect(
      lambda: self.showWindow(
        lambda parent: DevicesWindow(parent=parent)
      )
    )

    self.actionDepartment.triggered.connect(
      lambda: self.showDialog(
        lambda: DialogManageBase(parent=self) \
          .setManageTitle("Department List")
      )
    )

    self.actionDepartments.triggered.connect(
      lambda: self.showDialog(
        lambda: DialogManageBase(parent=self) \
          .setManageTitle("Department List")
      )
    )

    self.actionMembers.triggered.connect(
      lambda: self.showDialog(
        lambda: DialogManageBase(parent=self) \
          .setManageTitle("Member List")
      )
    )

    self.actionCategories.triggered.connect(
      lambda: self.showDialog(
        lambda: DialogManageBase(parent=self) \
          .setManageTitle("Category List")
      )
    )

    self.actionRoles.triggered.connect(
      lambda: self.showDialog(
        lambda: DialogManageBase(parent=self) \
          .setManageTitle("Role List")
      )
    )

  def showDialog(self, factory):
    dialog = factory()
    dialog.show()

    return self

  def showWindow(self, factory):
    win = QMdiSubWindow(parent=self.mdiArea)
    mdiWindowWidget = factory(win)
    win.setWidget(mdiWindowWidget)
    win.show()
    win.setWindowState(Qt.WindowState.WindowMaximized)
    
    return self

import signal

def start():
  # Setup Ctrl - C interceptors
  signal.signal(signal.SIGINT, signal.SIG_DFL)

  # Create an instance of QT application
  app = QApplication(sys.argv)

  window = MainApplicationWindow(parent=None)
  window.show()
  window.setWindowState(Qt.WindowState.WindowMaximized)

  # window.load_data()

  sys.exit(app.exec())
