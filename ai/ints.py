from brain import Brain
from neuron import Neuron

def add_int(x: int, y: int) -> int:
    return x + y

def sub_int(x: int, y: int) -> int:
    return x - y

def mul_int(x: int, y: int) -> int:
    return x * y

def div_int(x: int, y: int) -> int:
    return x // y

def mod_int(x: int, y: int) -> int:
    return x % y

def pow_int(x: int, y: int) -> int:
    return x ** y

def and_int(x: int, y: int) -> int:
    return x & y

def or_int(x: int, y: int) -> int:
    return x | y

def xor_int(x: int, y: int) -> int:
    return x ^ y

def left_shift_int(x: int, y: int) -> int:
    return x << y

def right_shift_int(x: int, y: int) -> int:
    return x >> y

def complement_int(x: int) -> int:
    return ~x

def abs_int(x: int) -> int:
    return abs(x)

def neg_int(x: int) -> int:
    return -x

def int_to_str(x: int) -> str:
    return str(x)

def int_to_float(x: int) -> float:
    return float(x)

def int_to_bool(x: int) -> bool:
    return bool(x)

def eq_int(x: int, y: int) -> bool:
    return x == y

def ne_int(x: int, y: int) -> bool:
    return x != y

def gt_int(x: int, y: int) -> bool:
    return x > y

def lt_int(x: int, y: int) -> bool:
    return x < y

def ge_int(x: int, y: int) -> bool:
    return x > y

def le_int(x: int, y: int) -> bool:
    return x < y

def factorial_int(x: int) -> int:
    return math.factorial(x)

def comb_int(n: int, k: int) -> int:
    return math.comb(n, k)

def perm_int(n: int, k: int) -> int:
    return math.perm(n, k)

def isqrt_int(x: int) -> int:
    return math.isqrt(x)

def add(brain: Brain):
    neuronIds = {}

    neuronIds["add_int"] = brain.add(Neuron(add_int, "add_int", module = "ints.operators.arithmetic"))
    neuronIds["sub_int"] = brain.add(Neuron(sub_int, "sub_int", module = "ints.operators.arithmetic"))
    neuronIds["mul_int"] = brain.add(Neuron(mul_int, "mul_int", module = "ints.operators.arithmetic"))
    neuronIds["div_int"] = brain.add(Neuron(div_int, "div_int", module = "ints.operators.arithmetic"))
    neuronIds["mod_int"] = brain.add(Neuron(mod_int, "mod_int", module = "ints.operators.arithmetic"))
    neuronIds["pow_int"] = brain.add(Neuron(pow_int, "pow_int", module = "ints.operators.arithmetic"))
    neuronIds["and_int"] = brain.add(Neuron(and_int, "and_int", module = "ints.operators.bitwise"))
    neuronIds["or_int"] = brain.add(Neuron(or_int, "or_int", module = "ints.operators.bitwise"))
    neuronIds["xor_int"] = brain.add(Neuron(xor_int, "xor_int", module = "ints.operators.bitwise"))
    neuronIds["left_shift_int"] = brain.add(Neuron(left_shift_int, "left_shift_int", module = "ints.operators.bitwise"))
    neuronIds["right_shift_int"] = brain.add(Neuron(right_shift_int, "right_shift_int", module = "ints.operators.bitwise"))
    neuronIds["complement_int"] = brain.add(Neuron(complement_int, "complement_int", module = "ints.operators.bitwise"))
    neuronIds["abs_int"] = brain.add(Neuron(abs_int, "abs_int", module = "ints.functions"))
    neuronIds["neg_int"] = brain.add(Neuron(neg_int, "neg_int", module = "ints.functions"))
    neuronIds["int_to_str"] = brain.add(Neuron(int_to_str, "int_to_str", module = "ints.functions.conversion"))
    neuronIds["int_to_float"] = brain.add(Neuron(int_to_float, "int_to_float", module = "ints.functions.conversion"))
    neuronIds["int_to_bool"] = brain.add(Neuron(int_to_bool, "int_to_bool", module = "ints.functions.conversion"))
    neuronIds["eq_int"] = brain.add(Neuron(eq_int, "eq_int", module = "ints.operators.comparison"))
    neuronIds["ne_int"] = brain.add(Neuron(ne_int, "ne_int", module = "ints.operators.comparison"))
    neuronIds["gt_int"] = brain.add(Neuron(gt_int, "gt_int", module = "ints.operators.comparison"))
    neuronIds["lt_int"] = brain.add(Neuron(lt_int, "lt_int", module = "ints.operators.comparison"))
    neuronIds["ge_int"] = brain.add(Neuron(ge_int, "ge_int", module = "ints.operators.comparison"))
    neuronIds["le_int"] = brain.add(Neuron(le_int, "le_int", module = "ints.operators.comparison"))
    neuronIds["factorial_int"] = brain.add(Neuron(factorial_int, "factorial_int", module = "ints.functions.numbertheoric"))
    neuronIds["comb_int"] = brain.add(Neuron(comb_int, "comb_int", module = "ints.functions.numbertheoric"))
    neuronIds["perm_int"] = brain.add(Neuron(perm_int, "perm_int", module = "ints.functions.numbertheoric"))
    neuronIds["isqrt_int"] = brain.add(Neuron(isqrt_int, "isqrt_int", module = "ints.functions.numbertheoric"))

    return neuronIds

def add_value(brain: Brain, x: int, name: str = None):
    neuronIds = {}

    if (name is None):
        name = str(x)

    def value(x = x) -> int:
        return x if type(x) is int else x()

    neuronIds[name] = brain.add(Neuron(value, name, module = "ints.variables"))

    return neuronIds
