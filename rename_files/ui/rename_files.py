# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rename_files.ui',
# licensing of 'rename_files.ui' applies.
#
# Created: Wed Jun  5 22:00:39 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_RenameFiles(object):
    def setupUi(self, RenameFiles):
        RenameFiles.setObjectName("RenameFiles")
        RenameFiles.resize(357, 216)
        RenameFiles.setMinimumSize(QtCore.QSize(357, 216))
        RenameFiles.setMaximumSize(QtCore.QSize(357, 216))
        self.centralwidget = QtWidgets.QWidget(RenameFiles)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.line_edit_new_word = QtWidgets.QLineEdit(self.frame_2)
        self.line_edit_new_word.setMaximumSize(QtCore.QSize(100, 16777215))
        self.line_edit_new_word.setObjectName("line_edit_new_word")
        self.horizontalLayout_3.addWidget(self.line_edit_new_word)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_edit_folder = QtWidgets.QLineEdit(self.frame_2)
        self.line_edit_folder.setObjectName("line_edit_folder")
        self.horizontalLayout.addWidget(self.line_edit_folder)
        self.btn_Go_to_folder = QtWidgets.QPushButton(self.frame_2)
        self.btn_Go_to_folder.setObjectName("btn_Go_to_folder")
        self.horizontalLayout.addWidget(self.btn_Go_to_folder)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.btn_rename = QtWidgets.QPushButton(self.frame_2)
        self.btn_rename.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_rename.setMaximumSize(QtCore.QSize(100, 50))
        self.btn_rename.setObjectName("btn_rename")
        self.gridLayout_2.addWidget(self.btn_rename, 5, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.line_edit_old_word = QtWidgets.QLineEdit(self.frame_2)
        self.line_edit_old_word.setMaximumSize(QtCore.QSize(100, 16777215))
        self.line_edit_old_word.setObjectName("line_edit_old_word")
        self.horizontalLayout_2.addWidget(self.line_edit_old_word)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        RenameFiles.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RenameFiles)
        self.statusbar.setObjectName("statusbar")
        RenameFiles.setStatusBar(self.statusbar)

        self.retranslateUi(RenameFiles)
        QtCore.QMetaObject.connectSlotsByName(RenameFiles)

    def retranslateUi(self, RenameFiles):
        RenameFiles.setWindowTitle(QtWidgets.QApplication.translate("RenameFiles", "MainWindow", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("RenameFiles", "New word", None, -1))
        self.btn_Go_to_folder.setText(QtWidgets.QApplication.translate("RenameFiles", "Go to folder", None, -1))
        self.btn_rename.setText(QtWidgets.QApplication.translate("RenameFiles", "Rename", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("RenameFiles", "Old word", None, -1))

