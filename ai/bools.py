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

def eq_bool(x: bool, y: bool) -> bool:
    return x == y

def ne_bool(x: bool, y: bool) -> bool:
    return x != y

def bool_to_int(x: bool) -> int:
    return int(x)

def add(brain: Brain):
    neuronIds = {}

    def true() -> bool:
        return True

    neuronIds["True"] = brain.add(Neuron(true, "True", module = "bools.constants"))

    def false() -> bool:
        return False

    neuronIds["False"] = brain.add(Neuron(false, "False", module = "bools.constants"))

    neuronIds["not_bool"] = brain.add(Neuron(not_bool, "not_bool", module = "bools.functions"))
    neuronIds["and_bool"] = brain.add(Neuron(and_bool, "and_bool", module = "bools.functions"))
    neuronIds["or_bool"] = brain.add(Neuron(or_bool, "or_bool", module = "bools.functions"))
    neuronIds["xor_bool"] = brain.add(Neuron(xor_bool, "xor_bool", module = "bools.functions"))
    neuronIds["bool_to_str"] = brain.add(Neuron(bool_to_str, "bool_to_str", module = "bools.functions"))
    neuronIds["eq_bool"] = brain.add(Neuron(eq_bool, "eq_bool", module = "bools.operators.comparison"))
    neuronIds["ne_bool"] = brain.add(Neuron(ne_bool, "ne_bool", module = "bools.operators.comparison"))
    neuronIds["bool_to_int"] = brain.add(Neuron(bool_to_int, "bool_to_int", module = "bools.functions.conversion"))

    return neuronIds

def add_value(brain: Brain, x: bool, name: str = None):
    neuronIds = {}

    if (name is None):
        name = str(x)

    def value(x = x) -> bool:
        return x if type(x) is bool else x()

    neuronIds[name] = brain.add(Neuron(value, name))

    return neuronIds
