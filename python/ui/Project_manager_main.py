# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project_manager_main.ui',
# licensing of 'Project_manager_main.ui' applies.
#
# Created: Tue May 28 22:56:29 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ProjectManager(object):

    def setupUi_MAIN(self, ProjectManager):
        ProjectManager.setObjectName("ProjectManager")
        ProjectManager.resize(276, 354)
        ProjectManager.setMinimumSize(QtCore.QSize(276, 354))
        ProjectManager.setMaximumSize(QtCore.QSize(276, 354))
        ProjectManager.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(ProjectManager)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        self.btn_newProject = QtWidgets.QPushButton(self.frame_2)
        self.btn_newProject.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_newProject.setObjectName("btn_newProject")
        self.gridLayout_2.addWidget(self.btn_newProject, 0, 2, 1, 1)
        self.ui_project_path = QtWidgets.QLabel(self.frame_2)
        self.ui_project_path.setObjectName("ui_project_path")
        self.gridLayout_2.addWidget(self.ui_project_path, 1, 1, 1, 1)
        self.ui_loadProject = QtWidgets.QPushButton(self.frame_2)
        self.ui_loadProject.setMinimumSize(QtCore.QSize(100, 50))
        self.ui_loadProject.setObjectName("ui_loadProject")
        self.gridLayout_2.addWidget(self.ui_loadProject, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_Houdini = QtWidgets.QPushButton(self.frame)
        self.btn_Houdini.setObjectName("btn_Houdini")
        self.gridLayout.addWidget(self.btn_Houdini, 0, 0, 1, 1)
        self.btn_nuke = QtWidgets.QPushButton(self.frame)
        self.btn_nuke.setObjectName("btn_nuke")
        self.gridLayout.addWidget(self.btn_nuke, 1, 0, 1, 1)
        self.btn_pftrack = QtWidgets.QPushButton(self.frame)
        self.btn_pftrack.setObjectName("btn_pftrack")
        self.gridLayout.addWidget(self.btn_pftrack, 2, 0, 1, 1)
        self.btn_illustrator = QtWidgets.QPushButton(self.frame)
        self.btn_illustrator.setObjectName("btn_illustrator")
        self.gridLayout.addWidget(self.btn_illustrator, 3, 0, 1, 1)
        self.btn_photoshop = QtWidgets.QPushButton(self.frame)
        self.btn_photoshop.setObjectName("btn_photoshop")
        self.gridLayout.addWidget(self.btn_photoshop, 4, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1)
        ProjectManager.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ProjectManager)
        self.statusbar.setObjectName("statusbar")
        ProjectManager.setStatusBar(self.statusbar)

        self.retranslateUi(ProjectManager)
        QtCore.QMetaObject.connectSlotsByName(ProjectManager)


    def retranslateUi(self, ProjectManager):
        ProjectManager.setWindowTitle(QtWidgets.QApplication.translate("ProjectManager", "MainWindow", None, -1))
        self.btn_newProject.setText(QtWidgets.QApplication.translate("ProjectManager", "NEW PROJECT", None, -1))
        self.ui_project_path.setText(QtWidgets.QApplication.translate("ProjectManager", "Project path", None, -1))
        self.ui_loadProject.setText(QtWidgets.QApplication.translate("ProjectManager", "LOAD PROJECT", None, -1))
        self.btn_Houdini.setText(QtWidgets.QApplication.translate("ProjectManager", "Houdini", None, -1))
        self.btn_nuke.setText(QtWidgets.QApplication.translate("ProjectManager", "Nuke", None, -1))
        self.btn_pftrack.setText(QtWidgets.QApplication.translate("ProjectManager", "Pftrack", None, -1))
        self.btn_illustrator.setText(QtWidgets.QApplication.translate("ProjectManager", "Illustrator", None, -1))
        self.btn_photoshop.setText(QtWidgets.QApplication.translate("ProjectManager", "Photoshop", None, -1))
