from Qt import __binding__

if __binding__ == "PySide2":
    print("Using PySide2")
elif __binding__ == "PySide":
    print("Using PySide")
