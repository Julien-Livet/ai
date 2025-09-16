from brain import Brain
from neuron import Neuron

class Char:
    def __init__(self, value: str):
        assert(isinstance(value, str))
        assert(len(value) == 1)
        assert(value.isalpha())

        self.value = value

    def __str__(self):
        return str(self.value)

def char_to_str(x: Char) -> str:
    return str(x)

def lower_char(x: Char) -> Char:
    return Char(str(x).lower())

def upper_char(x: Char) -> Char:
    return Char(str(x).upper())

def add_char(x: Char, y: Char) -> str:
    return str(x) + str(y)

def char_add_str(x: Char, s: str) -> str:
    return str(x) + s

def str_add_char(s: str, x: Char) -> str:
    return s + str(x)

def add(brain: Brain):
    neuronIds = {}

    for i in range(26):
        def number(i = i) -> Char:
            return Char(chr(ord('a') + i))

        neuronIds[chr(ord('a') + i)] = brain.add(Neuron(number, chr(ord('a') + i), module = "chars.constants"))

    for c in ["à", "á", "â", "ä", "é", "è", "ê", "ë", "î", "ï", "ô", "ö", "ù", "ü", "û", "ÿ", "ç"]:
        neuronIds[c] = brain.add(Neuron(lambda c = c: Char(c), c, outputType = Char, module = "chars.constants"))

    neuronIds["char_to_str"] = brain.add(Neuron(char_to_str, "char_to_str", module = "chars.functions.conversion"))
    neuronIds["lower_char"] = brain.add(Neuron(lower_char, "lower_char", module = "chars.functions"))
    neuronIds["upper_char"] = brain.add(Neuron(upper_char, "upper_char", module = "chars.functions"))
    neuronIds["add_char"] = brain.add(Neuron(add_char, "add_char", module = "chars.functions"))
    neuronIds["char_add_str"] = brain.add(Neuron(char_add_str, "char_add_str", module = "chars.functions"))
    neuronIds["str_add_char"] = brain.add(Neuron(str_add_char, "str_add_char", module = "chars.functions"))

    return neuronIds

def add_value(brain: Brain, x: Char, name: str = None):
    neuronIds = {}

    if (name is None):
        name = str(x)

    def value(x = x) -> Char:
        return x if type(x) is Char else x()

    neuronIds[name] = brain.add(Neuron(value, name, module = "chars.variables"))

    return neuronIds
