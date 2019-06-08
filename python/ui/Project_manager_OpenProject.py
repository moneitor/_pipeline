# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project_manager_OpenProject.ui',
# licensing of 'Project_manager_OpenProject.ui' applies.
#
# Created: Tue May 28 22:56:50 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_OpenProject(object):
    def setupUi_OPEN_PROJECT(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(314, 400)
        MainWindow.setMinimumSize(QtCore.QSize(314, 400))
        MainWindow.setMaximumSize(QtCore.QSize(314, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ui_projectPath = QtWidgets.QLineEdit(self.frame)
        self.ui_projectPath.setObjectName("ui_projectPath")
        self.horizontalLayout.addWidget(self.ui_projectPath)
        self.btn_folder_lookup = QtWidgets.QToolButton(self.frame)
        self.btn_folder_lookup.setObjectName("btn_folder_lookup")
        self.horizontalLayout.addWidget(self.btn_folder_lookup)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.ui_projectPath.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Project path...", None, -1))
        self.btn_folder_lookup.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Existing files", None, -1))

