# import sys
# import random
# from PySide6 import QtCore, QtWidgets, QtGui


# class MyWidget(QtWidgets.QWidget):
#     def __init__(self, w, h):
#         super().__init__()

#         self.setWindowTitle("Tesla Information")

#         # self.hello = ["Hallo Welt", "Hei maailma",
#         #               "Hola Mundo", "Привет мир"]

#         # self.button = QtWidgets.QPushButton("Click me!")
#         # self.text = QtWidgets.QLabel("Hello World",
#         #                              alignment=QtCore.Qt.AlignCenter)

#         # self.layout = QtWidgets.QVBoxLayout(self)
#         # self.layout.addWidget(self.text)
#         # self.layout.addWidget(self.button)

#         # self.button.clicked.connect(self.magic)
#         self.resize(w, h)

#         self.layout = QtWidgets.QVBoxLayout(self)

#         # 　Widget: bottomMenuBar

#     @QtCore.Slot()
#     def magic(self):
#         self.text.setText(random.choice(self.hello))


# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])

#     widget = MyWidget(1280, 720)
#     widget.show()

#     sys.exit(app.exec())

from PySide6 import QtCore, QtWidgets, QtGui, QtQml
from Controllers.system import System
import sys
import os

if __name__ == "__main__":
    os.environ["QT_QUICK_BACKEND"] = "software"
    app = QtWidgets.QApplication(sys.argv)
    # View = QtCore.QtQuickView()
    # Context = View.rootContext()
    # systemHandler = System()
    # Context.setContextProperty("systemHandler", systemHandler)
    # View.setSource(Qt)
    engine = QtQml.QQmlApplicationEngine()

    engine.load("./tesla_ui/main.qml")

    systemHandler = System(True, 54, "lich")
    # systemHandler = System()
    engine.rootContext().setContextProperty("systemHandler", systemHandler)

    app.exec()

    # sys.exit(app.exec())
