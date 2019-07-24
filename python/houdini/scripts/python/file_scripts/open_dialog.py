from PySide2 import QtWidgets, QtCore, QtGui
from palette import Palette
import hou
import os

parentHou = hou.ui.mainQtWindow()

temp_elements = ["ascensor", "portal", "animum", "utilities"]
temp_shots_ascensor = ["shot1", "shot2", "shot3", "shot4"]
temp_shots_portal = ["shot1", "shot2", "shot3"]
temp_shots_animum = ["shot1", "shot2", "shot3", "shot4", "shot5", "shot6"]
temp_shots_utilities = ["shot1", "shot2"]

root = r'C:\_fxProjects\_projects'

class OpenDialog(QtWidgets.QDialog):
    def __init__(self, parent=parentHou ):
        super(OpenDialog, self).__init__()
        self.setWindowTitle("Open File")

        self.current_project = ""
        self.current_shot = ""
        self.current_file = ""

        self.widgets()
        self.connections()
        self.layout()

        self.update_projects_tree(self.return_projects_folders())


    def widgets(self):
        self.line_search_label = QtWidgets.QLabel("Search")
        self.line_search = QtWidgets.QLineEdit()

        self.line_search_label.setBuddy(self.line_search)

        self.projects_tree = QtWidgets.QTreeWidget()
        self.projects_tree.setMaximumWidth(150)
        self.projects_tree.setColumnCount(1)
        self.projects_tree.setHeaderLabels(["Projects"])

        self.shots_tree = QtWidgets.QTreeWidget()
        self.shots_tree.setMaximumWidth(150)
        self.shots_tree.setColumnCount(1)
        self.shots_tree.setHeaderLabels(["Shots"])

        self.files_tree = QtWidgets.QTreeWidget()
        self.files_tree.setMaximumWidth(150)
        self.files_tree.setColumnCount(1)
        self.files_tree.setHeaderLabels(["Files"])

        self.btn_save = QtWidgets.QPushButton("Save")


    def connections(self):
        self.btn_save.clicked.connect(self.close)
        self.projects_tree.itemDoubleClicked.connect(lambda: self.update_shots_tree(temp_shots_portal))

    def layout(self):
        # Projects tree related
        projects_layout = QtWidgets.QHBoxLayout()
        projects_layout.addWidget(self.line_search_label)
        projects_layout.addWidget(self.line_search)
        projects_layout.addStretch()

        vertical_layout_1 = QtWidgets.QVBoxLayout()
        vertical_layout_1.addLayout(projects_layout)
        vertical_layout_1.addWidget(self.projects_tree)

        # Shot step related
        shots_layout = QtWidgets.QVBoxLayout()
        shots_layout.addWidget(self.shots_tree)

        # Files step related
        files_layout = QtWidgets.QVBoxLayout()
        files_layout.addWidget(self.files_tree)

        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.addLayout(vertical_layout_1)
        horizontal_layout.addLayout(shots_layout)
        horizontal_layout.addLayout(files_layout)
        horizontal_layout.addStretch()

        horizontal_open_form = QtWidgets.QFormLayout()
        horizontal_open_form.addWidget(self.btn_save)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(horizontal_layout)
        main_layout.addLayout(horizontal_open_form)

    def create_project_path(self, project):
        """Returns the path to the folder selected in the projects_tree widget"""
        project_path = r"C:\_fxProjects\_projects\{}".format(project)
        return project_path

    def return_projects_folders(self):
        """Return the list of projects inside the pipeline"""
        project_folders = []
        all_folders = os.listdir(root)
        for element in all_folders:
            if not os.path.isdir(element):
                project_folders.append(element)

        return project_folders

    def update_projects_tree(self, elements):
        """Updates the projects tree Widget with the list of the projects
        that are currently being worked within the pipeline"""
        for item in elements:
            projects_item = QtWidgets.QTreeWidgetItem([item])
            self.projects_tree.addTopLevelItem(projects_item)

    def return_shots_per_project(self, project):
        """"Returns a list of all the Shot folders in the selected project"""
        # TODO return the list of the shots that are present in the actual shot
        shot_list = []
        project_path = self.create_project_path(project)
        for folder in os.listdir(project_path):
            if folder.startswith("Shot"):
                shot_list.append(folder)
        # create a list of all the files starting with shot in the folder
        # return the list
        self.current_project = project_path.split("\\")[-1]
        return shot_list

    def update_shots_tree(self, project):
        """Updates the shots_tree Widget with the folders contained inside the current project"""
        self.shots_tree.clear()
        shots = self.return_shots_per_project(project)
        for shot in shots:
            shots_item = QtWidgets.QTreeWidgetItem([shot])
            self.shots_tree.addTopLevelItem(shots_item)

    def update_files_tree(self):
        """Updates the files_tree with the current hip files included within the selected shot"""
        # build the path to the files based on the project and the shot
        # check what files that end with .hip currently exist in the folder
        #update the file_tree widget with this list

        # Return the path to the file
        pass

    def return_file_path(self):
        """Create the absolute path to the file so it can be open by the self.open_file method"""
        # Build the final file path with extension based on the selected project and selected shot

    def open_file(self):
        pass





def run_open():
    open_app = OpenDialog()

    open_app.setStyle(QtWidgets.QStyleFactory.create("fusion"))
    dark_palette = QtGui.QPalette()
    Palette(dark_palette)
    open_app.setPalette(dark_palette)

    open_app.exec_()
