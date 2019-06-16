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
        #self.QDialog.QPushButton("test" , self)
        
if __name__ == "__main__":
    
    w = testDialog()
    w.show()
    