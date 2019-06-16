from PySide2 import QtCore, QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)
    
class OpenImportDialog(QtWidgets.QDialog):
    
    def __init__(self, parent=maya_main_window()):
        super(OpenImportDialog, self).__init__(parent)
        
        self.setWindowTitle("Open/Import/Reference")
        self.setMinimumSize(300,80)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        
        self.create_widgets()
        self.create_layout()
        self.create_connections()
        
    def create_widgets(self):
        self.filepath_le = QtWidgets.QLineEdit()
        self.select_file_path_btn = QtWidgets.QPushButton("...")
        
        self.open_rb = QtWidgets.QRadioButton("Open")
        self.open_rb.setChecked(True)
        self.import_rb = QtWidgets.QRadioButton("Import")
        self.reference_rb = QtWidgets.QRadioButton("Reference")
        
        self.force_cb = QtWidgets.QCheckBox("Force")
        
        self.apply_btn = QtWidgets.QPushButton("Apply")
        self.close_btn = QtWidgets.QPushButton("Close")
        
        
    def create_layout(self):
        file_path_layout = QtWidgets.QHBoxLayout() #horizontal layout
        file_path_layout.addWidget(self.filepath_le)#Buttons are gonna be in the horizontal layout
        file_path_layout.addWidget(self.select_file_path_btn)
        
        radio_btn_layout = QtWidgets.QHBoxLayout()#layout for the buttons
        radio_btn_layout.addWidget(self.open_rb)
        radio_btn_layout.addWidget(self.import_rb)
        radio_btn_layout.addWidget(self.reference_rb)
        
        form_layout = QtWidgets.QFormLayout()#layout that store rows, you can put a name and                                             
        form_layout.addRow("File: ", file_path_layout)#and the widget next to it
        form_layout.addRow("", radio_btn_layout)
        form_layout.addRow("", self.force_cb)
        
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.apply_btn)
        button_layout.addWidget(self.close_btn)
        
        main_layout = QtWidgets.QVBoxLayout(self)#main layout to contain the others
        main_layout.addLayout(form_layout)  
        main_layout.addLayout(button_layout)      
        
        
    def create_connections(self):
        self.select_file_path_btn.clicked.connect(self.show_file_select_dialog)
        
        self.open_rb.toggled.connect(self.update_force_visibility)
        
        self.apply_btn.clicked.connect(self.load_file)
        self.close_btn.clicked.connect(self.close)
       
    def show_file_select_dialog(self):
        pass
        
    def update_force_visibility(self):
        pass
        
    def load_file(self):
        pass
        
     
if __name__ == "__main__":
    try:
        open_import_dialog.close()
        open_import_dialog.deleteLater()
    except:
        pass
        
    open_import_dialog = OpenImportDialog()
    open_import_dialog.show()
 
