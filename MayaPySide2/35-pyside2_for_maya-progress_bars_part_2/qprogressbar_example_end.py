import time

from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.cmds as cmds
import maya.OpenMayaUI as omui


def maya_main_window():
    """
    Return the Maya main window widget as a Python object
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class ProgressTestDialog(QtWidgets.QDialog):

    WINDOW_TITLE = "Progress Test"

    def __init__(self, parent=maya_main_window()):
        super(ProgressTestDialog, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        if cmds.about(ntOS=True):
            self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        elif cmds.about(macOS=True):
            self.setWindowFlags(QtCore.Qt.Tool)

        self.setMinimumSize(300, 100)

        self.test_in_progress = False

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.progress_bar_label = QtWidgets.QLabel("Operation Progress")
        self.progress_bar = QtWidgets.QProgressBar()

        self.progress_bar_button = QtWidgets.QPushButton("Do It!")
        self.cancel_button = QtWidgets.QPushButton("Cancel")

        self.update_visibility()

    def create_layout(self):
        progress_layout = QtWidgets.QVBoxLayout()
        progress_layout.addWidget(self.progress_bar_label)
        progress_layout.addWidget(self.progress_bar)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.progress_bar_button)
        button_layout.addWidget(self.cancel_button)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)
        main_layout.addLayout(progress_layout)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.progress_bar_button.clicked.connect(self.run_progress_test)
        self.cancel_button.clicked.connect(self.cancel_progress_test)

    def update_visibility(self):
        self.progress_bar_label.setVisible(self.test_in_progress)
        self.progress_bar.setVisible(self.test_in_progress)

        self.cancel_button.setVisible(self.test_in_progress)
        self.progress_bar_button.setHidden(self.test_in_progress)

    def run_progress_test(self):
        if self.test_in_progress:
            return

        number_of_operation = 10

        self.progress_bar.setRange(0, number_of_operation)
        self.progress_bar.setValue(0)
        self.progress_bar_label.setText("Operation Progress")

        self.test_in_progress = True
        self.update_visibility()

        for i in range(1, number_of_operation + 1):
            if not self.test_in_progress:
                break

            self.progress_bar_label.setText("Processing operation: {0} (of {1})".format(i, number_of_operation))
            self.progress_bar.setValue(i)
            time.sleep(0.5)

            QtCore.QCoreApplication.processEvents()

        self.test_in_progress = False
        self.update_visibility()

    def cancel_progress_test(self):
        self.test_in_progress = False


if __name__ == "__main__":

    try:
        test_dialog.close() # pylint: disable=E0601
        test_dialog.deleteLater()
    except:
        pass

    test_dialog = ProgressTestDialog()
    test_dialog.show()
