# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/atmanand/Projects/AcademicsCSE/College/Attendance/modules/gui/device_logs.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(932, 480)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(9, 0, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.topPanel = QtWidgets.QVBoxLayout()
        self.topPanel.setContentsMargins(6, 6, 6, 6)
        self.topPanel.setObjectName("topPanel")
        self.filterPanel = QtWidgets.QVBoxLayout()
        self.filterPanel.setObjectName("filterPanel")
        self.basicFilterOptions = QtWidgets.QHBoxLayout()
        self.basicFilterOptions.setObjectName("basicFilterOptions")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.basicFilterOptions.addWidget(self.label)
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setObjectName("dateEdit")
        self.basicFilterOptions.addWidget(self.dateEdit)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.basicFilterOptions.addWidget(self.label_2)
        self.dateEdit_2 = QtWidgets.QDateEdit(Form)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.basicFilterOptions.addWidget(self.dateEdit_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.basicFilterOptions.addWidget(self.label_3)
        self.comboBoxDevice = QtWidgets.QComboBox(Form)
        self.comboBoxDevice.setObjectName("comboBoxDevice")
        self.basicFilterOptions.addWidget(self.comboBoxDevice)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.basicFilterOptions.addItem(spacerItem)
        self.filterPanel.addLayout(self.basicFilterOptions)
        self.filterGroup = QtWidgets.QGroupBox(Form)
        self.filterGroup.setObjectName("filterGroup")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.filterGroup)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.filterOptions = QtWidgets.QHBoxLayout()
        self.filterOptions.setObjectName("filterOptions")
        spacerItem1 = QtWidgets.QSpacerItem(92, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.filterOptions.addItem(spacerItem1)
        self.matchWholeWord = QtWidgets.QCheckBox(self.filterGroup)
        self.matchWholeWord.setObjectName("matchWholeWord")
        self.filterOptions.addWidget(self.matchWholeWord)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.filterOptions.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.filterOptions, 1, 0, 1, 1)
        self.filterLayout = QtWidgets.QHBoxLayout()
        self.filterLayout.setObjectName("filterLayout")
        self.labelMemberCode = QtWidgets.QLabel(self.filterGroup)
        self.labelMemberCode.setObjectName("labelMemberCode")
        self.filterLayout.addWidget(self.labelMemberCode)
        self.inputEmployeeCode = QtWidgets.QLineEdit(self.filterGroup)
        self.inputEmployeeCode.setObjectName("inputEmployeeCode")
        self.filterLayout.addWidget(self.inputEmployeeCode)
        self.label_5 = QtWidgets.QLabel(self.filterGroup)
        self.label_5.setObjectName("label_5")
        self.filterLayout.addWidget(self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.filterGroup)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.filterLayout.addWidget(self.lineEdit_2)
        self.label_6 = QtWidgets.QLabel(self.filterGroup)
        self.label_6.setObjectName("label_6")
        self.filterLayout.addWidget(self.label_6)
        self.comboBox_2 = QtWidgets.QComboBox(self.filterGroup)
        self.comboBox_2.setObjectName("comboBox_2")
        self.filterLayout.addWidget(self.comboBox_2)
        self.label_7 = QtWidgets.QLabel(self.filterGroup)
        self.label_7.setObjectName("label_7")
        self.filterLayout.addWidget(self.label_7)
        self.comboBox_3 = QtWidgets.QComboBox(self.filterGroup)
        self.comboBox_3.setObjectName("comboBox_3")
        self.filterLayout.addWidget(self.comboBox_3)
        self.label_8 = QtWidgets.QLabel(self.filterGroup)
        self.label_8.setObjectName("label_8")
        self.filterLayout.addWidget(self.label_8)
        self.comboBox_4 = QtWidgets.QComboBox(self.filterGroup)
        self.comboBox_4.setObjectName("comboBox_4")
        self.filterLayout.addWidget(self.comboBox_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.filterLayout.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.filterLayout, 0, 0, 1, 1)
        self.filterPanel.addWidget(self.filterGroup)
        self.topPanel.addLayout(self.filterPanel)
        self.gridLayout.addLayout(self.topPanel, 1, 0, 1, 1)
        self.tableLayout = QtWidgets.QVBoxLayout()
        self.tableLayout.setObjectName("tableLayout")
        self.table = QtWidgets.QTableView(Form)
        self.table.setObjectName("table")
        self.tableLayout.addWidget(self.table)
        self.gridLayout.addLayout(self.tableLayout, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Device Logs"))
        self.label.setText(_translate("Form", "From Date"))
        self.label_2.setText(_translate("Form", "To Date"))
        self.label_3.setText(_translate("Form", "Devices"))
        self.filterGroup.setTitle(_translate("Form", "Filter member"))
        self.matchWholeWord.setText(_translate("Form", "Match Whole Word"))
        self.labelMemberCode.setText(_translate("Form", "Member Code"))
        self.label_5.setText(_translate("Form", "Member Name"))
        self.label_6.setText(_translate("Form", "Department"))
        self.label_7.setText(_translate("Form", "Year"))
        self.label_8.setText(_translate("Form", "Status"))
from . import main_rc
