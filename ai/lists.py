from brain import Brain
import copy
from neuron import Neuron
import numpy as np
import random

def add_list(x: list, y: list) -> list:
    return x + y

def len_list(x: list) -> int:
    return len(x)

def range_list(start: int, stop: int, step: int) -> list:
    return list(range(start, stop, step))

def reversed_list(x: list) -> list:
    return list(reversed(x))

def list_to_ndarray(x: list) -> np.ndarray:
    return np.array(x)

def list_to_set(x: list) -> set:
    return set(x)

def list_to_tuple(x: list) -> tuple:
    return tuple(x)

def shuffle_list(x: list) -> list:
    y = copy.deepcopy(x)

    random.shuffle(y)

    return y

def list_to_str(x: list) -> str:
    return str(x)

def add(brain: Brain):
    neuronIds = {}

    neuronIds["add_list"] = brain.add(Neuron(add_list, "add_list", module = "lists.functions"))
    neuronIds["len_list"] = brain.add(Neuron(len_list, "len_list", module = "lists.functions"))
    neuronIds["range_list"] = brain.add(Neuron(range_list, "range_list", module = "lists.functions"))
    neuronIds["reversed_list"] = brain.add(Neuron(reversed_list, "reversed_list", module = "lists.functions"))
    neuronIds["shuffle_list"] = brain.add(Neuron(shuffle_list, "shuffle_list", module = "lists.functions"))
    neuronIds["list_to_ndarray"] = brain.add(Neuron(list_to_ndarray, "list_to_ndarray", module = "lists.functions.conversion"))
    neuronIds["list_to_set"] = brain.add(Neuron(list_to_set, "list_to_set", module = "lists.functions.conversion"))
    neuronIds["list_to_tuple"] = brain.add(Neuron(list_to_tuple, "list_to_tuple", module = "lists.functions.conversion"))
    neuronIds["list_to_str"] = brain.add(Neuron(list_to_str, "list_to_str", module = "lists.functions.conversion"))

    return neuronIds

def add_value(brain: Brain, x: list, name = None):
    neuronIds = {}

    if (name is None):
        name = str(x)

    def value(x = x) -> list:
        return x if type(x) is list else x()

    neuronIds[name] = brain.add(Neuron(value, name, module = "lists.variables"))

    return neuronIds
