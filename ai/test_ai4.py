from brain import Brain
from connection import Connection
import ndarrays
from neuron import Neuron
import numpy as np

brain = Brain()
neuronIds = {}

x = np.array((1, -2, 3))
y = np.array((-4, 5, 6))
z = np.array((7, 8, -9))

neuronIds |= ndarrays.add(brain)

brain.deactivate_all_modules()
brain.activate_module("ndarrays.operators.arithmetic")

neuronIds |= ndarrays.add_value(brain, lambda: x, "x")
neuronIds |= ndarrays.add_value(brain, lambda: y, "y")
neuronIds |= ndarrays.add_value(brain, lambda: z, "z")

print(len(brain.connect(2)))
print(len(brain.connections))

#for connection in brain.connections:
#    print(brain.connection_str(connection) + " -> " + str(brain.connection_output(connection)))

brain.activate_type(np.ndarray, 1, False, False)

try:
    brain.show2d(seed = 0, levelColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])
except:
    pass

#brain.show3d(seed = 0, levelColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])

print(x * y + z)
connections = brain.associate(x * y + z, "mul_add")
brain.connections = set(connections)

print(brain.connection_str(connections[0]) + " -> " + str(brain.connection_output(connections[0])))
print(connections[0].origin_input_types())

brain.clear_connections()

print(len(brain.connect(1)))
print(len(brain.connections))

#for connection in brain.connections:
#    print(brain.connection_str(connection) + " -> " + str(brain.connection_output(connection)))

x += 1
y += 1
z += 1

connections = brain.associate(x * y + z)

print(brain.connection_str(connections[0]) + " -> " + str(brain.connection_output(connections[0])))
print(connections[0].origin_input_types())

brain.neurons[neuronIds["x"]].function = lambda: int(input("x? "))
brain.neurons[neuronIds["y"]].function = lambda: int(input("y? "))
brain.neurons[neuronIds["z"]].function = lambda: int(input("z? "))

print(brain.connection_output(connections[0]))
