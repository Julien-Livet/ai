from brain import Brain
from connection import Connection
import chars
import datetime
import digits
from neuron import Neuron
import os
import random
import strs
import symbols
import sympy

def process(brain: Brain, number: str):
    brain.clear_connections()
    brain.deactivate_all_modules()
    brain.activate_module("chars.functions.conversion")
    brain.activate_module("digits.functions.conversion")
    brain.activate_module("numbers.functions")
    brain.activate_module("strs.functions")
    brain.activate_module("strs.functions.conversion")
    brain.activate_module("symbols.functions.conversion")
    brain.activate_str(number)

    answers = brain.learn(number, depth = 10, compact_name = number, compact_module = "numbers.constants", module = "numbers.functions")

    if (isinstance(answers[0], Connection)):
        print(brain.connection_str(answers[0]), "->", brain.connection_output(answers[0]))
    else:
        print(brain.neuron_name(answers[0]), "->", answers[0].output())

    try:
        brain.show2d(seed = 0, title = number, colorBy = "weight")
    except:
        pass

    brain.show3d(seed = 0, title = number, colorBy = "weight")

brain = Brain()
with_pretraining = True
filename = "number_brain.bin"

if (os.path.exists(filename)):
    brain.load(filename)
else:
    chars.add(brain)
    digits.add(brain)
    strs.add(brain)
    symbols.add(brain)

    if (with_pretraining):
        numbers = ["10", "-2", "3.", "-4.", "3e4", "5e-6", "-7e-8", "9.0", "1.e2", "-3.e4", "5.e-6", "-7.e-8", "9.0e0", "1.2e-3",
                   "-4.5e-6", "-23", "0.3", "-6.4", "1e6", "-3e4", "2e-4", "-1e-2", "1.5e2", "-3.4e2", "5.1e-4", "-3.6e-2"]

        time = datetime.datetime.now()

        for number in numbers:
            print("Number:", number)

            process(brain, number)

        print("Pretraining done in", datetime.datetime.now() - time)

        brain.save(filename)

while (True):
    sp_number = None

    while (not isinstance(sp_number, sympy.Number)):
        number = input("What is your number (for example: 3.1)? ")

        sp_number = sympy.sympify(number)

    process(brain, number)
    brain.save(filename)
