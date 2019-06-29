from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui
import sys

from ui._pipe_main_project import Ui_ui_main_project
from ui._pipe_new_project import Ui_ui_new_project_dialog
from ui._pipe_open_project import Ui_Dialog



class MainWindow(QtWidgets.QMainWindow, Ui_ui_main_project):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.connections()

    

    def connections(self):
        self.btn_newProject.clicked.connect(self.new_file_dialog)


    def new_file_dialog(self):
        dialog = QtWidgets.QDialog()
        ui = Ui_ui_new_project_dialog()
        ui.setupUi(dialog)
        #dialog.show()
        sys.exit(dialog.exec_())



        print("test")




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_project = MainWindow()
    main_project.show()

    sys.exit(app.exec_())