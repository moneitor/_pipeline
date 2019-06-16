from ui.project_utility import Ui_MainWindow
from PySide2 import QtWidgets
from general_functions import go_folder
import os


temp_path = r'C:\Users\Hernan\Documents\HERNAN\_projects'
#temp_path = r'C:\Users\monei\Documents\HERNAN\_projects'
go_folder(temp_path)


class ProjectUtility(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(ProjectUtility, self).__init__()
        self.setupUi(self)
        self.maximumHeight()
        self.maximumWidth()
        self.selected_folder = ""
        self.setWindowTitle("Project initialization")
        self.btn_go_project.clicked.connect(self.go_project)
        self.btn_go_project.clicked.connect(self.change_label_go_project)
        self.btn_go_project.clicked.connect(self.populate_list_widget)
        self.btn_set_project.clicked.connect(self.create_project)

    def populate_list_widget(self):
        self.listWidget.clear()
        if self.selected_folder:
            x = [x for x in os.listdir(self.selected_folder) if x.endswith(".hip") or x.endswith("nk") or x.endswith("hiplc")
                 or x.endswith("mb") or x.endswith("py")]
            for name in x:
                item = QtWidgets.QListWidgetItem(self.listWidget)
                item.setText(name)
        else:
            QtWidgets.QMessageBox.about(self,"Warning", "Please select a folder")

    def go_project(self):
        self.selected_folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select folder")

    def create_project(self):
        self.selected_folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select folder")
        #create_folders(self.selected_folder, folder_list())
        QtWidgets.QMessageBox.about(self, "Output", "Project folders created")


    def change_label_go_project(self):
            label_text = self.label.setText(self.selected_folder)


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    qt_app = ProjectUtility()

    qt_app.show()
    app.exec_()
