from brain import Brain
from neuron import Neuron

class Digit:
    def __init__(self, value: int):
        assert(isinstance(value, int))
        assert(0 <= value <= 9)

        self.value = value

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return self.value

def digit_to_str(x: Digit) -> str:
    return str(x)

def add(brain: Brain):
    neuronIds = {}

    for i in range(10):
        def number(i = i) -> Digit:
            return Digit(int(i))

        neuronIds[str(i)] = brain.add(Neuron(number, str(i), module = "digits.constants"))
    
    neuronIds["digit_to_str"] = brain.add(Neuron(digit_to_str, "digit_to_str", module = "digits.functions.conversion"))
    
    return neuronIds

def add_value(brain: Brain, x: Digit, name: str = None):
    neuronIds = {}

    if (name is None):
        name = str(x)

    def value(x = x) -> Digit:
        return x if type(x) is Digit else x()

    neuronIds[name] = brain.add(Neuron(value, name, module = "digits.variables"))

    return neuronIds
