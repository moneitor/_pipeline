import hou
import os

from PySide2 import QtCore, QtUiTools, QtWidgets, QtGui
from palette import Palette
from files_handling_class import Files_Handling 

hou_name = hou.hipFile.basename()
hou_path = hou.hipFile.path()


root = r'C:\_fxProjects\_projects'

class OpenDialog(QtWidgets.QDialog):
    def __init__(self):
        super(OpenDialog,self).__init__()

        self.path_folder = ""
        self.fx_folder = ""

        self.setWindowTitle("Pipe Open Dialog")
        
        self.setMinimumSize(400,500)
        self.setMaximumSize(400,900)

        self.widgedts()
        self.connections()
        self.layout()

        self.return_path(hou_path)

        self.clear_tree()
        self.get_project_folders()
        self.append_files_to_listWidget(hou_name, hou_path)


    def widgedts(self):
        self.path_line = QtWidgets.QLineEdit()
        self.path_line.setReadOnly(True)
        self.path_line.setPlaceholderText("Please select the SHOT folder")

        self.btn_search = QtWidgets.QPushButton("Search")

        #Projects tree
        self.projects_model = QtWidgets.QFileSystemModule()
        self.tree_projects = QtWidgets.QTreeView()
        #self.tree_projects.setModel
        header = self.tree_projects.headerItem()        
        #self.tree_projects.setMinimumSize(200,450)
        tree_header = self.tree_projects.headerItem()
        tree_header.setText(0, "Projects")




    def connections(self):
        self.btn_search.clicked.connect(self.update_path_text)
        self.btn_search.clicked.connect(self.clear_tree)
        self.btn_search.clicked.connect(lambda: self.append_files_to_listWidget(hou_name, self.path_folder + "/work/fx"))

        self.tree_projects.itemDoubleClicked.connect(self.open_hip_scene)


    def layout(self):
        path_layout = QtWidgets.QHBoxLayout()
        path_layout.addWidget(self.path_line)
        path_layout.addWidget(self.btn_search)

        tree_layout = QtWidgets.QHBoxLayout()
        tree_layout.addWidget(self.tree_projects)
        tree_layout.addStretch()

        organize_layout = QtWidgets.QFormLayout()
        organize_layout.addRow("File Options", path_layout)
        organize_layout.addRow("Files", tree_layout)


        main_layout = QtWidgets.QHBoxLayout(self)
        main_layout.setContentsMargins(2,2,2,2)
        main_layout.addLayout(organize_layout)

    def get_project_folders(self):
        projects = Files_Handling("", root)
        projects.return_project_folders()

        return 


    def update_path_text(self):
        get_folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder", os.chdir(r"C:\_fxProjects\_projects"))
        self.path_folder = get_folder_path
        self.path_line.setText(get_folder_path)


    def return_path(self, path):
        file_object = Files_Handling(hou_name, path)
        file_path = file_object.return_file_path()

        self.fx_folder = file_path
        self.path_folder = file_path
        self.path_line.setText(file_path)            

    def append_files_to_listWidget(self, name="" , path=""):
        files = Files_Handling(name, path)
        list_files = files.return_files_on_dir()
        for file in list_files:
            item = QtWidgets.QTreeWidgetItem([file])
            self.tree_files.addTopLevelItem(item)


    def clear_tree(self):
        self.tree_projects.clear()


    def open_hip_scene(self, element_name):
        path_file = self.path_folder + ("/work/fx/{}".format(element_name.text(0)))
        hou.hipFile.load(path_file)
        print ("Opening file at " + path_file)

            


##########################################################        

def run_open():
    app = OpenDialog()
    app.setStyle(QtWidgets.QStyleFactory.create("fusion"))
    dark_palette = QtGui.QPalette()
    Palette(dark_palette)
    app.setPalette(dark_palette)
    app.exec_()