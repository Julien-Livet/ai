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

def ceil_ndarray(x: np.ndarray) -> np.ndarray:
    return np.ceil(x)

def floor_ndarray(x: np.ndarray) -> np.ndarray:
    return np.floor(x)

def inv_ndarray(x: np.ndarray) -> np.ndarray:
    return np.linalg.inv(x)

def eye_ndarray(x: int) -> np.ndarray:
    return np.eye(x)

def trace_ndarray(x: np.ndarray) -> float:
    return np.trace(x)

def add(brain: Brain):
    neuronIds = {}

    neuronIds["add_ndarray"] = brain.add(Neuron(add_ndarray, "add_ndarray", module = "ndarrays.operators.arithmetic"))
    neuronIds["sub_ndarray"] = brain.add(Neuron(sub_ndarray, "sub_ndarray", module = "ndarrays.operators.arithmetic"))
    neuronIds["mul_ndarray"] = brain.add(Neuron(mul_ndarray, "mul_ndarray", module = "ndarrays.operators.arithmetic"))
    neuronIds["div_ndarray"] = brain.add(Neuron(div_ndarray, "div_ndarray", module = "ndarrays.operators.arithmetic"))
    neuronIds["pow_ndarray"] = brain.add(Neuron(pow_ndarray, "pow_ndarray", module = "ndarrays.operators.arithmetic"))
    neuronIds["mulmat_ndarray"] = brain.add(Neuron(mulmat_ndarray, "mulmat_ndarray", module = "ndarrays.operators.linearalgebra"))
    neuronIds["abs_ndarray"] = brain.add(Neuron(abs_ndarray, "abs_ndarray", module = "ndarrays.functions.conversion"))
    neuronIds["neg_ndarray"] = brain.add(Neuron(neg_ndarray, "neg_ndarray", module = "ndarrays.functions.conversion"))
    neuronIds["len_ndarray"] = brain.add(Neuron(len_ndarray, "len_ndarray", module = "ndarrays.functions.conversion"))
    neuronIds["reversed_ndarray"] = brain.add(Neuron(reversed_ndarray, "reversed_ndarray", module = "ndarrays.functions"))
    neuronIds["ndarray_to_list"] = brain.add(Neuron(ndarray_to_list, "ndarray_to_list", module = "ndarrays.functions.conversion"))
    neuronIds["ndarray_to_set"] = brain.add(Neuron(ndarray_to_set, "ndarray_to_set", module = "ndarrays.functions.conversion"))
    neuronIds["ndarray_to_tuple"] = brain.add(Neuron(ndarray_to_tuple, "ndarray_to_tuple", module = "ndarrays.functions.conversion"))
    neuronIds["shuffle_ndarray"] = brain.add(Neuron(shuffle_ndarray, "shuffle_ndarray", module = "ndarrays.functions"))
    neuronIds["sqrt_ndarray"] = brain.add(Neuron(sqrt_ndarray, "sqrt_ndarray", module = "ndarrays.functions"))
    neuronIds["log_ndarray"] = brain.add(Neuron(log_ndarray, "log_ndarray", module = "ndarrays.functions"))
    neuronIds["exp_ndarray"] = brain.add(Neuron(exp_ndarray, "exp_ndarray", module = "ndarrays.functions"))
    neuronIds["cos_ndarray"] = brain.add(Neuron(cos_ndarray, "cos_ndarray", module = "ndarrays.functions.trigonometric"))
    neuronIds["sin_ndarray"] = brain.add(Neuron(sin_ndarray, "sin_ndarray", module = "ndarrays.functions.trigonometric"))
    neuronIds["tan_ndarray"] = brain.add(Neuron(tan_ndarray, "tan_ndarray", module = "ndarrays.functions.trigonometric"))
    neuronIds["acos_ndarray"] = brain.add(Neuron(acos_ndarray, "acos_ndarray", module = "ndarrays.functions.trigonometric"))
    neuronIds["asin_ndarray"] = brain.add(Neuron(asin_ndarray, "asin_ndarray", module = "ndarrays.functions.trigonometric"))
    neuronIds["atan_ndarray"] = brain.add(Neuron(atan_ndarray, "atan_ndarray", module = "ndarrays.functions.trigonometric"))
    neuronIds["cosh_ndarray"] = brain.add(Neuron(cosh_ndarray, "cosh_ndarray", module = "ndarrays.functions.hyperbolic"))
    neuronIds["sinh_ndarray"] = brain.add(Neuron(sinh_ndarray, "sinh_ndarray", module = "ndarrays.functions.hyperbolic"))
    neuronIds["tanh_ndarray"] = brain.add(Neuron(tanh_ndarray, "tanh_ndarray", module = "ndarrays.functions.hyperbolic"))
    neuronIds["acosh_ndarray"] = brain.add(Neuron(acosh_ndarray, "acosh_ndarray", module = "ndarrays.functions.hyperbolic"))
    neuronIds["asinh_ndarray"] = brain.add(Neuron(asinh_ndarray, "asinh_ndarray", module = "ndarrays.functions.hyperbolic"))
    neuronIds["atanh_ndarray"] = brain.add(Neuron(atanh_ndarray, "atanh_ndarray", module = "ndarrays.functions.hyperbolic"))
    neuronIds["logical_not_ndarray"] = brain.add(Neuron(logical_not_ndarray, "logical_not_ndarray", module = "ndarrays.operators.logical"))
    neuronIds["logical_and_ndarray"] = brain.add(Neuron(logical_and_ndarray, "logical_and_ndarray", module = "ndarrays.operators.logical"))
    neuronIds["logical_or_ndarray"] = brain.add(Neuron(logical_or_ndarray, "logical_or_ndarray", module = "ndarrays.operators.logical"))
    neuronIds["logical_xor_ndarray"] = brain.add(Neuron(logical_xor_ndarray, "logical_xor_ndarray", module = "ndarrays.operators.logical"))
    neuronIds["bitwise_and_ndarray"] = brain.add(Neuron(bitwise_and_ndarray, "bitwise_and_ndarray", module = "ndarrays.operators.bitwise"))
    neuronIds["bitwise_or_ndarray"] = brain.add(Neuron(bitwise_or_ndarray, "bitwise_or_ndarray", module = "ndarrays.operators.bitwise"))
    neuronIds["bitwise_xor_ndarray"] = brain.add(Neuron(bitwise_xor_ndarray, "bitwise_xor_ndarray", module = "ndarrays.operators.bitwise"))
    neuronIds["invert_ndarray"] = brain.add(Neuron(invert_ndarray, "invert_ndarray", module = "ndarrays.operators.bitwise"))
    neuronIds["dot_ndarray"] = brain.add(Neuron(dot_ndarray, "dot_ndarray", module = "ndarrays.functions.linearalgebra"))
    neuronIds["cross_ndarray"] = brain.add(Neuron(cross_ndarray, "cross_ndarray", module = "ndarrays.functions.linearalgebra"))
    neuronIds["ndarray_to_str"] = brain.add(Neuron(ndarray_to_str, "ndarray_to_str", module = "ndarrays.functions"))
    neuronIds["ceil_ndarray"] = brain.add(Neuron(ceil_ndarray, "ceil_ndarray", module = "ndarrays.functions.arithmetic"))
    neuronIds["floor_ndarray"] = brain.add(Neuron(floor_ndarray, "floor_ndarray", module = "ndarrays.functions.arithmetic"))
    neuronIds["inv_ndarray"] = brain.add(Neuron(inv_ndarray, "inv_ndarray", module = "ndarrays.functions.linearalgebra"))
    neuronIds["trace_ndarray"] = brain.add(Neuron(trace_ndarray, "trace_ndarray", module = "ndarrays.functions.linearalgebra"))
    neuronIds["eye_ndarray"] = brain.add(Neuron(eye_ndarray, "eye_ndarray", module = "ndarrays.functions.linearalgebra"))

    return neuronIds

def add_value(brain: Brain, x: np.ndarray, name = None):
    neuronIds = {}

    if (name is None):
        name = str(x)

    def value(x = x) -> np.ndarray:
        return x if type(x) is np.ndarray else x()

    neuronIds[name] = brain.add(Neuron(value, name, module = "ndarrays.variables"))

    return neuronIds
