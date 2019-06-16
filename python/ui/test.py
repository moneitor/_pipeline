from PySide2 import QtCore, QtGui, QtWidgets


def showdialog():
    d = QtWidgets.QDialog()
    b1 = QtWidgets.QPushButton("ok", d)
    b1.move(50, 50)
    #centralwidget.setObjectName("centralwidget")
    d.setWindowTitle("Dialog")
    d.setWindowModality(QtCore.Qt.ApplicationModal)
    d.exec_()