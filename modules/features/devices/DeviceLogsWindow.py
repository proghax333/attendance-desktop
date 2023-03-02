
from PyQt5.QtWidgets import *

import sqlite3

from modules.components.PaginationBar import PaginationBar
from modules.generated.device_logs_ui import Ui_Form as UI_DeviceLogsWindow
from modules.utils.Task import AsyncTask
from modules.models.SimpleTableModel import SimpleTableModel

from pypika import Query, Table, Field, Parameter, functions as fn
from operator import itemgetter
from modules.models import query, contacts

class DeviceLogsWindow(QWidget, UI_DeviceLogsWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)

    self.paginationBar = PaginationBar() \
      .setAddButtonText("Assign Employee Manual Entries") \
      .setEditButtonText("Edit") \
      .setDeleteButtonText("Delete all selected records")
    
    def onPageChange(options):
      AsyncTask.runTask(
        self.load_data,
        self.on_load_data
      )

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
    connection = sqlite3.connect("contacts.db")

    queryCount = Query \
      .from_(contacts) \
      .select(fn.AggregateFunction("count", "id").as_("totalRows")) \
      .get_sql()
    # print("count query: ", queryCount)

    rowsCount = itemgetter("rows") \
      (query(connection, queryCount))

    queryContacts = Query \
      .from_(contacts) \
      .select("id", "name", "job", "email") \
    
    # Pagination
    paginationOptions = self.paginationBar.getSqlOptions()
    if ("limit" in paginationOptions):
      queryContacts = queryContacts \
        .limit(paginationOptions["limit"]) \
        .offset(paginationOptions["offset"])

    queryContacts = queryContacts.get_sql()
    # print("contact query: ", queryContacts)
    
    rowsContacts, _ = itemgetter("rows", "count") \
      (query(connection, queryContacts))

    data, totalRecords = rowsContacts, rowsCount[0][0]

    return data, totalRecords
  
  def on_load_data(self, values):
    data, total = values

    self.model = SimpleTableModel(data)
    self.table.setModel(self.model)
    
    self.paginationBar.options["itemsCount"] = total

    # self.paginationBar.onChangeCurrentPage(lambda value: print("Current page changed: ", value))

    # # self.paginationBar.onFirst(lambda: print("First button was clicked"))
    # self.paginationBar.onChangePerPage(lambda value: print("Per page changed: ", value))

