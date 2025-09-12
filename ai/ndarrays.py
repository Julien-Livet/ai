from brain import Brain
import copy
from neuron import Neuron
import numpy as np
import random

def add_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return x + y

def sub_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return x - y

def mul_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return x * y

def div_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return x / y

def pow_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return x ** y

def mulmat_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return x @ y

def abs_ndarray(x: np.ndarray) -> np.ndarray:
    return abs(x)

def neg_ndarray(x: np.ndarray) -> np.ndarray:
    return -x

def len_ndarray(x: np.ndarray) -> int:
    return len(x)

def reversed_ndarray(x: np.ndarray) -> np.ndarray:
    return np.array(list(reversed(x)))

def ndarray_to_list(x: np.ndarray) -> list:
    return list(x)

def ndarray_to_set(x: np.ndarray) -> set:
    return set(x)

def ndarray_to_tuple(x: np.ndarray) -> tuple:
    return tuple(x)

def shuffle_ndarray(x: np.ndarray) -> np.ndarray:
    y = copy.deepcopy(x)

    random.shuffle(y)

    return y

def sqrt_ndarray(x: np.ndarray) -> np.ndarray:
    return np.sqrt(x)

def log_ndarray(x: np.ndarray) -> np.ndarray:
    return np.log(x)

def exp_ndarray(x: np.ndarray) -> np.ndarray:
    return np.exp(x)

def cos_ndarray(x: np.ndarray) -> np.ndarray:
    return np.cos(x)

def sin_ndarray(x: np.ndarray) -> np.ndarray:
    return np.sin(x)

def tan_ndarray(x: np.ndarray) -> np.ndarray:
    return np.tan(x)

def acos_ndarray(x: np.ndarray) -> np.ndarray:
    return np.acos(x)

def asin_ndarray(x: np.ndarray) -> np.ndarray:
    return np.asin(x)

def atan_ndarray(x: np.ndarray) -> np.ndarray:
    return np.atan(x)

def cosh_ndarray(x: np.ndarray) -> np.ndarray:
    return np.cosh(x)

def sinh_ndarray(x: np.ndarray) -> np.ndarray:
    return np.sinh(x)

def tanh_ndarray(x: np.ndarray) -> np.ndarray:
    return np.tanh(x)

def acosh_ndarray(x: np.ndarray) -> np.ndarray:
    return np.acosh(x)

def asinh_ndarray(x: np.ndarray) -> np.ndarray:
    return np.asinh(x)

def atanh_ndarray(x: np.ndarray) -> np.ndarray:
    return np.atanh(x)

def logical_not_ndarray(x: np.ndarray) -> np.ndarray:
    return np.logical_not(x)

def logical_and_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.logical_and(x, y)

def logical_or_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.bitwise_or(x, y)

def logical_xor_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.logical_xor(x, y)

def bitwise_and_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.bitwise_and(x, y)

def bitwise_or_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.bitwise_or(x, y)

def bitwise_xor_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.bitwise_xor(x, y)

def invert_ndarray(x: np.ndarray) -> np.ndarray:
    return np.invert(x)

def dot_ndarray(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.dot(x, y))

def cross_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.cross(x, y)

def ndarray_to_str(x: np.ndarray) -> str:
    return str(x)

