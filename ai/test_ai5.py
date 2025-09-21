from brain import Brain
from connection import Connection
import ndarrays
from neuron import Neuron
import numpy as np

brain = Brain()
neuronIds = {}

w = np.array((-2, 0, -1))
x = np.array((-1, 2, 3))
y = np.array((4, -6, 5))
z = np.array((9, 8, -7))

neuronIds |= ndarrays.add(brain)

brain.deactivate_all_modules()
brain.activate_module("ndarrays.operators.arithmetic")

example = 0

neuronIds |= ndarrays.add_value(brain, lambda: w, "w")
neuronIds |= ndarrays.add_value(brain, lambda: x, "x")
neuronIds |= ndarrays.add_value(brain, lambda: y, "y")
neuronIds |= ndarrays.add_value(brain, lambda: z, "z")

#print("Neuron number", len(brain.neurons))

match (example):
    case 0:
        connections = brain.learn(x + y * z, "mul_add", depth = 2)

    case 1:
        connections = brain.learn(w * x + y * z, "mul_add", depth = 2)

print(brain.connection_str(connections[0]) + " -> " + str(brain.connection_output(connections[0])))
print(connections[0].origin_input_types())

try:
    brain.show2d(seed = 0, colorBy = "module", neuronColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])
except:
    pass

brain.show3d(seed = 0, colorBy = "module", neuronColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])

brain.clear_connections()

w += 1
x += 1
y += 1
z += 1

match (example):
    case 0:
        connections = brain.learn(x + y * z, depth = 1)

    case 1:
        connections = brain.learn(w * x + y * z, depth = 1)

print(brain.connection_str(connections[0]) + " -> " + str(brain.connection_output(connections[0])))
print(connections[0].origin_input_types())

try:
    brain.show2d(seed = 0, colorBy = "module", neuronColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])
except:
    pass

brain.show3d(seed = 0, colorBy = "module", neuronColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])

brain.neurons[neuronIds["w"]].function = lambda: int(input("w? "))
brain.neurons[neuronIds["x"]].function = lambda: int(input("x? "))
brain.neurons[neuronIds["y"]].function = lambda: int(input("y? "))
brain.neurons[neuronIds["z"]].function = lambda: int(input("z? "))

print(brain.connection_output(connections[0]))
