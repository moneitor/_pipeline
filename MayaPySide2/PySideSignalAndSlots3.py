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
        self.create_connections()
        
    def create_widgets(self):
        self.combobox = QtWidgets.QComboBox()
        self.combobox.addItems(["ComboBoxItem 1" , "ComboBoxItem 2" , "ComboBoxItem 3"])        
        
        self.btn_OK = QtWidgets.QPushButton("OK")
        self.btn_Cancel = QtWidgets.QPushButton("Cancel")
        
    def create_layouts(self):
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow("Combo Box", self.combobox)
                       
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.btn_OK)
        button_layout.addWidget(self.btn_Cancel)
                                
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        
    def create_connections(self):       
        self.combobox.activated.connect(self.on_activated_int)
        # we are using [str] to force pyqt to read the signal as string
        self.combobox.activated[str].connect(self.on_activated_string)
        self.btn_Cancel.clicked.connect(self.close)
        
    @QtCore.Slot(int)
    def on_activated_int(self, index):
        print("Combobox Index: {}".format(index))
        
    @QtCore.Slot(str)
    def on_activated_string(self, text):
        print("ComboBox  text: {}".format(text))
      
               
        
if __name__ == "__main__":
    
    try:
        test_my_dialog.close()
        test_my_dialog.deleteLater()
    except:
        pass
        
    test_my_dialog = testDialog()
    test_my_dialog.show()
    
        