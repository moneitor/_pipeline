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
        pass
        
    def create_layout(self):
        pass
        
    def create_connections(self):
        pass
        
     
if __name__ == "__main__":
    try:
        open_import_dialog.close()
        open_import_dialog.deleteLater()
    except:
        pass
        
    open_import_dialog = OpenImportDialog()
    open_import_dialog.show()
 
