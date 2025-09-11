from brain import Brain
import math
from neuron import Neuron

def add_float(x: float, y: float) -> float:
    return x + y

def sub_float(x: float, y: float) -> float:
    return x - y

def mul_float(x: float, y: float) -> float:
    return x * y

def div_float(x: float, y: float) -> float:
    return x / y

def abs_float(x: float) -> float:
    return abs(x)

def neg_float(x: float) -> float:
    return -x

def sqrt_float(x: float) -> float:
    return math.sqrt(x)

def log_float(x: float) -> float:
    return math.log(x)

def exp_float(x: float) -> float:
    return math.exp(x)

def cos_float(x: float) -> float:
    return math.cos(x)

def sin_float(x: float) -> float:
    return math.sin(x)

def tan_float(x: float) -> float:
    return math.tan(x)

def acos_float(x: float) -> float:
    return math.acos(x)

def asin_float(x: float) -> float:
    return math.asin(x)

def atan_float(x: float) -> float:
    return math.atan(x)

def cosh_float(x: float) -> float:
    return math.cosh(x)

def sinh_float(x: float) -> float:
    return math.sinh(x)

def tanh_float(x: float) -> float:
    return math.tanh(x)

def acosh_float(x: float) -> float:
    return math.acosh(x)

def asinh_float(x: float) -> float:
    return math.asinh(x)

def atanh_float(x: float) -> float:
    return math.atanh(x)

def float_to_str(x: float) -> str:
    return str(x)

def add(brain: Brain):
    neuronIds = {}

    neuronIds["add_float"] = brain.add(Neuron(add_float, "add_float"))
    neuronIds["sub_float"] = brain.add(Neuron(sub_float, "sub_float"))
    neuronIds["mul_float"] = brain.add(Neuron(mul_float, "mul_float"))
    neuronIds["div_float"] = brain.add(Neuron(div_float, "div_float"))
    neuronIds["abs_float"] = brain.add(Neuron(abs_float, "abs_float"))
    neuronIds["neg_float"] = brain.add(Neuron(neg_float, "neg_float"))
    neuronIds["sqrt_float"] = brain.add(Neuron(sqrt_float, "sqrt_float"))
    neuronIds["log_float"] = brain.add(Neuron(log_float, "log_float"))
    neuronIds["exp_float"] = brain.add(Neuron(exp_float, "exp_float"))
    neuronIds["cos_float"] = brain.add(Neuron(cos_float, "cos_float"))
    neuronIds["sin_float"] = brain.add(Neuron(sin_float, "sin_float"))
    neuronIds["tan_float"] = brain.add(Neuron(tan_float, "tan_float"))
    neuronIds["acos_float"] = brain.add(Neuron(acos_float, "acos_float"))
    neuronIds["asin_float"] = brain.add(Neuron(asin_float, "asin_float"))
    neuronIds["atan_float"] = brain.add(Neuron(atan_float, "atan_float"))
    neuronIds["cosh_float"] = brain.add(Neuron(cosh_float, "cosh_float"))
    neuronIds["sinh_float"] = brain.add(Neuron(sinh_float, "sinh_float"))
    neuronIds["tanh_float"] = brain.add(Neuron(tanh_float, "tanh_float"))
    neuronIds["acosh_float"] = brain.add(Neuron(acosh_float, "acosh_float"))
    neuronIds["asinh_float"] = brain.add(Neuron(asinh_float, "asinh_float"))
    neuronIds["atanh_float"] = brain.add(Neuron(atanh_float, "atanh_float"))
    neuronIds["float_to_str"] = brain.add(Neuron(float_to_str, "float_to_str"))
    
    return neuronIds

def add_value(brain: Brain, x: float, name = None):
    neuronIds = {}

    if (name is None):
        name = str(x)

    def value(x = x) -> float:
        return x if type(x) is float else x()

    neuronIds[name] = brain.add(Neuron(value, name))

    return neuronIds
