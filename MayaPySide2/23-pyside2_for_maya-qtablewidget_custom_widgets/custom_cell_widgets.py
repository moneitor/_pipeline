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
        self.setMinimumWidth(340)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

        self.refresh_table()

    def create_widgets(self):
        self.table_wdg = QtWidgets.QTableWidget()
        self.table_wdg.setColumnCount(3)
        self.table_wdg.setHorizontalHeaderLabels(["QPushButton", "QSpinBox", "QComboBox"])

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
        main_layout.addWidget(self.table_wdg)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.refresh_btn.clicked.connect(self.refresh_table)
        self.close_btn.clicked.connect(self.close)

    def refresh_table(self):
        self.table_wdg.setRowCount(0)
        self.table_wdg.insertRow(0)

        btn = QtWidgets.QPushButton("Button")
        btn.clicked.connect(self.on_button_pressed)
        self.table_wdg.setCellWidget(0, 0, btn)

        spin_box = QtWidgets.QSpinBox()
        spin_box.valueChanged.connect(self.on_value_changed)
        self.table_wdg.setCellWidget(0, 1, spin_box)

        combo_box = QtWidgets.QComboBox()
        combo_box.addItems(["Item 01", "Item 02", "Item 03"])
        combo_box.currentTextChanged.connect(self.on_current_text_changed)
        self.table_wdg.setCellWidget(0, 2, combo_box)

    def on_button_pressed(self):
        print("Button was pressed")

    def on_value_changed(self, value):
        print("SpinBox value changed: {0}".format(value))

    def on_current_text_changed(self, text):
        print("ComboBox text changed: {0}".format(text))



if __name__ == "__main__":

    try:
        table_example_dialog.close() # pylint: disable=E0601
        table_example_dialog.deleteLater()
    except:
        pass

    table_example_dialog = TableExampleDialog()
    table_example_dialog.show()
