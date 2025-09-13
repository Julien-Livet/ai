from brain import Brain
from neuron import Neuron

def add_str(x: str, y: str) -> str:
    return x + y

def len_str(x: str) -> int:
    return len(x)

def lower_str(x: str) -> str:
    return x.lower()

def upper_str(x: str) -> str:
    return x.upper()

def str_to_bool(x: str) -> bool:
    return bool(x)

def str_to_float(x: str) -> float:
    return float(x)

def str_to_int(x: str) -> int:
    return int(x)

def add(brain: Brain):
    neuronIds = {}

    neuronIds["add_str"] = brain.add(Neuron(add_str, "add_str", module = "strs.functions"))
    neuronIds["len_str"] = brain.add(Neuron(len_str, "len_str", module = "strs.functions"))
    neuronIds["lower_str"] = brain.add(Neuron(lower_str, "lower_str", module = "strs.functions"))
    neuronIds["upper_str"] = brain.add(Neuron(upper_str, "upper_str", module = "strs.functions"))
    neuronIds["str_to_bool"] = brain.add(Neuron(str_to_bool, "str_to_bool", module = "strs.functions.conversion"))
    neuronIds["str_to_float"] = brain.add(Neuron(str_to_float, "str_to_float", module = "strs.functions.conversion"))
    neuronIds["str_to_int"] = brain.add(Neuron(str_to_int, "str_to_int", module = "strs.functions.conversion"))

    return neuronIds

def add_value(brain: Brain, x: str, name: str = None):
    neuronIds = {}

    if (name is None):
        name = x

    def value(x = x) -> str:
        return x if type(x) is str else x()

    neuronIds[name] = brain.add(Neuron(value, name, module = "strs.variables"))

    return neuronIds
