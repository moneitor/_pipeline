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


class MultiSelectDialog(QtWidgets.QDialog):

    def __init__(self, parent=maya_main_window()):
        super(MultiSelectDialog, self).__init__(parent)

        self.setWindowTitle("Multi-Select")
        self.setFixedWidth(220)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.list_wdg = QtWidgets.QListWidget()
        self.list_wdg.addItems(["Item 01", "Item 02", "Item 03", "Item 04", "Item 05", "Item 06"])

        self.close_btn = QtWidgets.QPushButton("Close")

    def create_layout(self):

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.close_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)
        main_layout.setSpacing(2)
        main_layout.addWidget(self.list_wdg)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.list_wdg.itemSelectionChanged.connect(self.print_selected_item)

        self.close_btn.clicked.connect(self.close)

    def print_selected_item(self):
        items = self.list_wdg.selectedItems()

        selected_item_labels = []
        for item in items:
            selected_item_labels.append(item.text())

        print("Selected Items: {0}".format(selected_item_labels))


if __name__ == "__main__":

    try:
        multi_select_dialog.close() # pylint: disable=E0601
        multi_select_dialog.deleteLater()
    except:
        pass

    multi_select_dialog = MultiSelectDialog()
    multi_select_dialog.show()
