from brain import Brain
from neuron import Neuron

class Char:
    def __init__(self, value: str):
        assert(isinstance(value, str))
        assert(len(str) == 1)
        assert('a' <= value <= 'z')

        self.value = value

    def __str__(self):
        return str(self.value)

def char_to_str(x: Char) -> str:
    return str(x)

def lower_char(x: Char) -> Char:
    return Char(str(x).lower())

def upper_char(x: Char) -> Char:
    return Char(str(x).upper())

def add(brain: Brain):
    neuronIds = {}

    for i in range(26):
        def number(i = i) -> Char:
            return Char(chr(ord('a') + i))

        neuronIds[chr(ord('a') + i)] = brain.add(Neuron(number, chr(ord('a') + i)))

    neuronIds["char_to_str"] = brain.add(Neuron(char_to_str, "char_to_str"))
    neuronIds["lower_char"] = brain.add(Neuron(lower_char, "lower_char"))
    neuronIds["upper_char"] = brain.add(Neuron(upper_char, "upper_char"))

    return neuronIds

def add_value(brain: Brain, x: Char, name = None):
    neuronIds = {}

    if (name is None):
        name = str(x)

    def value(x = x) -> Char:
        return x if type(x) is Char else x()

    neuronIds[name] = brain.add(Neuron(value, name))

    return neuronIds
