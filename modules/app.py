
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

import sys
import signal

from modules.features.main.MainWindow import MainApplicationWindow

def start():
  # Setup Ctrl - C interceptors
  signal.signal(signal.SIGINT, signal.SIG_DFL)

  # Create an instance of QT application
  app = QApplication(sys.argv)

  window = MainApplicationWindow(parent=None)
  window.show()
  window.setWindowState(Qt.WindowState.WindowMaximized)

  # window.load_data()

  sys.exit(app.exec())
