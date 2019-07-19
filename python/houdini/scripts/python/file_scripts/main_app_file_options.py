from PySide2 import QtWidgets, QtCore, QtGui
from palette import Palette
import hou
import json

import os
import sys


tempName = "ASCENSOR"
parentHou = hou.ui.mainQtWindow()


class FileHandling:
    """
    This class handles Houdini files
    and its paths and versions
    """
    def __init__(self, name, path):
        self.this_path = path
        self.this_name = name
        self.full_path = ""

    def path(self):
        return self.this_path

    def name(self):
        return self.this_name

    def complete_path(self, shot):
        additional_path = "/Shot_{}/work/fx/".format(shot)
        saving_path = self.this_path + additional_path
        self.full_path = self.this_path + additional_path + self.this_name + ".hip"
        return self.full_path, saving_path




class FileSave(QtWidgets.QDialog):
    """
    File Saving dialog
    """
    def __init__(self, parent=parentHou):
        super(FileSave, self).__init__()

        self.project_name = ""        
        self.full_path = ""
        self.shot_value = 0
        self.version_value = 0
        self.full_name_for_save = ""
        self.fx_folder_path = ""
        self.project_main_name = ""

        self.setMinimumSize(600, 200)
        self.setMaximumSize(700, 200)

        self.create_widgets()
        self.create_connections()
        self.create_layout()

        self.changed_name()
        self.changed_shot()
        self.changed_version()
        self.changed_path()


    def create_widgets(self):
        """
        Widget creation for the interface
        """
        self.folder_edit = QtWidgets.QLineEdit()
        self.folder_lookup = QtWidgets.QPushButton("Search")

        self.save_file = QtWidgets.QPushButton("Save")
        self.save_file.setMaximumSize(100,50)
        self.setWindowTitle("Pipeline Save")

        self.shot = QtWidgets.QSpinBox()
        self.shot.setMaximumSize(70,20)
        self.shot.setMinimum(1)

        self.version = QtWidgets.QSpinBox()
        self.version.setMaximumSize(70, 20)
        self.version.setMinimum(1)

        self.name = QtWidgets.QLineEdit()
        self.name.setFrame(True)

        self.cancel = QtWidgets.QPushButton("Cancel")
        self.cancel.setMaximumSize(100, 50)

        self.full_name_display = QtWidgets.QLabel(self.return_name("TEST", "NAME", "SHOT", "VERSION"))
        self.complete_path = QtWidgets.QLabel(self.return_path(self.full_path, self.project_name))

    def create_connections(self):
        """
        Connections between the widgets and the functions
        """
        self.folder_lookup.clicked.connect(self.get_folder)
        self.folder_lookup.clicked.connect(self.changed_path)
        self.folder_lookup.clicked.connect(lambda: self.return_project_name(self.full_path))

        self.name.textChanged.connect(self.changed_name)
        self.name.textChanged.connect(self.changed_shot)
        self.name.textChanged.connect(self.changed_version)
        self.name.textChanged.connect(self.changed_path)

        self.shot.valueChanged.connect(self.changed_name)
        self.shot.valueChanged.connect(self.changed_shot)
        self.shot.valueChanged.connect(self.changed_version)
        self.shot.valueChanged.connect(self.changed_path)

        self.version.valueChanged.connect(self.changed_name)
        self.version.valueChanged.connect(self.changed_shot)
        self.version.valueChanged.connect(self.changed_version)
        self.version.valueChanged.connect(self.changed_path)

        self.save_file.clicked.connect(lambda: self.save_file_ui((self.full_name_for_save)))
        self.save_file.clicked.connect(self.close)
        self.cancel.clicked.connect(self.close)



    def create_layout(self):
        """
        Layout configuration and addition of the Widgets
        """
        folder_layout = QtWidgets.QHBoxLayout()
        folder_layout.addWidget(self.folder_edit)
        folder_layout.addWidget(self.folder_lookup)

        form_layout_parms = QtWidgets.QFormLayout()
        form_layout_parms.addRow("Name: ", self.name)
        form_layout_parms.addRow("Shot", self.shot)
        form_layout_parms.addRow("Version", self.version)

        form_layout_names = QtWidgets.QFormLayout()
        form_layout_names.addRow("Name Display: ", self.full_name_display)
        form_layout_names.addRow("Full Path Display: ", self.complete_path)

        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.save_file)
        buttons_layout.addWidget(self.cancel)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(folder_layout)
        main_layout.addStretch()
        main_layout.addLayout(form_layout_parms)
        main_layout.addStretch()
        main_layout.addLayout(form_layout_names)
        main_layout.addStretch()
        main_layout.addLayout(buttons_layout)

    def get_folder(self):
        """
        Get the folder path where we are gonna store the houdini files,
        set the full_path class attribute to the path of the folder and
        set the foder_edit LineEdit text to the same path
        """
        get_folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder", os.chdir(r"C:\_fxProjects\_projects"))
        self.full_path = get_folder_path
        self.folder_edit.setText(get_folder_path)

    def return_path(self, path, name):
        project_file = FileHandling(name, path).complete_path(self.shot_value)[0]
        self.fx_folder_path = FileHandling(name, path).complete_path(self.shot_value)[1]
        self.full_name_for_save = project_file
        print(self.fx_folder_path)
        return project_file

    def changed_path(self):
        self.complete_path.setText(self.return_path(self.full_path, self.changed_name()))

    def return_name(self, project , name, shot, version):
        return("{}_{}_{}_{}".format(project, name, shot, version))

    def changed_shot(self):
        self.shot_value = self.shot.text()

    def changed_version(self):
        self.version_value = self.version.text()

    def return_project_name(self, path):
        info = ""
        with open(self.full_path + "/project_info.json", "r") as json_info:
            info = json.load(json_info)
        self.project_main_name = info["Project name"]

    def changed_name(self):
        name = self.name.text()
        self.project_name = name
        full_name = self.return_name(self.project_main_name, self.project_name, "SH{}".format(self.shot_value), "VER{}".format(self.version_value))        
        self.full_name_display.setText(full_name)
        return full_name   

    def save_file_ui(self, path):
        if(os.path.isdir(self.fx_folder_path)):
            hou.hipFile.save(path, True)
        else:
            msgBox = QtWidgets.QMessageBox(self)
            msgBox.setText("The shot folder doesn't exist")
            msgBox.exec_()


    #####################################################################################

def run_app():
    app = FileSave()
    app.setStyle(QtWidgets.QStyleFactory.create("fusion"))
    dark_palette = QtGui.QPalette()
    Palette(dark_palette)
    app.setPalette(dark_palette)

    app.exec_()
