from general_functions import run_app , go_folder, create_folders, create_project_message
from houdini_set_env import houdini_env
from apps_path import return_app_path

from palette import Palette

from store_shot_data import store_data, save_project_info, read_projects_info

from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui

import sys
import os
import json

from ui._pipe_main_project import Ui_ui_main_project
from ui._pipe_new_project import Ui_ui_new_project_dialog
from ui._pipe_open_project import Ui_Dialog


class MainWindow(QtWidgets.QMainWindow, Ui_ui_main_project):    

    def __init__(self):
        super(MainWindow, self).__init__()

        self.path = ""

        self.setupUi(self)
        self.update_projects_list()
        self.update_project_widget()
        self.connections()              
    

    def connections(self):  
        self.btn_newProject.clicked.connect(self.new_project_instance)  
        self.btn_goProject.clicked.connect(self.show_folder_select) 
        self.btn_houdini.clicked.connect(self.launch_houdini)  
        self.btn_Nuke.clicked.connect(self.launch_nuke)

        self.list_project_widget.doubleClicked.connect(self.look_for_path_from_list)


    def update_projects_list(self):
        info_path = "C:/_fxProjects/_projects/projects_info.json"
        project_list = []
        projects = ""
        with open(info_path, "r") as projects_info:
            projects = json.load(projects_info)            
            for project in projects:
                project_name = project["folder"]
                project_list.append(project_name)

        return project_list, projects

    def update_project_widget(self):
        self.list_project_widget.clear()
        list_projects = self.update_projects_list()[0]
        for project in list_projects:            
            self.list_project_widget.addItem(project)
            self.list_project_widget


    def look_for_path_from_list(self, item_list):
        list_projects = self.update_projects_list()[1]
        project_path = ""
        for project in list_projects:
            if item_list.data() == project["folder"]:
                project_path = project["project_path"]
        
        self.path = project_path
        self.label_project_folder.setText(self.path)               
                

    def new_project_instance(self):        
        new_project = NewProjectWindow()        
        result = new_project.exec_()
        
        #if the boton ok is pressed then it will change the label text in the main window
        if result == QtWidgets.QDialog.Accepted:                        
            self.label_project_folder.setText(new_project.path)
            self.path = new_project.path
            

    def show_folder_select(self):        
        new_directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder", os.chdir(r"C:/_fxProjects/_projects"))
        if new_directory:
            self.path = new_directory
            self.label_project_folder.setText(self.path)
            os.chdir(self.path)           

        return self.path
            

    def launch_houdini(self):    
        if len(self.path) > 0 :  
            go_folder(self.path, 1, 1)
            houdini_env(self.path, return_app_path()[1], return_app_path()[2], self.path)
            run_app(return_app_path()[0])
        else:
            msg = QtWidgets.QMessageBox()
            msg.setText("Please open or create a new project first.")
            msg.exec_()


    def launch_nuke(self):
        if len(self.path) > 0:
            go_folder(self.path, 0, 1)
            run_app(return_app_path()[5])
        else:
            create_project_message()



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
       

        self.btn_OK.clicked.connect(self.Ok_pressed)
        self.btn_OK.clicked.connect(self.accept) 


    def Ok_pressed(self):
        # set values to defaults if not changed     
        if len(self.path) > 1:   
            self.resolution_x = self.ui_resolution_x_2.text()
            self.resolution_y = self.ui_resolution_y_2.text()
            self.FPS = self.le_fps_2.text()
            self.shot_number = self.ui_shotNumber_2.text()
            create_folders(self.shot_number, self.path)
            store_data(self.path, self.shot_number, [self.resolution_x, self.resolution_y], self.FPS, self.client_name, self.project_name)
            save_project_info(self.project_name, self.path)            
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Please specify a project folder")
            msgBox.exec_()


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

      


def Main():
    app = QtWidgets.QApplication(sys.argv)

    app.setStyle(QtWidgets.QStyleFactory.create("fusion"))

    dark_palette = QtGui.QPalette()
    Palette(dark_palette)
    

    app.setPalette(dark_palette)

    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    Main()
