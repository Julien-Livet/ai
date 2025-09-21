from brain import Brain
from connection import Connection
import digits
import ndarrays
import numpy as np
from neuron import Neuron

brain = Brain()
neuronIds = {}

neuronIds |= digits.add(brain)
neuronIds |= ndarrays.add(brain)

def syracuse(n: int):
    return 3 * n + 1 if n % 2 else n // 2

numbers = [14]

for i in range(0, 5):
    numbers.append(syracuse(numbers[-1]))

numbers = np.array(numbers)

neuronIds |= ndarrays.add_value(brain, numbers[:-1], "numbers")

brain.deactivate_all_modules()
brain.activate_module("ndarrays.operators.arithmetic")

for module in brain.modules:
    if ("digits" in module):
        brain.activate_module(module)

brain.neurons[neuronIds["numbers"]].activated = True

connections = list()

conns = brain.learn(numbers[:-1] % 2, compact_name = "f1", compact_module = "syracuse.constants", module = "syracuse.functions", transform_best_into_neuron = False)
assert(len(conns))
connections += conns

brain.clear_connections()
conns = brain.learn(numbers[:-1] // 2, compact_name = "f2", compact_module = "syracuse.constants", module = "syracuse.functions", transform_best_into_neuron = False)
assert(len(conns))
connections += conns

brain.clear_connections()
conns = brain.learn(3 * numbers[:-1], compact_name = "f3", compact_module = "syracuse.constants", module = "syracuse.functions", transform_best_into_neuron = False)
assert(len(conns))
connections += conns

conns = brain.learn(3 * numbers[:-1] + 1, compact_name = "f4", compact_module = "syracuse.constants", module = "syracuse.functions", transform_best_into_neuron = False)
assert(len(conns))
connections += conns

brain.clear_connections()
brain.connections = set(connections)
brain.deactivate_all_modules()
brain.activate_module("ndarrays.operators.logical")

answers = brain.learn(numbers[1:], compact_name = "syracuse", compact_module = "syracuse.constants", module = "syracuse.functions")

print(brain.connection_str(answers[0]), "->", brain.connection_output(answers[0]))

brain.set_connections(answers)

try:
    brain.show2d(seed = 0, title = "Syracuse suite", colorBy = "weight")
except:
    pass

brain.show3d(seed = 0, title = "Syracuse suite", colorBy = "weight")
