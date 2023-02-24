
from PyQt5.QtWidgets import *

from modules.components.PaginationBar import PaginationBar
from modules.generated.members_ui import Ui_Form as UI_MembersWindow

class MembersWindow(QWidget, UI_MembersWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)

    self.paginationBar = PaginationBar()

    self.mainLayout.addWidget(self.paginationBar)
