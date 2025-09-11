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

def abs_int(x: int) -> int:
    return abs(x)

def neg_int(x: int) -> int:
    return -x

def complement_int(x: int) -> int:
    return ~x

def int_to_str(x: int) -> str:
    return str(x)

def add(brain: Brain):
    neuronIds = {}

    neuronIds["add_int"] = brain.add(Neuron(add_int, "add_int"))
    neuronIds["sub_int"] = brain.add(Neuron(sub_int, "sub_int"))
    neuronIds["mul_int"] = brain.add(Neuron(mul_int, "mul_int"))
    neuronIds["div_int"] = brain.add(Neuron(div_int, "div_int"))
    neuronIds["mod_int"] = brain.add(Neuron(mod_int, "mod_int"))
    neuronIds["pow_int"] = brain.add(Neuron(pow_int, "pow_int"))
    neuronIds["and_int"] = brain.add(Neuron(and_int, "and_int"))
    neuronIds["or_int"] = brain.add(Neuron(or_int, "or_int"))
    neuronIds["xor_int"] = brain.add(Neuron(xor_int, "xor_int"))
    neuronIds["left_shift_int"] = brain.add(Neuron(left_shift_int, "left_shift_int"))
    neuronIds["right_shift_int"] = brain.add(Neuron(right_shift_int, "right_shift_int"))
    neuronIds["abs_int"] = brain.add(Neuron(abs_int, "abs_int"))
    neuronIds["neg_int"] = brain.add(Neuron(neg_int, "neg_int"))
    neuronIds["complement_int"] = brain.add(Neuron(complement_int, "complement_int"))
    neuronIds["int_to_str"] = brain.add(Neuron(int_to_str, "int_to_str"))

    return neuronIds

def add_value(brain: Brain, x: int, name = None):
    neuronIds = {}

    if (name is None):
        name = str(x)

    def value(x = x) -> int:
        return x

    neuronIds[name] = brain.add(Neuron(value, name))

    return neuronIds
