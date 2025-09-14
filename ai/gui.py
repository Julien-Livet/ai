from brain import Brain
import os
from PySide6 import QtCore, QtWidgets, QtGui
import sys

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Brain GUI")

        self.brain = Brain()
        self.fileName = ""

        self.loadPushButton = QtWidgets.QPushButton("Load")
        self.savePushButton = QtWidgets.QPushButton("Save")
        self.colorByComboBox = QtWidgets.QComboBox()
        self.colorByComboBox.addItems(["level", "weight", "module", "timestamp"])
        self.show2dPushButton = QtWidgets.QPushButton("Show 2D")
        self.show3dPushButton = QtWidgets.QPushButton("Show 3D")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.loadPushButton)
        self.layout.addWidget(self.savePushButton)
        self.layout.addWidget(self.colorByComboBox)
        self.layout.addWidget(self.show2dPushButton)
        self.layout.addWidget(self.show3dPushButton)

        self.loadPushButton.clicked.connect(self.load)
        self.savePushButton.clicked.connect(self.save)
        self.show2dPushButton.clicked.connect(self.show2d)
        self.show3dPushButton.clicked.connect(self.show3d)

    @QtCore.Slot()
    def load(self):
        fileName, selectedFilter = QtWidgets.QFileDialog.getOpenFileName(filter = "*.bin")

        if (os.path.exists(fileName)):
            self.brain.load(fileName)

    @QtCore.Slot()
    def save(self):
        fileName, selectedFilter = QtWidgets.QFileDialog.getSaveFileName(dir = self.fileName, filter = "*.bin")

        self.brain.save(fileName)

    @QtCore.Slot()
    def show2d(self):
        self.brain.show2d(seed = 0, colorBy = self.colorByComboBox.currentText(), title = self.fileName)

    @QtCore.Slot()
    def show3d(self):
        self.brain.show3d(seed = 0, colorBy = self.colorByComboBox.currentText(), title = self.fileName)

if (__name__ == "__main__"):
    app = QtWidgets.QApplication([])

    widget = Window()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
