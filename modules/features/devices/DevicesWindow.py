
from PyQt5.QtWidgets import *

from modules.components.PaginationBar import PaginationBar
from modules.generated.devices_ui import Ui_Form as UI_DevicesWindow

from modules.features.devices.DialogDeviceAdd import DialogDeviceAdd

from pypika import Query, Table, Tables, Field, Parameter, functions as fn

class DevicesWindow(QWidget, UI_DevicesWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)

    self.paginationBar = PaginationBar()

    self.mainLayout.addWidget(self.paginationBar, 3, 0, 1, 1)

    self.paginationBar.onAdd(self.onAdd)
    self.paginationBar.onEdit(self.onEdit)
    self.paginationBar.onDelete(self.onDelete)
  
  def onAdd(self):
    self.dialogDeviceAdd = DialogDeviceAdd(parent=self)
    self.dialogDeviceAdd.show()
    pass

  def onEdit(self):
    pass

  def onDelete(self):
    pass