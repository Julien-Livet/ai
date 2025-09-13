from brain import Brain
from connection import Connection
import digits
import floats
import ints
from neuron import Neuron
import numpy as np
import random
import strs
import symbols
import sympy

brain = Brain()
neuronIds = {}

s = input("What is you expression (for example: x + y * z)?" )

expr = sympy.sympify(s)

seen = set()
variables = {}

for node in sympy.preorder_traversal(expr):
    if (isinstance(node, sympy.Symbol) and node not in seen):
        variables[node] = random.random()
        seen.add(node)

neuronIds |= digits.add(brain)
neuronIds |= ints.add(brain)
neuronIds |= floats.add(brain)
neuronIds |= strs.add(brain)
neuronIds |= symbols.add(brain)

values = []

for variable, value in variables.items():
    neuronIds |= floats.add_value(brain, lambda value = value: value, str(variable))

brain.deactivate_all_modules()
brain.activate_module("digits.constants")
brain.activate_module("digits.functions.conversion")
brain.activate_module("floats.operators.arithmetic")
brain.activate_module("floats.variables")
brain.activate_module("strs.functions")
brain.activate_module("strs.functions.conversion")
brain.activate_module("symbols.constants")
brain.activate_module("symbols.functions.conversion")

connections = brain.learn(expr.subs(variables), "expr", depth = 10)

print(variables, "->", expr.subs(variables))
print(brain.connection_str(connections[0]), "->", str(brain.connection_output(connections[0])))

try:
    brain.show2d(seed = 0, colorBy = "module")
except:
    pass

brain.show3d(seed = 0, colorBy = "module")
