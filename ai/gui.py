from brain import Brain
from connection import Connection
from neuron import Neuron
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

        self.inputTypesLabel = QtWidgets.QLabel("Input types:")
        self.inputTypesLineEdit = QtWidgets.QLineEdit()
        self.inputTypesLineEdit.setReadOnly(True)
        self.outputTypeLabel = QtWidgets.QLabel("Output type:")
        self.outputTypeLineEdit = QtWidgets.QLineEdit()
        self.outputTypeLineEdit.setReadOnly(True)
        self.neuronLabel = QtWidgets.QLabel("Neuron:")
        self.sortByLabel = QtWidgets.QLabel("Sort by:")
        self.sortByComboBox = QtWidgets.QComboBox()
        self.sortByComboBox.addItems(["name", "weight", "timestamp"])
        self.sortByComboBox.currentTextChanged.connect(self.sortByChanged)
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
        self.neuronsComboBox.addItems(self.neuronItems())
        self.neuronsComboBox.setFixedWidth(500)

        self.neuronLayout = QtWidgets.QHBoxLayout()
        self.neuronLayout.addWidget(self.neuronLabel)
        self.neuronLayout.addWidget(self.neuronsComboBox)
        self.neuronLayout.addWidget(self.sortByLabel)
        self.neuronLayout.addWidget(self.sortByComboBox)
        self.neuronLayout.addWidget(self.neuronCheckBox)
        self.neuronLayout.addWidget(self.neuronWeightLabel)
        self.neuronLayout.addWidget(self.neuronTimestampDateTimeEdit)
        self.neuronLayout.addWidget(self.inputTypesLabel)
        self.neuronLayout.addWidget(self.inputTypesLineEdit)
        self.neuronLayout.addWidget(self.outputTypeLabel)
        self.neuronLayout.addWidget(self.outputTypeLineEdit)

        self.connectionTotalNumberLabel = QtWidgets.QLabel("Connection total number: " + str(len(self.brain.connections)))

        self.activateAllNeuronsPushButton = QtWidgets.QPushButton("Activate all neurons")
        self.deactivateAllNeuronsPushButton = QtWidgets.QPushButton("Deactivate all neurons")

        self.moduleLabel = QtWidgets.QLabel("Module:")
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

        self.updateHistogram()

        self.expressionLabel = QtWidgets.QLabel("Expression:")
        self.expressionLineEdit = QtWidgets.QLineEdit("x+y")
        self.activatePushButton = QtWidgets.QPushButton("Activate")
        self.deactivatePushButton = QtWidgets.QPushButton("Deactivate")
        self.depthSpinBox = QtWidgets.QSpinBox()
        self.depthLabel = QtWidgets.QLabel("Depth:")
        self.depthSpinBox.setValue(5)
        self.learnModuleLabel = QtWidgets.QLabel("Module:")
        self.moduleLineEdit = QtWidgets.QLineEdit()
        self.learnPushButton = QtWidgets.QPushButton("Learn")
        self.connectPushButton = QtWidgets.QPushButton("Connect")
        
        self.connectionLabel = QtWidgets.QLabel("Connection")
        self.connectionsComboBox = QtWidgets.QComboBox()
        self.connectionsComboBox.currentTextChanged.connect(self.connectionChanged)
        self.connectionsComboBox.clear()
        self.connectionsComboBox.addItems([str(i) for i in range(0, len(self.brain.connections))])
        self.connectionTreeWidget = QtWidgets.QTreeWidget()
        self.connectionTreeWidget.setHeaderLabels(["Connection"])
        self.connectionLayout = QtWidgets.QHBoxLayout()
        self.connectionLayout.addWidget(self.connectionLabel)
        self.connectionLayout.addWidget(self.connectionsComboBox)
        
        self.clearConnectionsPushButton = QtWidgets.QPushButton("Clear connections")
        self.associatePushButton = QtWidgets.QPushButton("Associate")

        self.learnLayout = QtWidgets.QHBoxLayout()
        self.learnLayout.addWidget(self.expressionLabel)
        self.learnLayout.addWidget(self.expressionLineEdit)
        self.learnLayout.addWidget(self.activatePushButton)
        self.learnLayout.addWidget(self.deactivatePushButton)
        self.learnLayout.addWidget(self.depthLabel)
        self.learnLayout.addWidget(self.depthSpinBox)
        self.learnLayout.addWidget(self.learnModuleLabel)
        self.learnLayout.addWidget(self.moduleLineEdit)
        self.learnLayout.addWidget(self.learnPushButton)
        self.learnLayout.addWidget(self.connectPushButton)
        self.learnLayout.addWidget(self.associatePushButton)

        self.outputLabel = QtWidgets.QLabel("Output:")
        self.outputLineEdit = QtWidgets.QLineEdit()
        self.outputLineEdit.setReadOnly(True)

        self.outputLayout = QtWidgets.QHBoxLayout()
        self.outputLayout.addWidget(self.outputLabel)
        self.outputLayout.addWidget(self.outputLineEdit)

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
        self.layout.addLayout(self.connectionLayout)
        self.layout.addWidget(self.connectionTreeWidget)
        self.layout.addWidget(self.clearConnectionsPushButton)
        self.layout.addLayout(self.outputLayout)

        self.loadPushButton.clicked.connect(self.load)
        self.savePushButton.clicked.connect(self.save)
        self.show2dPushButton.clicked.connect(self.show2d)
        self.show3dPushButton.clicked.connect(self.show3d)
        self.activateAllModulesPushButton.clicked.connect(self.activateAllModules)
        self.deactivateAllModulesPushButton.clicked.connect(self.deactivateAllModules)
        self.activateAllNeuronsPushButton.clicked.connect(self.activateAllNeurons)
        self.deactivateAllNeuronsPushButton.clicked.connect(self.deactivateAllNeurons)
        self.connectPushButton.clicked.connect(self.connect)
        self.clearConnectionsPushButton.clicked.connect(self.clearConnections)
        self.learnPushButton.clicked.connect(self.learn)
        self.associatePushButton.clicked.connect(self.associate)
        self.activatePushButton.clicked.connect(self.activate)
        self.deactivatePushButton.clicked.connect(self.deactivate)

    @QtCore.Slot()
    def load(self):
        fileName, selectedFilter = QtWidgets.QFileDialog.getOpenFileName(filter = "*.bin")

        if (os.path.exists(fileName)):
            self.fileName = fileName

            self.brain.load(fileName)

            self.neuronsComboBox.clear()
            self.neuronsComboBox.addItems(self.neuronItems())
            
            self.connectionsComboBox.clear()
            self.connectionsComboBox.addItems([str(i) for i in range(0, len(self.brain.connections))])

            self.modulesComboBox.clear()
            self.modulesComboBox.addItems(sorted([x for x in self.brain.modules]))

            self.neuronTotalNumberLabel.setText("Neuron total number: " + str(len(self.brain.neurons)))
            self.connectionTotalNumberLabel.setText("Connection total number: " + str(len(self.brain.connections)))

            self.updateHistogram()

    def neuronIdFromName(self, name: str):
        for id, n in self.brain.neurons.items():
            if (self.brain.neuron_name(n) == name):
                return id

        return None

    @QtCore.Slot()
    def save(self):
        fileName, selectedFilter = QtWidgets.QFileDialog.getSaveFileName(dir = self.fileName, filter = "*.bin")

        self.brain.save(fileName)

        self.fileName = fileName

    @QtCore.Slot()
    def show2d(self):
        self.brain.show2d(seed = 0, colorBy = self.colorByComboBox.currentText(), title = self.fileName)

    @QtCore.Slot()
    def show3d(self):
        self.brain.show3d(seed = 0, colorBy = self.colorByComboBox.currentText(), title = self.fileName)

    @QtCore.Slot()
    def neuronChanged(self, text: str):
        if (len(text) == 0):
            return

        neuron = self.brain.neurons[self.neuronIdFromName(text)]

        self.neuronCheckBox.setChecked(neuron.activated)
        self.neuronWeightLabel.setValue(neuron.weight)

        dateTime = QtCore.QDateTime()
        dateTime.setMSecsSinceEpoch(int(neuron.datetime.timestamp()))

        self.neuronTimestampDateTimeEdit.setDateTime(dateTime)
        self.inputTypesLineEdit.setText(str(neuron.inputTypes))
        self.outputTypeLineEdit.setText(str(neuron.outputType))

    @QtCore.Slot()
    def moduleChanged(self, text: str):
        if (len(text) == 0):
            return

        self.moduleCheckBox.setChecked(self.brain.modules[text])

    def addItems(self, parent, connection: Connection):
        connectionItem = QtWidgets.QTreeWidgetItem(["connection"])
        
        if (parent == None):
            self.connectionTreeWidget.addTopLevelItem(connectionItem)
        else:
            parent.addChild(connectionItem)
        
        item = QtWidgets.QTreeWidgetItem(["inputs"])
        connectionItem.addChild(item)
        
        for input in connection.inputs:
            if (isinstance(input, Connection)):
                self.addItems(item, input)
            elif (isinstance(input, Neuron)):
                it = QtWidgets.QTreeWidgetItem([self.brain.neuron_name(input)])
                item.addChild(it)
            else:
                it = QtWidgets.QTreeWidgetItem([str(input)])
                item.addChild(it)

        item = QtWidgets.QTreeWidgetItem([self.brain.neuron_name(self.brain.neurons[connection.neuronId])])
        connectionItem.addChild(item)

    @QtCore.Slot()
    def connectionChanged(self, text: str):
        if (len(text) == 0):
            self.connectionTreeWidget.clear()
            
            return

        self.addItems(None, list(self.brain.connections)[int(text)])
        
        self.connectionTreeWidget.expandAll()

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
        self.updateHistogram()

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
        answers = self.brain.learn(self.expressionLineEdit.text(), depth = self.depthSpinBox.value(), module = module)

        if (len(answers)):
            if (isinstance(answers[0], Connection)):
                self.outputLineEdit.setText(brain.connection_str(answers[0]), "->", self.brain.connection_output(answers[0]))
            else:
                self.outputLineEdit.setText(self.brain.neuron_name(answers[0]), "->", answers[0].output())

        self.neuronTotalNumberLabel.setText("Neuron total number: " + str(len(self.brain.neurons)))
        self.connectionTotalNumberLabel.setText("Connection total number: " + str(len(self.brain.connections)))

        self.neuronsComboBox.clear()
        self.neuronsComboBox.addItems(self.neuronItems())
        
        self.connectionsComboBox.clear()
        self.connectionsComboBox.addItems([str(i) for i in range(0, len(self.brain.connections))])

        self.modulesComboBox.clear()
        self.modulesComboBox.addItems(sorted([x for x in self.brain.modules]))

        self.updateHistogram()

    @QtCore.Slot()
    def connect(self):
        self.brain.connect(self.depthSpinBox.value())

        self.connectionTotalNumberLabel.setText("Connection total number: " + str(len(self.brain.connections)))
        
        self.connectionsComboBox.clear()
        self.connectionsComboBox.addItems([str(i) for i in range(0, len(self.brain.connections))])

    @QtCore.Slot()
    def clearConnections(self):
        self.brain.clear_connections()

        self.connectionTotalNumberLabel.setText("Connection total number: " + str(len(self.brain.connections)))
        
        self.connectionsComboBox.clear()
        self.connectionsComboBox.addItems([str(i) for i in range(0, len(self.brain.connections))])

    @QtCore.Slot()
    def associate(self):
        module = None

        if (len(self.moduleLineEdit.text())):
            module = self.moduleLineEdit.text()

        self.brain.associate(self.expressionLineEdit.text(), module = module)

        self.neuronTotalNumberLabel.setText("Neuron total number: " + str(len(self.brain.neurons)))

        self.neuronsComboBox.clear()
        self.neuronsComboBox.addItems(self.neuronItems())

        self.modulesComboBox.clear()
        self.modulesComboBox.addItems(sorted([x for x in self.brain.modules]))

        self.updateHistogram()

    def updateHistogram(self):
        y, x = np.histogram([n.weight for id, n in self.brain.neurons.items()])
        x = x[:-1]

        self.bar_graph = pg.BarGraphItem(x = x, height = y, width = (x[1] - x[0]), brush = 'b')
        self.plot_widget.clear()
        self.plot_widget.addItem(self.bar_graph)

    @QtCore.Slot()
    def activate(self):
        self.brain.activate_str(self.expressionLineEdit.text())
        self.neuronChanged(self.neuronsComboBox.currentText())

    @QtCore.Slot()
    def deactivate(self):
        self.brain.deactivate_str(self.expressionLineEdit.text())
        self.neuronChanged(self.neuronsComboBox.currentText())

    @QtCore.Slot()
    def sortByChanged(self, text: str):
        self.neuronsComboBox.clear()
        self.neuronsComboBox.addItems(self.neuronItems())

    def neuronItems(self):
        if (self.sortByComboBox.currentText() == "name"):
            return sorted([self.brain.neuron_name(n) for id, n in self.brain.neurons.items()])
        elif (self.sortByComboBox.currentText() == "weight"):
            l = ([(self.brain.neuron_name(n), n.weight) for id, n in self.brain.neurons.items()])

            return [x[0] for x in sorted(l, key = lambda x: x[1])]
        elif (self.sortByComboBox.currentText() == "timestamp"):
            l = ([(self.brain.neuron_name(n), n.datetime) for id, n in self.brain.neurons.items()])

            return [x[0] for x in sorted(l, key = lambda x: x[1])]

if (__name__ == "__main__"):
    app = QtWidgets.QApplication([])

    widget = Window()
    widget.showMaximized()

    sys.exit(app.exec())
