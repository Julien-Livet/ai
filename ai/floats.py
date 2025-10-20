from brain import Brain
import math
from neuron import Neuron

def add_float(x: float, y: float) -> float:
    return x + y

def sub_float(x: float, y: float) -> float:
    return x - y

def mul_float(x: float, y: float) -> float:
    return x * y

def truediv_float(x: float, y: float) -> float:
    return x / y

def floordiv_float(x: float, y: float) -> float:
    return x // y

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

def float_to_int(x: float) -> int:
    return int(x)

def eq_float(x: float, y: float) -> bool:
    return x == y

def ne_float(x: float, y: float) -> bool:
    return x != y

def gt_float(x: float, y: float) -> bool:
    return x > y

def lt_float(x: float, y: float) -> bool:
    return x < y

def ge_float(x: float, y: float) -> bool:
    return x >= y

def le_float(x: float, y: float) -> bool:
    return x <= y

def fabs_float(x: float) -> float:
    return math.fabs(x)

def ceil_float(x: float) -> float:
    return math.ceil(x)

def floor_float(x: float) -> float:
    return math.floor(x)

def trunc_float(x: float) -> float:
    return math.trunc(x)

def add(brain: Brain):
    neuronIds = {}

    neuronIds["pi"] = brain.add(Neuron(lambda: math.pi, "pi", inputTypes = [], outputType = float, module = "floats.constants"))
    neuronIds["e"] = brain.add(Neuron(lambda: math.e, "e", inputTypes = [], outputType = float, module = "floats.constants"))
    neuronIds["tau"] = brain.add(Neuron(lambda: math.tau, "tau", inputTypes = [], outputType = float, module = "floats.constants"))
    neuronIds["inf"] = brain.add(Neuron(lambda: math.inf, "inf", inputTypes = [], outputType = float, module = "floats.constants"))
    neuronIds["nan"] = brain.add(Neuron(lambda: math.nan, "nan", inputTypes = [], outputType = float, module = "floats.constants"))

    neuronIds["add_float"] = brain.add(Neuron(add_float, "add_float", module = "floats.operators.arithmetic"))
    neuronIds["sub_float"] = brain.add(Neuron(sub_float, "sub_float", module = "floats.operators.arithmetic"))
    neuronIds["mul_float"] = brain.add(Neuron(mul_float, "mul_float", module = "floats.operators.arithmetic"))
    neuronIds["truediv_float"] = brain.add(Neuron(truediv_float, "truediv_float", module = "floats.operators.arithmetic"))
    neuronIds["floordiv_float"] = brain.add(Neuron(floordiv_float, "floordiv_float", module = "floats.operators.arithmetic"))
    neuronIds["abs_float"] = brain.add(Neuron(abs_float, "abs_float", module = "floats.operators.functions"))
    neuronIds["neg_float"] = brain.add(Neuron(neg_float, "neg_float", module = "floats.operators.functions"))
    neuronIds["sqrt_float"] = brain.add(Neuron(sqrt_float, "sqrt_float", module = "floats.functions"))
    neuronIds["log_float"] = brain.add(Neuron(log_float, "log_float", module = "floats.functions"))
    neuronIds["exp_float"] = brain.add(Neuron(exp_float, "exp_float", module = "floats.functions"))
    neuronIds["cos_float"] = brain.add(Neuron(cos_float, "cos_float", module = "floats.functions.trigonometric"))
    neuronIds["sin_float"] = brain.add(Neuron(sin_float, "sin_float", module = "floats.functions.trigonometric"))
    neuronIds["tan_float"] = brain.add(Neuron(tan_float, "tan_float", module = "floats.functions.trigonometric"))
    neuronIds["acos_float"] = brain.add(Neuron(acos_float, "acos_float", module = "floats.functions.trigonometric"))
    neuronIds["asin_float"] = brain.add(Neuron(asin_float, "asin_float", module = "floats.functions.trigonometric"))
    neuronIds["atan_float"] = brain.add(Neuron(atan_float, "atan_float", module = "floats.functions.trigonometric"))
    neuronIds["cosh_float"] = brain.add(Neuron(cosh_float, "cosh_float", module = "floats.functions.hyperbolic"))
    neuronIds["sinh_float"] = brain.add(Neuron(sinh_float, "sinh_float", module = "floats.functions.hyperbolic"))
    neuronIds["tanh_float"] = brain.add(Neuron(tanh_float, "tanh_float", module = "floats.functions.hyperbolic"))
    neuronIds["acosh_float"] = brain.add(Neuron(acosh_float, "acosh_float", module = "floats.functions.hyperbolic"))
    neuronIds["asinh_float"] = brain.add(Neuron(asinh_float, "asinh_float", module = "floats.functions.hyperbolic"))
    neuronIds["atanh_float"] = brain.add(Neuron(atanh_float, "atanh_float", module = "floats.functions.hyperbolic"))
    neuronIds["float_to_str"] = brain.add(Neuron(float_to_str, "float_to_str", module = "floats.functions.conversion"))
    neuronIds["float_to_int"] = brain.add(Neuron(float_to_int, "float_to_int", module = "floats.functions.conversion"))
    neuronIds["eq_float"] = brain.add(Neuron(eq_float, "eq_float", module = "floats.operators.comparison"))
    neuronIds["ne_float"] = brain.add(Neuron(ne_float, "ne_float", module = "floats.operators.comparison"))
    neuronIds["gt_float"] = brain.add(Neuron(gt_float, "gt_float", module = "floats.operators.comparison"))
    neuronIds["lt_float"] = brain.add(Neuron(lt_float, "lt_float", module = "floats.operators.comparison"))
    neuronIds["ge_float"] = brain.add(Neuron(ge_float, "ge_float", module = "floats.operators.comparison"))
    neuronIds["le_float"] = brain.add(Neuron(le_float, "le_float", module = "floats.operators.comparison"))
    neuronIds["fabs_float"] = brain.add(Neuron(fabs_float, "fabs_float", module = "floats.functions.arithmetic"))
    neuronIds["ceil_float"] = brain.add(Neuron(ceil_float, "ceil_float", module = "floats.functions.arithmetic"))
    neuronIds["floor_float"] = brain.add(Neuron(floor_float, "floor_float", module = "floats.functions.arithmetic"))
    neuronIds["trunc_float"] = brain.add(Neuron(trunc_float, "trunc_float", module = "floats.functions.arithmetic"))

    return neuronIds

def add_value(brain: Brain, x: float, name: str = None):
    neuronIds = {}

    if (name is None):
        name = str(x)

    def value(x = x) -> float:
        return x if type(x) is float else x()

    neuronIds[name] = brain.add(Neuron(value, name, module = "floats.variables"))

    return neuronIds
