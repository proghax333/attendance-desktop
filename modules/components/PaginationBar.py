
from PyQt5.QtWidgets import *

from modules.generated.pagination_bar_ui import Ui_Form as UI_PaginationBar

class PaginationBar(QWidget, UI_PaginationBar):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)

    # Default texts
    self.setAddButtonText("Add New") \
      .setEditButtonText("Edit") \
      .setEditButtonText("Delete")

  def setAddButtonText(self, text):
    self.buttonAdd.setText(text)
    return self

  def setEditButtonText(self, text):
    self.buttonEdit.setText(text)
    return self

  def setDeleteButtonText(self, text):
    self.buttonDelete.setText(text)
    return self
