from brain import Brain
from neuron import Neuron

def not_bool(x: bool) -> bool:
    return not x

def and_bool(x: bool, y: bool) -> bool:
    return x and y

def or_bool(x: bool, y: bool) -> bool:
    return x or y

def xor_bool(x: bool, y: bool) -> bool:
    return x ^ y

def bool_to_str(x: int) -> str:
    return str(x)

def add(brain: Brain):
    neuronIds = {}

    def true() -> bool:
        return True

    neuronIds["True"] = brain.add(Neuron(true, "True"))

    def false() -> bool:
        return False

    neuronIds["False"] = brain.add(Neuron(false, "False"))

    neuronIds["not_bool"] = brain.add(Neuron(not_bool, "not_bool"))
    neuronIds["and_bool"] = brain.add(Neuron(and_bool, "and_bool"))
    neuronIds["or_bool"] = brain.add(Neuron(or_bool, "or_bool"))
    neuronIds["xor_bool"] = brain.add(Neuron(xor_bool, "xor_bool"))
    neuronIds["bool_to_str"] = brain.add(Neuron(bool_to_str, "bool_to_str"))

    return neuronIds

def add_value(brain: Brain, x: bool, name = None):
    neuronIds = {}

    if (name is None):
        name = str(x)

    def value(x = x) -> bool:
        return x if type(x) is bool else x()

    neuronIds[name] = brain.add(Neuron(value, name))

    return neuronIds
