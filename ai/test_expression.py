from brain import Brain
import chars
from connection import Connection
import digits
from neuron import Neuron
import numpy as np
import os
import random
import strs
import symbols

def process(brain: Brain, expression: str):
    brain.clear_connections()
    brain.deactivate_all_modules()
    brain.activate_module("chars.functions.conversion")
    brain.activate_module("digits.functions.conversion")
    brain.activate_module("floats.operators.arithmetic")
    brain.activate_module("floats.variables")
    brain.activate_module("strs.functions")
    brain.activate_module("strs.functions.conversion")
    brain.activate_module("symbols.functions.conversion")
    brain.activate_str(expression)

    connections = brain.learn(expression, depth = 10)

    print(brain.connection_str(connections[0]) + " -> " + str(brain.connection_output(connections[0])))

    try:
        brain.show2d(seed = 0, title = expression, colorBy = "weight")
    except:
        pass

    brain.show3d(seed = 0, title = expression, colorBy = "weight")

brain = Brain()
with_pretraining = True
number_filename = "number_brain.bin"
expression_filename = "expression_brain.bin"
numbers = [str(i) for i in range(10)] \
          + ["10", "-2", "3e4", "5e-6", "-7e-8", "9.0", "1.e2", "-3.e4", "5.e-6", "-7.e-8", "9.0e0",
             "1.2e-3", "-4.5e-6", "-23", "0.3", "-6.4", "1e6", "-3e4", "2e-4", "-1e-2", "1.5e2", "-3.4e2",
             "5.1e-4", "-3.6e-2"]
expressions = [chr(ord('a') + i) for i in range(26)] \
              + ["2*x", "-3*x", "x+y", "2.*x", "3.1*x", "-4.*y", "-5.1*y", "3*x+y", "3.1*x+y",
                 "-2.1*x+4.5*y", "x*y", "1.2*x*y", "(x+y)*z", "1.2*(x+y)", "(x-y)*4.6", "(x-y)*(-3.8)"]

if (os.path.exists(expression_filename)):
    brain.load(expression_filename)
elif (os.path.exists(number_filename)):
    brain.load(number_filename)

    if (with_pretraining):
        for expression in expressions:
            print("Expression:", expression)

            process(brain, expression)

        brain.save(expression_filename)
else:
    chars.add(brain)
    digits.add(brain)
    strs.add(brain)
    symbols.add(brain)

    if (with_pretraining):
        for number in numbers:
            print("Number:", number)

            process(brain, number)

        brain.save(number_filename)

        for expression in expressions:
            print("Expression:", expression)

            process(brain, expression)

        brain.save(expression_filename)

while (True):
    expression = input("What is you expression (for example: x + y * z)? ")

    process(brain, expression)

    brain.save(expression_filename)
