from brain import Brain
from connection import Connection
import chars
import digits
from neuron import Neuron
import numpy as np
import random
import strs
import symbols
import sympy

brain = Brain()
neuronIds = {}

neuronIds["e"] = brain.add(Neuron(lambda: chars.Char("e"), "e", outputType = chars.Char, module = "chars.constants"))
neuronIds["char_to_str"] = brain.add(Neuron(chars.char_to_str, "char_to_str", module = "chars.functions.conversion"))
neuronIds["lower_char"] = brain.add(Neuron(chars.lower_char, "lower_char", module = "chars.functions"))
neuronIds["upper_char"] = brain.add(Neuron(chars.upper_char, "upper_char", module = "chars.functions"))

neuronIds |= digits.add(brain)
neuronIds |= strs.add(brain)

for c in ["+", "-", "."]:
    def symbol(c = c) -> symbols.Symbol:
        return symbols.Symbol(symbols.Symbol.symbols.index(c))

    neuronIds[c] = brain.add(Neuron(symbol, c, module = "symbols.constants"))

neuronIds["symbol_to_str"] = brain.add(Neuron(symbols.symbol_to_str, "symbol_to_str", module = "symbols.functions.conversion"))

with_pretraining = True

if (with_pretraining):
    numbers = ["0", "10", "-2", "3e4", "5e-6", "-7e-8", "9.0", "1.e2", "-3.e4", "5.e-6", "-7.e-8", "9.0e0", "1.2e-3", "-4.5e-6", "-23", "0.3", "-6.4", "1e6", "-3e4", "2e-4", "-1e-2", "1.5e2", "-3.4e2", "5.1e-4", "-3.6e-2"]

    for number in numbers:
        print("Number:", number)

        brain.clear_connections()
        brain.deactivate_all_modules()
        brain.activate_module("chars.functions.conversion")
        brain.activate_module("digits.functions.conversion")
        brain.activate_module("strs.variables")
        brain.activate_module("strs.functions")
        brain.activate_module("strs.functions.conversion")
        brain.activate_module("symbols.functions.conversion")
        brain.activate_str(number)

        connections = brain.learn(number, depth = 10)

        print(brain.connection_str(connections[0]) + " -> " + str(brain.connection_output(connections[0])))

        try:
            brain.show2d(seed = 0, title = number, colorBy = "weight")
        except:
            pass

        brain.show3d(seed = 0, title = number, colorBy = "weight")

while (True):
    number = input("What is you number (for example: 3.1)? ")

    brain.clear_connections()
    brain.deactivate_all_modules()
    brain.activate_module("chars.functions.conversion")
    brain.activate_module("digits.functions.conversion")
    brain.activate_module("strs.variables")
    brain.activate_module("strs.functions")
    brain.activate_module("strs.functions.conversion")
    brain.activate_module("symbols.functions.conversion")
    brain.activate_str(number)

    connections = brain.learn(number, depth = 10)

    print(brain.connection_str(connections[0]) + " -> " + str(brain.connection_output(connections[0])))

    try:
        brain.show2d(seed = 0, title = number, colorBy = "weight")
    except:
        pass

    brain.show3d(seed = 0, title = number, colorBy = "weight")
