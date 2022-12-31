from ui_calculator import Ui_MainWindow

import typing
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

class CalculatorWindow(QMainWindow, Ui_MainWindow):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)
    self.setupUi(self)

if __name__ == "__main__":
  app = QApplication(sys.argv)

  calculatorWindow = CalculatorWindow()
  calculatorWindow.show()

  sys.exit(app.exec())