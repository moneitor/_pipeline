from ui.Project_manager_main import Ui_ProjectManager
from ui.Project_manager_NewProject import Ui_NewProject
from PySide2 import QtWidgets
from general_functions import go_folder
import sys
import os

temp_path = r'C:\Users\Hernan\Documents\HERNAN\_projects'
# temp_path = r'C:\Users\monei\Documents\HERNAN\_projects'
go_folder(temp_path)


class UiCreationMain(Ui_ProjectManager, Ui_NewProject, QtWidgets.QMainWindow):
    def __init__(self):
        super(UiCreationMain, self).__init__()
        self.setupUi_MAIN(self)
        self.btn_newProject.clicked.connect(lambda: self.openNewProject())

    def openNewProject(self):
        app_NEW_PROJECT = QtWidgets.QApplication(sys.argv)
        qt_app_NEW_PROJECT = Ui_NewProject.setupUi_NEW_PROJECT()

        qt_app_NEW_PROJECT.show()
        app.instance().quit






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = UiCreationMain()

    qt_app.show()
    sys.exit(app.exec_())
