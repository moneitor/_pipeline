from PySide2 import QtWidgets
from PySide2.QtGui import *
from PySide2 import QtCore
from PySide2 import QtGui
import sys
import os


class CustomDialog(QtWidgets.QDialog):
    """
    A simple dialog for getting a user's name
    """

    def __init__(self):
        super(CustomDialog, self).__init__()

        self.setWindowTitle("Custom Dialog")
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.lineedit = QtWidgets.QLineEdit()
        self.ok_btn = QtWidgets.QPushButton("OK")

    def create_layout(self):
        wdg_layout = QtWidgets.QHBoxLayout()
        wdg_layout.addWidget(QtWidgets.QLabel("Name: "))
        wdg_layout.addWidget(self.lineedit)

        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.ok_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(wdg_layout)
        main_layout.addLayout(btn_layout)

    def create_connections(self):
        self.ok_btn.clicked.connect(self.accept)

    def get_text(self):
        return(self.lineedit.text())



class TestDialog(QtWidgets.QDialog):
    """
    Main dialog for displaying modal dialogs
    """

    def __init__(self):
        super(TestDialog, self).__init__()

        self.setWindowTitle("Test Dialog")
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        #self.initial_directory = cmds.internalVar(userPrefDir=True)
        self.initial_color = QtGui.QColor(255, 0, 0)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.warning_btn = QtWidgets.QPushButton("Warning")
        self.folder_select_btn = QtWidgets.QPushButton("Folder Select")
        self.color_select_btn = QtWidgets.QPushButton("Color Select")
        self.custom_btn = QtWidgets.QPushButton("Modal (Custom)")

    def create_layout(self):
        main_layout = QtWidgets.QHBoxLayout(self)
        main_layout.addWidget(self.warning_btn)
        main_layout.addWidget(self.folder_select_btn)
        main_layout.addWidget(self.color_select_btn)
        main_layout.addWidget(self.custom_btn)

    def create_connections(self):
        self.warning_btn.clicked.connect(self.show_warning_dialog)
        self.folder_select_btn.clicked.connect(self.show_folder_select)
        self.color_select_btn.clicked.connect(self.show_color_select)
        self.custom_btn.clicked.connect(self.show_custom_dialog)


    def show_warning_dialog(self):
        """
        Display Qt's warning message dialog
        """
        QtWidgets.QMessageBox.warning(self, "Object Not Found", "Camera 'shotcam' not found.")


    def show_folder_select(self):
        """
        Display Qt's folder select dialog
        """
        new_directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder", os.getcwd())
        if new_directory:
            self.initial_directory = new_directory

        print("Selected Folder: {0}".format(new_directory))


    def show_color_select(self):
        """
        Display Qt's color select dialog
        """
        self.initial_color = QtWidgets.QColorDialog.getColor(self.initial_color, self)

        print("Red:{0} Green:{1} Blue:{2}".format(self.initial_color.red(),
                                                  self.initial_color.green(),
                                                  self.initial_color.blue()))


    def show_custom_dialog(self):
        """
        Display a user created dialog
        """
        custom_dialog = CustomDialog()

        result = custom_dialog.exec_()

        if result == QtWidgets.QDialog.Accepted:
            print("Name: {0}".format(custom_dialog.get_text()))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = TestDialog()
    w.show()

    app.exec_()
