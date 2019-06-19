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


class TableExampleDialog(QtWidgets.QDialog):

    def __init__(self, parent=maya_main_window()):
        super(TableExampleDialog, self).__init__(parent)

        self.setWindowTitle("Table Example")
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setMinimumWidth(500)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.refresh_btn = QtWidgets.QPushButton("Refresh")
        self.close_btn = QtWidgets.QPushButton("Close")

    def create_layout(self):
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setSpacing(2)
        button_layout.addStretch()
        button_layout.addWidget(self.refresh_btn)
        button_layout.addWidget(self.close_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)
        main_layout.setSpacing(2)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.refresh_btn.clicked.connect(self.refresh_table)
        self.close_btn.clicked.connect(self.close)

    def refresh_table(self):
        print("TODO: refresh_table()")


if __name__ == "__main__":

    try:
        table_example_dialog.close() # pylint: disable=E0601
        table_example_dialog.deleteLater()
    except:
        pass

    table_example_dialog = TableExampleDialog()
    table_example_dialog.show()
