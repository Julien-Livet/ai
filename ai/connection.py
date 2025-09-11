from neuron import Neuron

class Connection:
    def __init__(self, inputs, neuron: Neuron):
        self.inputs = inputs
        self.neuron = neuron
