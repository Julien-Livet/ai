from brain import Brain
from connection import Connection
import ndarrays
from neuron import Neuron
import numpy as np

brain = Brain()
neuronIds = {}

x = np.array((1, 2, 3))
y = np.array((4, 5, 6))
z = np.array((7, 8, 9))

neuronIds["add_ndarray"] = brain.add(Neuron(ndarrays.add_ndarray, "add_ndarray"))
neuronIds["sub_ndarray"] = brain.add(Neuron(ndarrays.sub_ndarray, "sub_ndarray"))
neuronIds["mul_ndarray"] = brain.add(Neuron(ndarrays.mul_ndarray, "mul_ndarray"))
neuronIds["div_ndarray"] = brain.add(Neuron(ndarrays.div_ndarray, "div_ndarray"))
neuronIds |= ndarrays.add_value(brain, lambda: x, "x")
neuronIds |= ndarrays.add_value(brain, lambda: y, "y")
neuronIds |= ndarrays.add_value(brain, lambda: z, "z")

print(len(brain.connect(2)))
print(len(brain.connections))

#for connection in brain.connections:
#    print(brain.connection_str(connection) + " -> " + str(brain.connection_output(connection)))

brain.activate_type(np.ndarray, 1, False, False)

#brain.show2d(seed = 0, levelColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])
#brain.show3d(seed = 0, levelColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])

print(x * y + z)
connections = brain.learn(x * y + z, "mul_add")
brain.connections = set(connections)

print(brain.connection_str(connections[0]) + " -> " + str(brain.connection_output(connections[0])))
print(connections[0].origin_input_types())

brain.clear_connections()

print(len(brain.connect(1)))
print(len(brain.connections))

#for connection in brain.connections:
#    print(brain.connection_str(connection) + " -> " + str(brain.connection_output(connection)))

connections = brain.learn(x * y + z)

print(brain.connection_str(connections[0]) + " -> " + str(brain.connection_output(connections[0])))
print(connections[0].origin_input_types())

brain.neurons[neuronIds["x"]].function = lambda: int(input("x? "))
brain.neurons[neuronIds["y"]].function = lambda: int(input("y? "))
brain.neurons[neuronIds["z"]].function = lambda: int(input("z? "))

print(brain.connection_output(connections[0]))
