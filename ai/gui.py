from brain import Brain
import numpy as np
import os
import pyqtgraph as pg
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

        self.colorByLabel = QtWidgets.QLabel("Color by:")
        self.colorByComboBox = QtWidgets.QComboBox()
        self.colorByComboBox.addItems(["level", "weight", "module", "timestamp"])

        self.colorByLayout = QtWidgets.QHBoxLayout()
        self.colorByLayout.addWidget(self.colorByLabel)
        self.colorByLayout.addWidget(self.colorByComboBox)

        self.show2dPushButton = QtWidgets.QPushButton("Show 2D")
        self.show3dPushButton = QtWidgets.QPushButton("Show 3D")

        self.neuronTotalNumberLabel = QtWidgets.QLabel("Neuron total number: " + str(len(self.brain.neurons)))

        self.neuronLabel = QtWidgets.QLabel("Neuron :")
        self.neuronCheckBox = QtWidgets.QCheckBox("Activated")
        self.neuronCheckBox.checkStateChanged.connect(self.neuronCheckStateChanged)
        self.neuronTimestampDateTimeEdit = QtWidgets.QDateTimeEdit()
        self.neuronTimestampDateTimeEdit.setDisplayFormat("dd/MM/yyyy hh:ss:mm:zzz")
        self.neuronTimestampDateTimeEdit.setDisabled(True)
        self.neuronWeightLabel = QtWidgets.QDoubleSpinBox()
        self.neuronWeightLabel.valueChanged.connect(self.neuronWeightChanged)
        self.neuronsComboBox = QtWidgets.QComboBox()
        self.neuronsComboBox.currentTextChanged.connect(self.neuronChanged)
        self.neuronsComboBox.clear()
        self.neuronsComboBox.addItems(sorted([self.brain.neuron_name(n) for id, n in self.brain.neurons.items()]))

        self.neuronLayout = QtWidgets.QHBoxLayout()
        self.neuronLayout.addWidget(self.neuronLabel)
        self.neuronLayout.addWidget(self.neuronsComboBox)
        self.neuronLayout.addWidget(self.neuronCheckBox)
        self.neuronLayout.addWidget(self.neuronWeightLabel)
        self.neuronLayout.addWidget(self.neuronTimestampDateTimeEdit)

        self.connectionTotalNumberLabel = QtWidgets.QLabel("Connection total number: " + str(len(self.brain.connections)))

        self.activateAllNeuronsPushButton = QtWidgets.QPushButton("Activate all neurons")
        self.deactivateAllNeuronsPushButton = QtWidgets.QPushButton("Deactivate all neurons")

        self.moduleLabel = QtWidgets.QLabel("Module :")
        self.moduleCheckBox = QtWidgets.QCheckBox("Activated")
        self.moduleCheckBox.checkStateChanged.connect(self.moduleCheckStateChanged)
        self.modulesComboBox = QtWidgets.QComboBox()
        self.modulesComboBox.currentTextChanged.connect(self.moduleChanged)
        self.modulesComboBox.clear()
        self.modulesComboBox.addItems(sorted([x for x in self.brain.modules]))

        self.moduleLayout = QtWidgets.QHBoxLayout()
        self.moduleLayout.addWidget(self.moduleLabel)
        self.moduleLayout.addWidget(self.modulesComboBox)
        self.moduleLayout.addWidget(self.moduleCheckBox)

        self.activateAllModulesPushButton = QtWidgets.QPushButton("Activate all modules")
        self.deactivateAllModulesPushButton = QtWidgets.QPushButton("Deactivate all modules")

        self.plot_widget = pg.PlotWidget()

        y, x = np.histogram([n.weight for id, n in self.brain.neurons.items()])
        x = x[:-1]

        self.bar_graph = pg.BarGraphItem(x = x, height = y, width = (x[1] - x[0]), brush = 'b')
        self.plot_widget.clear()
        self.plot_widget.addItem(self.bar_graph)

        self.expressionLabel = QtWidgets.QLabel("Expression:")
        self.learnPushButton = QtWidgets.QPushButton("Learn")
        self.expressionLineEdit = QtWidgets.QLineEdit("x+y")
        self.depthSpinBox = QtWidgets.QSpinBox()
        self.depthSpinBox.setValue(5)
        self.moduleLineEdit = QtWidgets.QLineEdit()

        self.learnLayout = QtWidgets.QHBoxLayout()
        self.learnLayout.addWidget(self.expressionLabel)
        self.learnLayout.addWidget(self.expressionLineEdit)
        self.learnLayout.addWidget(self.depthSpinBox)
        self.learnLayout.addWidget(self.moduleLineEdit)
        self.learnLayout.addWidget(self.learnPushButton)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.loadPushButton)
        self.layout.addWidget(self.savePushButton)
        self.layout.addLayout(self.colorByLayout)
        self.layout.addWidget(self.neuronTotalNumberLabel)
        self.layout.addLayout(self.neuronLayout)
        self.layout.addWidget(self.connectionTotalNumberLabel)
        self.layout.addWidget(self.activateAllNeuronsPushButton)
        self.layout.addWidget(self.deactivateAllNeuronsPushButton)
        self.layout.addLayout(self.moduleLayout)
        self.layout.addWidget(self.activateAllModulesPushButton)
        self.layout.addWidget(self.deactivateAllModulesPushButton)
        self.layout.addWidget(self.show2dPushButton)
        self.layout.addWidget(self.show3dPushButton)
        self.layout.addWidget(self.plot_widget)
        self.layout.addLayout(self.learnLayout)

        self.loadPushButton.clicked.connect(self.load)
        self.savePushButton.clicked.connect(self.save)
        self.show2dPushButton.clicked.connect(self.show2d)
        self.show3dPushButton.clicked.connect(self.show3d)
        self.activateAllModulesPushButton.clicked.connect(self.activateAllModules)
        self.deactivateAllModulesPushButton.clicked.connect(self.deactivateAllModules)
        self.activateAllNeuronsPushButton.clicked.connect(self.activateAllNeurons)
        self.deactivateAllNeuronsPushButton.clicked.connect(self.deactivateAllNeurons)
        self.learnPushButton.clicked.connect(self.learn)

    @QtCore.Slot()
    def load(self):
        fileName, selectedFilter = QtWidgets.QFileDialog.getOpenFileName(filter = "*.bin")

        if (os.path.exists(fileName)):
            self.brain.load(fileName)

            self.neuronsComboBox.clear()
            self.neuronsComboBox.addItems(sorted([self.brain.neuron_name(n) for id, n in self.brain.neurons.items()]))

            self.modulesComboBox.clear()
            self.modulesComboBox.addItems(sorted([x for x in self.brain.modules]))

            self.neuronTotalNumberLabel.setText("Neuron total number: " + str(len(self.brain.neurons)))
            self.connectionTotalNumberLabel.setText("Connection total number: " + str(len(self.brain.connections)))

            y, x = np.histogram([n.weight for id, n in self.brain.neurons.items()])
            x = x[:-1]

            self.bar_graph = pg.BarGraphItem(x = x, height = y, width = (x[1] - x[0]), brush = 'b')
            self.plot_widget.clear()
            self.plot_widget.addItem(self.bar_graph)

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
        self.neuronWeightLabel.setValue(self.brain.neurons[self.neuronIdFromName(text)].weight)

        dateTime = QtCore.QDateTime()
        dateTime.setMSecsSinceEpoch(int(self.brain.neurons[self.neuronIdFromName(text)].datetime.timestamp()))

        self.neuronTimestampDateTimeEdit.setDateTime(dateTime)

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

    @QtCore.Slot()
    def neuronWeightChanged(self, value: float):
        self.brain.neurons[self.neuronIdFromName(self.neuronsComboBox.currentText())].weight = value

    @QtCore.Slot()
    def learn(self):
        self.brain.clear_connections()
        self.brain.deactivate_all_modules()

        for module in self.brain.modules:
            if (not "constants" in module):
                self.brain.activate_module(module)

        module = None
        
        if (len(self.moduleLineEdit.text())):
            module = self.moduleLineEdit.text()

        self.brain.activate_str(self.expressionLineEdit.text())
        self.brain.learn(self.expressionLineEdit.text(), depth = self.depthSpinBox.value(), module = module)

        self.neuronTotalNumberLabel.setText("Neuron total number: " + str(len(self.brain.neurons)))
        self.connectionTotalNumberLabel.setText("Connection total number: " + str(len(self.brain.connections)))
        
        self.neuronsComboBox.clear()
        self.neuronsComboBox.addItems(sorted([self.brain.neuron_name(n) for id, n in self.brain.neurons.items()]))

        self.modulesComboBox.clear()
        self.modulesComboBox.addItems(sorted([x for x in self.brain.modules]))

if (__name__ == "__main__"):
    app = QtWidgets.QApplication([])

    widget = Window()
    widget.setFixedWidth(1000)
    widget.show()

    sys.exit(app.exec())
