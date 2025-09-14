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

        self.neuronCheckBox = QtWidgets.QCheckBox("Activated")
        self.neuronCheckBox.checkStateChanged.connect(self.neuronCheckStateChanged)
        self.neuronsComboBox = QtWidgets.QComboBox()
        self.neuronsComboBox.currentTextChanged.connect(self.neuronChanged)
        self.neuronsComboBox.clear()
        self.neuronsComboBox.addItems(sorted([self.brain.neuron_name(n) for id, n in self.brain.neurons.items()]))

        self.neuronLayout = QtWidgets.QHBoxLayout()
        self.neuronLayout.addWidget(self.neuronsComboBox)
        self.neuronLayout.addWidget(self.neuronCheckBox)

        self.activateAllNeuronsPushButton = QtWidgets.QPushButton("Activate all neurons")
        self.deactivateAllNeuronsPushButton = QtWidgets.QPushButton("Deactivate all neurons")

        self.moduleCheckBox = QtWidgets.QCheckBox("Activated")
        self.moduleCheckBox.checkStateChanged.connect(self.moduleCheckStateChanged)
        self.modulesComboBox = QtWidgets.QComboBox()
        self.modulesComboBox.currentTextChanged.connect(self.moduleChanged)
        self.modulesComboBox.clear()
        self.modulesComboBox.addItems(sorted([x for x in self.brain.modules]))

        self.moduleLayout = QtWidgets.QHBoxLayout()
        self.moduleLayout.addWidget(self.modulesComboBox)
        self.moduleLayout.addWidget(self.moduleCheckBox)

        self.activateAllModulesPushButton = QtWidgets.QPushButton("Activate all modules")
        self.deactivateAllModulesPushButton = QtWidgets.QPushButton("Deactivate all modules")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.loadPushButton)
        self.layout.addWidget(self.savePushButton)
        self.layout.addWidget(self.colorByComboBox)
        self.layout.addLayout(self.neuronLayout)
        self.layout.addWidget(self.activateAllNeuronsPushButton)
        self.layout.addWidget(self.deactivateAllNeuronsPushButton)
        self.layout.addLayout(self.moduleLayout)
        self.layout.addWidget(self.activateAllModulesPushButton)
        self.layout.addWidget(self.deactivateAllModulesPushButton)
        self.layout.addWidget(self.show2dPushButton)
        self.layout.addWidget(self.show3dPushButton)

        self.loadPushButton.clicked.connect(self.load)
        self.savePushButton.clicked.connect(self.save)
        self.show2dPushButton.clicked.connect(self.show2d)
        self.show3dPushButton.clicked.connect(self.show3d)
        self.activateAllModulesPushButton.clicked.connect(self.activateAllModules)
        self.deactivateAllModulesPushButton.clicked.connect(self.deactivateAllModules)
        self.activateAllNeuronsPushButton.clicked.connect(self.activateAllNeurons)
        self.deactivateAllNeuronsPushButton.clicked.connect(self.deactivateAllNeurons)

    @QtCore.Slot()
    def load(self):
        fileName, selectedFilter = QtWidgets.QFileDialog.getOpenFileName(filter = "*.bin")

        if (os.path.exists(fileName)):
            self.brain.load(fileName)

            self.neuronsComboBox.clear()
            self.neuronsComboBox.addItems(sorted([self.brain.neuron_name(n) for id, n in self.brain.neurons.items()]))

            self.modulesComboBox.clear()
            self.modulesComboBox.addItems(sorted([x for x in self.brain.modules]))

    def neuronIdFromName(self, name: str):
        for id, n in self.brain.neurons.items():
            if (self.brain.neuron_name(n) == name):
                return id
        
        return None

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

    @QtCore.Slot()
    def neuronChanged(self, text: str):
        self.neuronCheckBox.setChecked(self.brain.neurons[self.neuronIdFromName(text)].activated)

    @QtCore.Slot()
    def moduleChanged(self, text: str):
        self.moduleCheckBox.setChecked(self.brain.modules[text])

    @QtCore.Slot()
    def neuronCheckStateChanged(self, state: QtCore.Qt.CheckState):
        if (state == QtCore.Qt.Unchecked):
            self.brain.deactivate_neuron(self.neuronIdFromName(self.neuronsComboBox.currentText()))
        elif (state == QtCore.Qt.Checked):
            self.brain.activate_neuron(self.neuronIdFromName(self.neuronsComboBox.currentText()))

    @QtCore.Slot()
    def moduleCheckStateChanged(self, state: QtCore.Qt.CheckState):
        if (state == QtCore.Qt.Unchecked):
            self.brain.deactivate_module(self.modulesComboBox.currentText())
        elif (state == QtCore.Qt.Checked):
            self.brain.activate_module(self.modulesComboBox.currentText())

        self.neuronChanged(self.neuronsComboBox.currentText())

    @QtCore.Slot()
    def activateAllNeurons(self):
        self.brain.activate_all_neurons()
        self.neuronCheckBox.setChecked(True)

    @QtCore.Slot()
    def deactivateAllNeurons(self):
        self.brain.deactivate_all_neurons()
        self.neuronCheckBox.setChecked(False)

    @QtCore.Slot()
    def activateAllModules(self):
        self.brain.activate_all_modules()
        self.moduleCheckBox.setChecked(True)
        self.neuronChanged(self.neuronsComboBox.currentText())

    @QtCore.Slot()
    def deactivateAllModules(self):
        self.brain.deactivate_all_modules()
        self.moduleCheckBox.setChecked(False)
        self.neuronChanged(self.neuronsComboBox.currentText())

if (__name__ == "__main__"):
    app = QtWidgets.QApplication([])

    widget = Window()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
