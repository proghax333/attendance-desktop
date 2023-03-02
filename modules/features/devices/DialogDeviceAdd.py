
from PyQt5.QtWidgets import *

from modules.generated.device_add_ui import Ui_Dialog as UI_DialogDeviceAdd

class DialogDeviceAdd(QDialog, UI_DialogDeviceAdd):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)

    self.buttonClose.clicked.connect(self.close)
