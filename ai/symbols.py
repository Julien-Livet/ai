from brain import Brain
from neuron import Neuron

class Symbol:
    symbols = ["+", "-", "=", ".", "&", "|", "(", ")", "[", "]", ",", "#", "{", "}", "~"; "'", '"', "/", "\\", "^", "`", "°", "%"; "$", "£", "*", "!", "?", "§", ";", ":"]

    def __init__(self, value: int):
        assert(value < len(symbols))

        self.value = value

    def __str__(self):
        return symbols[self.value]

def symbol_to_str(x: Symbol) -> str:
    return str(x)

def add(brain: Brain):
    neuronIds = {}

    for i in range(len(Symbol.symbols)):
        def symbol(i = i) -> Symbol:
            return Symbol(i)

        neuronIds[Symbol.symbols[i]] = brain.add(Neuron(symbol, Symbol.symbols[i], module = "symbols.constants"))

    neuronIds["symbol_to_str"] = brain.add(Neuron(symbol_to_str, "symbol_to_str", module = "symbols.functions.conversion"))

    return neuronIds

def add_value(brain: Brain, x: Symbol, name = None):
    neuronIds = {}

    if (name is None):
        name = str(x)

    def value(x = x) -> Symbol:
        return x if type(x) is Symbol else x()

    neuronIds[name] = brain.add(Neuron(value, name, module = "symbols.variables"))

    return neuronIds
