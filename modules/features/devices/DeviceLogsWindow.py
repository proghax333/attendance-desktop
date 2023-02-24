
from PyQt5.QtWidgets import *

import sqlite3

from modules.components.PaginationBar import PaginationBar
from modules.generated.device_logs_ui import Ui_Form as UI_DeviceLogsWindow
from modules.utils.Task import AsyncTask
from modules.models.SimpleTableModel import SimpleTableModel

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
