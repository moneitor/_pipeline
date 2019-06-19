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


class SpinBoxDialog(QtWidgets.QDialog):

    def __init__(self, parent=maya_main_window()):
        super(SpinBoxDialog, self).__init__(parent)

        self.setWindowTitle("Spin Box Dialog")
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.spin_box = QtWidgets.QSpinBox()
        self.spin_box.setFixedWidth(80)
        self.spin_box.setMinimum(-100)
        self.spin_box.setMaximum(100)
        self.spin_box.setSingleStep(5)
        self.spin_box.setPrefix("$ ")
        self.spin_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)

        self.double_spin_box = QtWidgets.QDoubleSpinBox()
        self.double_spin_box.setFixedWidth(80)
        self.double_spin_box.setRange(-50.0, 50.0)
        self.double_spin_box.setSuffix(" m")

    def create_layout(self):
        main_layout = QtWidgets.QFormLayout(self)
        main_layout.addRow("Spin Box:", self.spin_box)
        main_layout.addRow("Double Spin Box:", self.double_spin_box)

    def create_connections(self):
        self.spin_box.valueChanged.connect(self.print_value)
        self.double_spin_box.valueChanged.connect(self.print_value)

    def print_value(self, value):
        print("Value: {0}".format(value))


if __name__ == "__main__":

    try:
        spin_box_dialog.close() # pylint: disable=E0601
        spin_box_dialog.deleteLater()
    except:
        pass

    spin_box_dialog = SpinBoxDialog()
    spin_box_dialog.show()
