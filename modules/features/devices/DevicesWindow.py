
from PyQt5.QtWidgets import *

from modules.components.PaginationBar import PaginationBar
from modules.generated.devices_ui import Ui_Form as UI_DevicesWindow

class DevicesWindow(QWidget, UI_DevicesWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)

    self.paginationBar = PaginationBar()

    self.mainLayout.addWidget(self.paginationBar, 3, 0, 1, 1)
