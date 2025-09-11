from brain import Brain
from neuron import Neuron
import numpy as np

def add_tuple(x: tuple, y: tuple) -> tuple:
    return x + y

def len_tuple(x: tuple) -> int:
    return len(x)

def range_tuple(start: int, stop: int, step: int) -> tuple:
    return tuple(range(start, stop, step))

def reversed_tuple(x: tuple) -> tuple:
    return tuple(reversed(x))

def tuple_to_ndarray(x: tuple) -> np.ndarray:
    return np.array(x)

def tuple_to_list(x: tuple) -> list:
    return list(x)

def tuple_to_set(x: tuple) -> set:
    return set(x)

def tuple_to_str(x: tuple) -> str:
    return str(x)

def add(brain: Brain):
    neuronIds = {}

    neuronIds["add_tuple"] = brain.add(Neuron(add_tuple, "add_tuple"))
    neuronIds["len_tuple"] = brain.add(Neuron(len_tuple, "len_tuple"))
    neuronIds["range_tuple"] = brain.add(Neuron(range_tuple, "range_tuple"))
    neuronIds["reversed_tuple"] = brain.add(Neuron(reversed_tuple, "reversed_tuple"))
    neuronIds["tuple_to_ndarray"] = brain.add(Neuron(tuple_to_ndarray, "tuple_to_ndarray"))
    neuronIds["tuple_to_list"] = brain.add(Neuron(tuple_to_list, "tuple_to_list"))
    neuronIds["tuple_to_set"] = brain.add(Neuron(tuple_to_set, "tuple_to_set"))
    neuronIds["tuple_to_str"] = brain.add(Neuron(tuple_to_str, "tuple_to_str"))

    return neuronIds

def add_value(brain: Brain, x: tuple, name = None):
    neuronIds = {}

    if (name is None):
        name = str(x)

    def value(x = x) -> tuple:
        return x if type(x) is tuple else x()

    neuronIds[name] = brain.add(Neuron(value, name))

    return neuronIds
