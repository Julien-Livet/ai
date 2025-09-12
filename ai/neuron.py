import datetime
import inspect

class Neuron:
    def __init__(self, function, name = "", inputTypes = None, outputType = None):
        self.function = function
        self.name = name
        self.datetime = datetime.datetime.now()

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
        
        self.activated = False
        self.activationLevel = 0

    def output(self, *input):
        return self.function(*input)
