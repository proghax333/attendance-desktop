
from PyQt5.QtWidgets import *

from modules.generated.report_ui import Ui_Dialog as UI_GenerateReportDialog

class GenerateReportDialog(QDialog, UI_GenerateReportDialog):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)
