from PySide2 import QtCore, QtWidgets, QtGui
from shiboken2 import wrapInstance

import maya.OpenMaya as om
import maya.OpenMayaUI as omui

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)
    
class OpenImportDialog(QtWidgets.QDialog):
    
    FILE_FILTERS = "Maya (* .ma *.mb);;Maya ASCII (*.ma)::Maya Binary (*.mb);;All Files(*.*)"
    
    selected_filter = "Maya (*.ma *.mb)"
    
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
        self.select_file_path_btn = QtWidgets.QPushButton()
        self.select_file_path_btn.setIcon(QtGui.QIcon(":fileOpen.png"))# "name"  means is a resource
        self.select_file_path_btn.setToolTip("Select File")
        
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
        file_path, self.selected_filter = QtWidgets.QFileDialog.getOpenFileName(self, "Select File", "" ,self.FILE_FILTERS, self.selected_filter)
        if file_path:
            self.filepath_le.setText(file_path)
        
    def update_force_visibility(self, checked):
        self.force_cb.setVisible(checked)
        
    def load_file(self):
        print("TODO: load file")
        
    def load_file(self, file_path):
        file_path = self.filepath_le.text()
        if not file_path:
            return
            
        file_info = QtCore.QFileInfo(file_path)
        if not file_info.exists():
            om.MGlobal.displayError("File does not exist")
        
        if self.open_rb.isChecked(file_path):
            self.open_file
        elif self.import_rb.isChecked(file_path):
            self.import_file
        else:
            self.reference_file(file_path)
            
        
        
    def open_file(self, file_path):
        pass
        
    def import_file(self, file_path):
        pass
        
    def reference_file(self, file_path):
        pass
        
     
        
     
if __name__ == "__main__":
    try:
        open_import_dialog.close()
        open_import_dialog.deleteLater()
    except:
        pass
        
    open_import_dialog = OpenImportDialog()
    open_import_dialog.show()
 
