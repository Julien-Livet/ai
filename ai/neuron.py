import datetime
import inspect
import math

class Neuron:
    def __init__(self, function, name: str = "", inputTypes: list = None, outputType = None, activationDuration: float = math.inf, weight: float = 1.0, module: str = "", limitationTimeout: float = None):
        self.function = function
        self.name = name
        self.datetime = datetime.datetime.now()
        self.activationDuration = activationDuration
        self.weight = weight
        self.module = module

        sig = inspect.signature(function)

        self.parameters = sig.parameters
        self.return_annotation = sig.return_annotation

        if (inputTypes is None):
            self.inputTypes = []

            for k, v in self.parameters.items():
                if (not v.annotation is inspect._empty):
                    self.inputTypes.append(v.annotation)
        else:
            self.inputTypes = inputTypes

        if (outputType is None):
            self.outputType = self.return_annotation
        else:
            self.outputType = outputType

        self.activated = True
        self.activationLevel = 0
        self.limitationTimeout = limitationTimeout

    def __eq__(self, other):
        return isinstance(other, Neuron) \
               and self.function == other.function \
               and self.name == other.name \
               and self.activationDuration == other.activationDuration \
               and self.weight == other.weight \
               and self.parameters == other.parameters \
               and self.return_annotation == other.return_annotation \
               and self.inputTypes == other.inputTypes \
               and self.outputType == other.outputType \
               and self.activated == other.activated \
               and self.activationLevel == other.activationLevel \
               and self.limitationTimeout == other.limitationTimeout \
               and self.module == other.module

    def __hash__(self):
        return hash(self.function) + hash(self.name) + hash(self.activationDuration) + hash(self.activationLevel) + hash(self.module)

    def output(self, *input):
        return self.function(*input)

    def is_active(self):
        if (self.activationDuration == math.inf):
            return True

        return (datetime.datetime.now() - self.datetime > datetime.timedelta(milliseconds = self.activationDuration))
