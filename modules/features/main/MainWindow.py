
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from modules.generated.main_window_ui import Ui_MainWindow
from modules.features.devices.DeviceLogsWindow import DeviceLogsWindow
from modules.features.devices.DevicesWindow import DevicesWindow
from modules.features.members.MembersWindow import MembersWindow

from modules.features.manager.ManageDialog import ManageDialog
from modules.features.reports.GenerateReportDialog import GenerateReportDialog

class MainApplicationWindow(QMainWindow, Ui_MainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)

    '''Set up actions'''
    self.actionDeviceLogs.triggered.connect(
      lambda: self.showWindow(
        lambda parent: DeviceLogsWindow(parent=parent)
      )
    )

    self.actionDeviceLogs.trigger()
    
    self.actionDevices.triggered.connect(
      lambda: self.showWindow(
        lambda parent: DevicesWindow(parent=parent)
      )
    )


    # Manage
    self.actionDepartment.triggered.connect(
      lambda: self.showDialog(
        lambda: ManageDialog(parent=self) \
          .setManageTitle("Department List")
      )
    )
    self.actionManageDepartments.triggered.connect(
      lambda: self.showDialog(
        lambda: ManageDialog(parent=self) \
          .setManageTitle("Department List")
      )
    )

    self.actionManageMembers.triggered.connect(
      lambda: self.showWindow(
        lambda parent: MembersWindow(parent=parent)
      )
    )
    self.actionMembers.triggered.connect(
      lambda: self.showWindow(
        lambda parent: MembersWindow(parent=parent)
      )
    )

    self.actionManageCategories.triggered.connect(
      lambda: self.showDialog(
        lambda: ManageDialog(parent=self) \
          .setManageTitle("Category List")
      )
    )

    self.actionManageRoles.triggered.connect(
      lambda: self.showDialog(
        lambda: ManageDialog(parent=self) \
          .setManageTitle("Role List")
      )
    )

    # Reports
    self.actionDaily_Report.triggered.connect(
      lambda:
        (dialog := GenerateReportDialog(parent=self)
          , dialog.show())
    )
    self.actionMonthly_Report.triggered.connect(
      lambda:
        (dialog := GenerateReportDialog(parent=self)
          , dialog.show())
    )
    self.actionYearly_Report.triggered.connect(
      lambda:
        (dialog := GenerateReportDialog(parent=self)
          , dialog.show())
    )

  def showDialog(self, factory):
    dialog = factory()
    dialog.show()

    return self

  def showWindow(self, factory):
    win = QMdiSubWindow(parent=self.mdiArea)
    mdiWindowWidget = factory(win)
    win.setWidget(mdiWindowWidget)
    win.show()
    win.setWindowState(Qt.WindowState.WindowMaximized)
    
    return self
