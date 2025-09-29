from brain import Brain
import chars
from connection import Connection
import datetime
import digits
from neuron import Neuron
import os
import random
import strs
import symbols
import sympy

def process(brain: Brain, expression: str, module: str):
    brain.clear_connections()
    brain.deactivate_all_modules()
    brain.activate_module("chars.functions.conversion")
    brain.activate_module("digits.functions.conversion")
    brain.activate_module("expressions.functions")
    brain.activate_module("numbers.functions")
    brain.activate_module("strs.functions")
    brain.activate_module("strs.functions.conversion")
    brain.activate_module("symbols.functions.conversion")
    brain.activate_str(expression)

    answers = brain.learn(expression, depth = 10, module = module + ".functions", compact_module = module + ".constants", compact_name = expression)

    if (isinstance(answers[0], Connection)):
        print(brain.connection_str(answers[0]).replace("\n", "").replace("\\", "").replace(" ", ""), "->", brain.connection_output(answers[0]))
    else:
        print(brain.neuron_name(answers[0]), "->", answers[0].output())

    try:
        brain.show2d(seed = 0, title = expression, colorBy = "weight")
    except:
        pass

    brain.show3d(seed = 0, title = expression, colorBy = "weight")

brain = Brain()
with_pretraining = True
number_filename = "number_brain.bin"
expression_filename = "expression_brain.bin"
numbers = ["10", "-2", "3e4", "5e-6", "-7e-8", "9.0", "1.e2", "-3.e4", "5.e-6", "-7.e-8", "9.0e0",
           "1.2e-3", "-4.5e-6", "-23", "0.3", "-6.4", "1e6", "-3e4", "2e-4", "-1e-2", "1.5e2", "-3.4e2",
           "5.1e-4", "-3.6e-2"]
expressions = ["(-4.5)", "(-3)", "-3*2", "7*(-8)", "(-6)*(-7)", "2*x", "-3*x", "x+y", "2.*x", "3.1*x", "-4.*y", "-5.1*y", "3*x+y", "3.1*x+y", "2.3*x+5.4*y",
               "-2.1*x+4.5*y", "x*y", "1.2*x*y", "(x+y)", "(y+z)*z", "2*(z-x)", "1.2*(y-x)", "(x-y)*4.6", "(z-y)*(-3.8)"]

if (os.path.exists(expression_filename)):
    brain.load(expression_filename)
elif (os.path.exists(number_filename)):
    brain.load(number_filename)

    time = datetime.datetime.now()

    if (with_pretraining):
        for expression in expressions:
            print("Expression:", expression)

            process(brain, expression, "expressions")

        brain.save(expression_filename)

    print("Pretraining for expressions done in", datetime.datetime.now() - time)
else:
    chars.add(brain)
    digits.add(brain)
    strs.add(brain)
    symbols.add(brain)

    if (with_pretraining):
        time = datetime.datetime.now()

        for number in numbers:
            print("Number:", number)

            process(brain, number, "numbers")

        brain.save(number_filename)

        print("Pretraining for numbers done in", datetime.datetime.now() - time)

        time = datetime.datetime.now()

        for expression in expressions:
            print("Expression:", expression)

            process(brain, expression, "expressions")

        brain.save(expression_filename)

        print("Pretraining for expressions done in", datetime.datetime.now() - time)

while (True):
    sp_ok = False

    while (not sp_ok):
        expression = input("What is your expression (for example: x + y * z)? ")

        try:
            sympy.sympify(expression)
            sp_ok = True
        except:
            sp_ok = False

    process(brain, expression, "expressions")
    brain.save(expression_filename)
