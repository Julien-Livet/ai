import inspect

class Neuron:
    def __init__(self, function, name = ""):
        self.function = function
        self.name = name
        
        sig = inspect.signature(function)
        
        self.parameters = sig.parameters
        self.return_annotation = sig.return_annotation

        self.inputTypes = []
        
        for k, v in self.parameters.items():
            if (not v.annotation is inspect._empty):
                self.inputTypes.append(v.annotation)
            
        self.outputType = self.return_annotation
        
        self.activated = False
        self.activationLevel = 0

    def output(self, *input):
        return self.function(*input)
