from brain import Brain
from connection import Connection
import ndarrays
from neuron import Neuron
import numpy as np

brain = Brain()
neuronIds = {}

w = np.array((-2, -1, 0))
x = np.array((1, 2, 3))
y = np.array((4, 5, 6))
z = np.array((7, 8, 9))

neuronIds |= ndarrays.add(brain)

#brain.deactivate_all_modules()
#brain.activate_module("ndarrays.operators.arithmetic")

example = 0

neuronIds |= ndarrays.add_value(brain, lambda: w, "w")
neuronIds |= ndarrays.add_value(brain, lambda: x, "x")
neuronIds |= ndarrays.add_value(brain, lambda: y, "y")
neuronIds |= ndarrays.add_value(brain, lambda: z, "z")

#print("Neuron number", len(brain.neurons))

match (example):
    case 0:
        connections = brain.learn(x + y * z, "mul_add", depth = 3)

    case 1:
        connections = brain.learn(w * x + y * z, "mul_add", depth = 3)

print(brain.connection_str(connections[0]) + " -> " + str(brain.connection_output(connections[0])))
print(connections[0].origin_input_types())

brain.clear_connections()

match (example):
    case 0:
        connections = brain.learn(x + y * z, depth = 1)

    case 1:
        connections = brain.learn(w * x + y * z, depth = 1)

print(brain.connection_str(connections[0]) + " -> " + str(brain.connection_output(connections[0])))
print(connections[0].origin_input_types())

try:
    brain.show2d(seed = 0, levelColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])
except:
    pass

#brain.show3d(seed = 0, levelColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])

brain.neurons[neuronIds["w"]].function = lambda: int(input("w? "))
brain.neurons[neuronIds["x"]].function = lambda: int(input("x? "))
brain.neurons[neuronIds["y"]].function = lambda: int(input("y? "))
brain.neurons[neuronIds["z"]].function = lambda: int(input("z? "))

print(brain.connection_output(connections[0]))
