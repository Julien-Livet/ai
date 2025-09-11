from brain import Brain
import copy
from neuron import Neuron
import numpy as np
import random

def add_set(x: set, y: set) -> set:
    return x | y

def len_set(x: list) -> int:
    return len(x)

def range_set(start: int, stop: int, step: int) -> set:
    return set(range(start, stop, step))

def set_to_ndarray(x: set) -> np.ndarray:
    return np.array(x)

def set_to_list(x: set) -> list:
    return tuple(x)

def set_to_tuple(x: set) -> list:
    return tuple(x)

def set_to_str(x: set) -> str:
    return str(x)

def add(brain: Brain):
    neuronIds = {}

    neuronIds["add_set"] = brain.add(Neuron(add_set, "add_set"))
    neuronIds["len_set"] = brain.add(Neuron(len_set, "len_set"))
    neuronIds["range_set"] = brain.add(Neuron(range_set, "range_set"))
    neuronIds["set_to_ndarray"] = brain.add(Neuron(set_to_ndarray, "set_to_ndarray"))
    neuronIds["set_to_list"] = brain.add(Neuron(set_to_list, "set_to_list"))
    neuronIds["set_to_tuple"] = brain.add(Neuron(set_to_tuple, "set_to_tuple"))
    neuronIds["set_to_str"] = brain.add(Neuron(set_to_str, "set_to_str"))

    return neuronIds

def add_value(brain: Brain, x: set, name = None):
    neuronIds = {}

    if (name is None):
        name = str(x)

    def value(x = x) -> set:
        return x

    neuronIds[name] = brain.add(Neuron(value, name))

    return neuronIds
