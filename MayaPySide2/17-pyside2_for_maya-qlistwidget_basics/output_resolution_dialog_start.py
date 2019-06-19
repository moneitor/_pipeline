from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMaya as om
import maya.OpenMayaUI as omui
import maya.cmds as cmds


def maya_main_window():
    """
    Return the Maya main window widget as a Python object
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class OutputResolutionDialog(QtWidgets.QDialog):

    def __init__(self, parent=maya_main_window()):
        super(OutputResolutionDialog, self).__init__(parent)

        self.setWindowTitle("Output Resolution")
        self.setFixedWidth(220)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.close_btn = QtWidgets.QPushButton("Close")

    def create_layout(self):

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.close_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.close_btn.clicked.connect(self.close)


if __name__ == "__main__":

    try:
        output_resolution_dialog.close() # pylint: disable=E0601
        output_resolution_dialog.deleteLater()
    except:
        pass

    output_resolution_dialog = OutputResolutionDialog()
    output_resolution_dialog.show()
