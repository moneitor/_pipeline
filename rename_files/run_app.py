from ui.rename_files import Ui_RenameFiles
from main import run_rename
from PySide2 import QtWidgets

import sys



class CreateUI(QtWidgets.QMainWindow, Ui_RenameFiles):
    def __init__(self):
        super(CreateUI, self).__init__()
        self.setupUi(self)
        self.selected_folder = ""
        self.btn_Go_to_folder.clicked.connect(lambda: self.go_project())
        self.btn_Go_to_folder.clicked.connect(lambda: self.set_line_project_folder())
        self.btn_rename.clicked.connect(lambda: self.rename(self.selected_folder))


    def go_project(self):
        self.selected_folder = QtWidgets.QFileDialog.getExistingDirectory(self,  "Select Folder")


    def set_line_project_folder(self):
        self.line_edit_folder.setText(self.selected_folder)


    def rename(self, path, old_string="", new_string=""):
        self.old_String = self.line_edit_old_word.text()
        self.new_String = self.line_edit_new_word.text()
        if(len(self.old_String) and len(self.new_String)):
            run_rename(path, self.old_String, self.new_String)



if __name__ == "__main__":
    myApp = QtWidgets.QApplication(sys.argv)
    window = CreateUI()
    window.show()
    sys.exit(myApp.exec_())