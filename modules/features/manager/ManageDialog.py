
from PyQt5.QtWidgets import *

from modules.generated.manage_base_ui import Ui_Dialog as UI_ManageBase
from modules.components.PaginationBar import PaginationBar

class ManageDialog(QDialog, UI_ManageBase):
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
