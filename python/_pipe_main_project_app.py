from general_functions import run_app , go_folder, create_folders
from houdini_set_env import houdini_env
from apps_path import return_app_path

from store_shot_data import store_data

from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui
import sys
import os

from ui._pipe_main_project import Ui_ui_main_project
from ui._pipe_new_project import Ui_ui_new_project_dialog
from ui._pipe_open_project import Ui_Dialog


class MainWindow(QtWidgets.QMainWindow, Ui_ui_main_project):    

    def __init__(self):
        super(MainWindow, self).__init__()

        self.path = ""

        self.setupUi(self)
        self.connections()
               
    

    def connections(self):  
        self.btn_newProject.clicked.connect(self.new_project_instance)   
        self.btn_houdini.clicked.connect(self.launch_houdini)          
        

    def new_project_instance(self):        
        new_project = NewProjectWindow()        
        result = new_project.exec_()
      
        if result == QtWidgets.QDialog.Accepted:            
            self.label_project_folder.setText(new_project.path)
            self.path = new_project.path
            print("Project {}, has been created".format((new_project.project_name).upper()))
            print("In the folder {}".format(os.getcwd()))
            print("For client {}".format((new_project.client_name).upper()))
            print("With resolution {} x {}".format(new_project.resolution_x, new_project.resolution_y))
            print("with FPS {}".format(new_project.FPS))
            print("The amount of shots is: {}".format(new_project.shot_number))


    def launch_houdini(self):        
        go_folder(self.path, 1, 0)
        houdini_env(self.path)
        run_app(return_app_path()[0])




class NewProjectWindow(Ui_ui_new_project_dialog):

    def __init__(self):
        super(NewProjectWindow, self).__init__()
        self.path = ""
        self.client_name = ""
        self.project_name = ""
        self.resolution_x = 0
        self.resolution_y = 0
        self.FPS = 0
        self.shot_number = 0
        self.setupUi(self)
        self.connections()


    def connections(self):
        self.btn_folder_lookup_2.clicked.connect(self.show_folder_select)
        self.le_clientName_2.textChanged.connect(self.set_client_name)
        self.le_projectName_2.textChanged.connect(self.set_project_name)
        self.ui_resolution_x_2.valueChanged.connect(self.store_resolution_x)
        self.ui_resolution_y_2.valueChanged.connect(self.store_resolution_y)
        #self.ui_shotNumber_2.valueChanged.connect(self.shot_number)


        self.btn_OK.clicked.connect(self.Ok_pressed)
        self.btn_OK.clicked.connect(self.accept) 


    def Ok_pressed(self):
        # set values to defaults if not changed        
        self.resolution_x = self.ui_resolution_x_2.text()
        self.resolution_y = self.ui_resolution_y_2.text()
        self.FPS = self.le_fps_2.text()
        self.shot_number = self.ui_shotNumber_2.text()
        create_folders(self.shot_number, self.path)
        store_data(self.path, self.shot_number, [self.resolution_x, self.resolution_y], self.FPS, self.client_name, self.project_name)
        #TODO Test if a folder was actually created


    def show_folder_select(self):        
        new_directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder", os.chdir(r"C:/_fxProjects/_projects"))
        if new_directory:
            self.path = new_directory
            self.le_projectPath_2.setText(self.path)
            os.chdir(self.path)           

        return self.path


    def set_client_name(self):
        self.client_name = self.le_clientName_2.text()


    def set_project_name(self):
        self.project_name = self.le_projectName_2.text()


    def store_resolution_x(self):
        self.resolution_x = self.ui_resolution_x_2.text()


    def store_resolution_y(self):
        self.resolution_y = self.ui_resolution_y_2.text()

    def setFPS(self):
        self.FPS = self.le_fps_2.text()

"""
    def shot_number(self):
        self.shot_number = int(self.ui_shotNumber_2.text())
        """
        


        

             
def testNew():
    app = QtWidgets.QApplication(sys.argv)
    ui = NewProjectWindow()
    ui.show()
    app.exec_()


def testMain():
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    testMain()
