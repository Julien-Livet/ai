from neuron import Neuron

class Connection:
    def __init__(self, inputs, neuron: Neuron):
        self.inputs = inputs
        self.neuron = neuron

    def origin_input_types(self):
        types = []

        for input in self.inputs:
            if (isinstance(input, Neuron) and len(input.inputTypes) == 0):
                types.append(input.outputType)
            elif (isinstance(input, Connection)):
                types.extend(input.origin_input_types())

        return types
