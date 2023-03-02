
from PyQt5.QtWidgets import *
from operator import itemgetter
import math
from PyQt5.QtCore import pyqtSignal

from modules.generated.pagination_bar_ui import Ui_Form as UI_PaginationBar

class PaginationBar(QWidget, UI_PaginationBar):
  changed = pyqtSignal(object)
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)

    # Default texts
    self.setAddButtonText("Add New") \
      .setEditButtonText("Edit") \
      .setDeleteButtonText("Delete")
    

    self.comboBoxPerPage.addItem("All", "all")
    self.comboBoxPerPage.addItem("25", 25)
    self.comboBoxPerPage.addItem("50", 50)
    self.comboBoxPerPage.addItem("100", 100)
    self.comboBoxPerPage.addItem("200", 200)
    self.comboBoxPerPage.addItem("500", 500)
    self.comboBoxPerPage.addItem("1000", 1000)
    
    self.options = {
      "itemsCount": 1,
      "currentPage": 1,
      "itemsPerPage": "all"
    }

    def onPrevious():
      count = self.options["currentPage"]

      if(count > 1):
        count = count - 1
        self.options["currentPage"] = count
        self.emitChange()
  
    def onNext():
      count = self.options["currentPage"]
      totalPages = self.totalPages()

      if(count < totalPages):
        count = count + 1
        self.options["currentPage"] = count
        self.emitChange()

    def onFirst():
      count = self.options["currentPage"]

      if(count > 1):
        count = 1
        self.options["currentPage"] = count
        self.emitChange()

    def onLast():
      count = self.options["currentPage"]
      totalPages = self.totalPages()

      if(count < totalPages):
        count = 1
        self.options["currentPage"] = totalPages
        self.emitChange()
    
    def onChangePerPage(index):
      data = self.comboBoxPerPage.itemData(index)
      self.options["itemsPerPage"] = data
      self.options["currentPage"] = 1

      self.emitChange()

    def onChangeCurrentPage():
      # editingFinished, textEdited, textChanged
      data = self.inputCurrentPage.text()

      try:
        data = int(data)

        if(data >= 1 and data <= self.totalPages()):
          self.options["currentPage"] = data
          self.emitChange()

          return
      except:
        pass
      
      self.updateUI()

    self.buttonPrevious.clicked.connect(onPrevious)
    self.buttonNext.clicked.connect(onNext)
    self.buttonFirst.clicked.connect(onFirst)
    self.buttonLast.clicked.connect(onLast)
    self.comboBoxPerPage.currentIndexChanged.connect(onChangePerPage)
    self.inputCurrentPage.editingFinished.connect(onChangeCurrentPage)

    self.updateUI()
    


  def getSqlQuery(self):
    currentPage = self.currentPage() - 1
    itemsPerPage = self.itemsPerPage()

    if (itemsPerPage != "all"):
      limit = itemsPerPage
      offset = currentPage * itemsPerPage

      return f"LIMIT {limit} OFFSET {offset}"
    
    return ""

  def getSqlOptions(self):
    currentPage = self.currentPage() - 1
    itemsPerPage = self.itemsPerPage()

    if (itemsPerPage != "all"):
      limit = itemsPerPage
      offset = currentPage * itemsPerPage

      return {
        "limit": limit,
        "offset": offset
      }
    
    return {}

  def emitChange(self):
    self.changed.emit(self.options)
    self.updateUI()

  def setAddButtonText(self, text):
    self.buttonAdd.setText(text)
    return self

  def setEditButtonText(self, text):
    self.buttonEdit.setText(text)
    return self

  def setDeleteButtonText(self, text):
    self.buttonDelete.setText(text)
    return self

  def currentPage(self):
    return self.options["currentPage"]
  
  def itemsCount(self):
    return self.options["itemsCount"]
  
  def itemsPerPage(self):
    return self.options["itemsPerPage"]

  def totalPages(self):
    itemsCount, itemsPerPage = itemgetter("itemsCount", "itemsPerPage")(self.options)
    
    if (itemsPerPage == "all"):
      return 1
    else:
      return math.ceil(itemsCount / int(itemsPerPage))
  
  def onAdd(self, fn):
    self.buttonAdd.clicked.connect(fn)

  def onEdit(self, fn):
    self.buttonEdit.clicked.connect(fn)

  def onDelete(self, fn):
    self.buttonDelete.clicked.connect(fn)


  # def setCurrentPage(self, currentPage):
  #   self.options["currentPage"] = currentPage
  #   self.updateUI()

  def updateUI(self):
    self.inputCurrentPage.setText(str(self.currentPage()))
    self.labelTotalPages.setText(str(self.totalPages()))

  # # Event emitters

  # def onFirst(self, fn):
  #   self.setCurrentPage(1)
  #   self.buttonFirst.clicked.connect(fn)

  # def onPrevious(self, fn):
  #   currentPage = self.currentPage()

  #   if (currentPage != 1):
  #     self.setCurrentPage(currentPage - 1)
  #     self.buttonPrevious.clicked.connect(fn)

  # def onNext(self, fn):
  #   def onNextHandler():
  #     currentPage = self.currentPage
  #     print("Current page: ", currentPage)

  #     # if (currentPage < self.totalPages()):
  #     self.setCurrentPage(currentPage + 1)
  #     fn()

  #   self.buttonNext.clicked.connect(onNextHandler)

  # def onLast(self, fn):
  #   self.buttonLast.clicked.connect(fn)


  # def onChangeCurrentPage(self, fn):
  #   # editingFinished, textEdited, textChanged
  #   self.inputCurrentPage.editingFinished.connect(
  #     lambda:
  #       (data := self.inputCurrentPage.text(),
  #         fn(data))
  #   )

  # def onChangePerPage(self, fn):
  #   # Get data at that index
  #   self.comboBoxPerPage.currentIndexChanged.connect(
  #     lambda index: 
  #       (data := self.comboBoxPerPage.itemData(index),
  #         fn(data))
  #   )
