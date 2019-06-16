from PySide2 import QtCore, QtWidgets
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui


def MayaMainWindow():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class testDialog(QtWidgets.QDialog):
    def __init__(self, parent=MayaMainWindow()):
        super(testDialog, self).__init__(parent)
        self.setMinimumSize(300,300)
        self.setWindowTitle("my maya shit")        
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        
        self.create_widgets()
        self.create_layouts()
        
    def create_widgets(self):
        self.lineedit = QtWidgets.QLineEdit(parent=self)
        self.checkbox1 = QtWidgets.QCheckBox("checkbox1")
        self.checkbox2 = QtWidgets.QCheckBox("checkbox2")
        self.button1 = QtWidgets.QPushButton("Button1")
        self.button2 = QtWidgets.QPushButton("Button2")
        
    def create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.lineedit)
        main_layout.addWidget(self.checkbox1)
        main_layout.addWidget(self.checkbox2)
        main_layout.addWidget(self.button1)
        main_layout.addWidget(self.button2)
        
if __name__ == "__main__":
    
    w = testDialog()
    w.show()
    
        