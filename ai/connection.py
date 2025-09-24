import datetime
import math
from neuron import Neuron

class Connection:
    def __init__(self, inputs, neuronId: id, activationDuration: float = math.inf, weight: float = 1.0):
        self.inputs = inputs
        self.neuronId = neuronId
        self.datetime = datetime.datetime.now()
        self.activationDuration = activationDuration
        self.weight = weight
        self.activated = True

    def __eq__(self, other):
        return isinstance(other, Connection) \
               and self.inputs == other.inputs \
               and self.neuronId == other.neuronId \
               and self.activationDuration == other.activationDuration \
               and self.weight == other.weight \
               and self.activated == other.activated

    def __hash__(self):
        h = hash(self.neuronId) + hash(self.activationDuration)

        for input in self.inputs:
            h += hash(input)

        return h

    def origin_input_types(self):
        types = []

        for input in self.inputs:
            if (isinstance(input, Neuron) and len(input.inputTypes) == 0):
                types.append(input.outputType)
            elif (isinstance(input, Connection)):
                types.extend(input.origin_input_types())
            else:
                types.append(type(input))

        return types

    def origin_input_values(self):
        values = []

        for input in self.inputs:
            if (isinstance(input, Neuron) and len(input.inputTypes) == 0):
                values.append(input.output())
            elif (isinstance(input, Connection)):
                values.extend(input.origin_input_values())
            else:
                values.append(input)

        return values

    def is_active(self):
        if (self.activationDuration == math.inf):
            return True

        return (datetime.datetime.now() - self.datetime > datetime.timedelta(milliseconds = self.activationDuration))