def add(brain: Brain):
    neuronIds = {}

    neuronIds["add_ndarray"] = brain.add(Neuron(add_ndarray, "add_ndarray"))
    neuronIds["sub_ndarray"] = brain.add(Neuron(sub_ndarray, "sub_ndarray"))
    neuronIds["mul_ndarray"] = brain.add(Neuron(mul_ndarray, "mul_ndarray"))
    neuronIds["div_ndarray"] = brain.add(Neuron(div_ndarray, "div_ndarray"))
    neuronIds["pow_ndarray"] = brain.add(Neuron(pow_ndarray, "pow_ndarray"))
    neuronIds["mulmat_ndarray"] = brain.add(Neuron(mulmat_ndarray, "mulmat_ndarray"))
    neuronIds["abs_ndarray"] = brain.add(Neuron(abs_ndarray, "abs_ndarray"))
    neuronIds["neg_ndarray"] = brain.add(Neuron(neg_ndarray, "neg_ndarray"))
    neuronIds["len_ndarray"] = brain.add(Neuron(len_ndarray, "len_ndarray"))
    neuronIds["reversed_ndarray"] = brain.add(Neuron(reversed_ndarray, "reversed_ndarray"))
    neuronIds["ndarray_to_list"] = brain.add(Neuron(ndarray_to_list, "ndarray_to_list"))
    neuronIds["ndarray_to_set"] = brain.add(Neuron(ndarray_to_set, "ndarray_to_set"))
    neuronIds["ndarray_to_tuple"] = brain.add(Neuron(ndarray_to_tuple, "ndarray_to_tuple"))
    neuronIds["shuffle_ndarray"] = brain.add(Neuron(shuffle_ndarray, "shuffle_ndarray"))
    neuronIds["sqrt_ndarray"] = brain.add(Neuron(sqrt_ndarray, "sqrt_ndarray"))
    neuronIds["log_ndarray"] = brain.add(Neuron(log_ndarray, "log_ndarray"))
    neuronIds["exp_ndarray"] = brain.add(Neuron(exp_ndarray, "exp_ndarray"))
    neuronIds["cos_ndarray"] = brain.add(Neuron(cos_ndarray, "cos_ndarray"))
    neuronIds["sin_ndarray"] = brain.add(Neuron(sin_ndarray, "sin_ndarray"))
    neuronIds["tan_ndarray"] = brain.add(Neuron(tan_ndarray, "tan_ndarray"))
    neuronIds["acos_ndarray"] = brain.add(Neuron(acos_ndarray, "acos_ndarray"))
    neuronIds["asin_ndarray"] = brain.add(Neuron(asin_ndarray, "asin_ndarray"))
    neuronIds["atan_ndarray"] = brain.add(Neuron(atan_ndarray, "atan_ndarray"))
    neuronIds["cosh_ndarray"] = brain.add(Neuron(cosh_ndarray, "cosh_ndarray"))
    neuronIds["sinh_ndarray"] = brain.add(Neuron(sinh_ndarray, "sinh_ndarray"))
    neuronIds["tanh_ndarray"] = brain.add(Neuron(tanh_ndarray, "tanh_ndarray"))
    neuronIds["acosh_ndarray"] = brain.add(Neuron(acosh_ndarray, "acosh_ndarray"))
    neuronIds["asinh_ndarray"] = brain.add(Neuron(asinh_ndarray, "asinh_ndarray"))
    neuronIds["atanh_ndarray"] = brain.add(Neuron(atanh_ndarray, "atanh_ndarray"))
    neuronIds["logical_not_ndarray"] = brain.add(Neuron(logical_not_ndarray, "logical_not_ndarray"))
    neuronIds["logical_and_ndarray"] = brain.add(Neuron(logical_and_ndarray, "logical_and_ndarray"))
    neuronIds["logical_or_ndarray"] = brain.add(Neuron(logical_or_ndarray, "logical_or_ndarray"))
    neuronIds["logical_xor_ndarray"] = brain.add(Neuron(logical_xor_ndarray, "logical_xor_ndarray"))
    neuronIds["bitwise_and_ndarray"] = brain.add(Neuron(bitwise_and_ndarray, "bitwise_and_ndarray"))
    neuronIds["bitwise_or_ndarray"] = brain.add(Neuron(bitwise_or_ndarray, "bitwise_or_ndarray"))
    neuronIds["bitwise_xor_ndarray"] = brain.add(Neuron(bitwise_xor_ndarray, "bitwise_xor_ndarray"))
    neuronIds["invert_ndarray"] = brain.add(Neuron(invert_ndarray, "invert_ndarray"))
    neuronIds["dot_ndarray"] = brain.add(Neuron(dot_ndarray, "dot_ndarray"))
    neuronIds["cross_ndarray"] = brain.add(Neuron(cross_ndarray, "cross_ndarray"))
    neuronIds["ndarray_to_str"] = brain.add(Neuron(ndarray_to_str, "ndarray_to_str"))

    return neuronIds

def add_value(brain: Brain, x: np.ndarray, name = None):
    neuronIds = {}

    if (name is None):
        name = str(x)

    def value(x = x) -> np.ndarray:
        return x if type(x) is np.ndarray else x()

    neuronIds[name] = brain.add(Neuron(value, name))

    return neuronIds
