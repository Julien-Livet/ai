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

neuronIds |= chars.add(brain)
neuronIds |= digits.add(brain)
neuronIds |= strs.add(brain)
neuronIds |= symbols.add(brain)

neuronIds |= strs.add_value(brain, lambda: 0, "number")

while (True):
    number = input("What is you number (for example: 3.1)? ")

    brain.deactivate_all_modules()
    brain.deactivate_all_neurons()
    brain.activate_module("chars.functions.conversion")
    brain.activate_module("digits.functions.conversion")
    brain.activate_module("strs.variables")
    brain.activate_module("strs.functions")
    brain.neurons[neuronIds["lower_str"]].activated = False
    brain.neurons[neuronIds["upper_str"]].activated = False
    brain.activate_module("strs.functions.conversion")
    brain.activate_module("symbols.functions.conversion")
    brain.activate_str(number)
    
    brain.neurons[neuronIds["number"]].function = lambda number = number: number

    connections = brain.learn(number, depth = 10)

    print(brain.connection_str(connections[0]) + " -> " + str(brain.connection_output(connections[0])))

    try:
        brain.show2d(seed = 0, colorBy = "weight")
    except:
        pass

    brain.show3d(seed = 0, colorBy = "weight")
