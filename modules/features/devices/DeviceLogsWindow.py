
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
    
    def onPageChange(options):
      print("query: ", self.paginationBar.getSqlQuery())

      AsyncTask.runTask(
        self.load_data,
        self.on_load_data
      )

      pass

    self.paginationBar.changed.connect(onPageChange)

    self.gridLayout.addWidget(self.paginationBar, 3, 0, 1, 1)

    AsyncTask.runTask(
      self.load_data,
      self.on_load_data
    )
  #   self.inputEmployeeCode.changed.connect(self.handleEmployeeCodeChange)

  # def handleEmployeeCodeChange(self):
  #   print(self.inputEmployeeCode)
    
  def load_data(self):
    con = sqlite3.connect("contacts.db")

    queryCount = con.cursor()
    sqlCount = "select count(id) from contacts";
    queryCount.execute(sqlCount)
    totalRecords, = queryCount.fetchall()[0]

    print("total records: ", totalRecords)

    query = con.cursor()
    sql = f"select * from contacts {self.paginationBar.getSqlQuery()}"
    print("Data query: ", sql)
    query.execute(sql)

    data = query.fetchall()
    
    con.close()

    return data, totalRecords
  
  def on_load_data(self, values):
    data, total = values

    self.model = SimpleTableModel(data)
    self.table.setModel(self.model)
    
    self.paginationBar.options["itemsCount"] = total

    # self.paginationBar.onChangeCurrentPage(lambda value: print("Current page changed: ", value))

    # # self.paginationBar.onFirst(lambda: print("First button was clicked"))
    # self.paginationBar.onChangePerPage(lambda value: print("Per page changed: ", value))

