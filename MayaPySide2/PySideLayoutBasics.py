from PySide2 import QtCore, QtWidgets
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui


def MayaMainWindow():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class testDialog(QtWidgets.QDialog):
    def __init__(self, parent=MayaMainWindow()):
        super(testDialog, self).__init__(parent)
        self.setMinimumSize(200,200)
        self.setWindowTitle("my maya shit")        
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        
        self.create_widgets()
        self.create_layouts()
        
    def create_widgets(self):
        self.lineedit = QtWidgets.QLineEdit()
        self.checkbox1 = QtWidgets.QCheckBox("checkbox1")
        self.checkbox2 = QtWidgets.QCheckBox("checkbox2")
        self.btn_OK = QtWidgets.QPushButton("OK")
        self.btn_Cancel = QtWidgets.QPushButton("Cancel")
        
    def create_layouts(self):
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow("Name" , self.lineedit)
        form_layout.addRow("Hidden", self.checkbox1)
        form_layout.addRow("Locked" , self.checkbox2)
        
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.btn_OK)
        button_layout.addWidget(self.btn_Cancel)
                                
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
       
               
        
if __name__ == "__main__":
    
    w = testDialog()
    w.show()
    
        