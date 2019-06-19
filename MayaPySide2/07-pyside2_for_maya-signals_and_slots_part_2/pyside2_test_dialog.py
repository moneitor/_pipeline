from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui


def maya_main_window():
    """
    Return the Maya main window widget as a Python object
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class TestDialog(QtWidgets.QDialog):

    def __init__(self, parent=maya_main_window()):
        super(TestDialog, self).__init__(parent)

        self.setWindowTitle("Test Dialog")
        self.setMinimumWidth(200)
        self.setMinimumHeight(150)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widgets()
        self.create_layouts()
        self.create_connections()

    def create_widgets(self):
        self.combobox = QtWidgets.QComboBox()
        self.combobox.addItems(["ComboBoxItem 1", "ComboBoxItem 2", "ComboBoxItem 3", "ComboBoxItem 4"])

        self.ok_btn = QtWidgets.QPushButton("OK")
        self.cancel_btn = QtWidgets.QPushButton("Cancel")


    def create_layouts(self):
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow("ComboBox:", self.combobox)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.ok_btn)
        button_layout.addWidget(self.cancel_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.combobox.activated.connect(self.on_activated_int)
        self.combobox.activated[str].connect(self.on_activated_str) # pylint: disable=E1136

        self.cancel_btn.clicked.connect(self.close)

    @QtCore.Slot(int)
    def on_activated_int(self, index):
        print("ComboBox Index: {0}".format(index))

    @QtCore.Slot(str)
    def on_activated_str(self, text):
        print("ComboBox Text: {0}".format(text))


if __name__ == "__main__":

    try:
        test_dialog.close() # pylint: disable=E0601
        test_dialog.deleteLater()
    except:
        pass

    test_dialog = TestDialog()
    test_dialog.show()
