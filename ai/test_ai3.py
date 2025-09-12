from brain import Brain
from connection import Connection
import ints
from neuron import Neuron

brain = Brain()
neuronIds = {}

x = 6
y = 5
z = 4

neuronIds |= ints.add(brain)

brain.deactivate_all_modules()
brain.activate_module("ints.operators.arithmetic")

neuronIds |= ints.add_value(brain, lambda: x, "x")
neuronIds |= ints.add_value(brain, lambda: y, "y")
neuronIds |= ints.add_value(brain, lambda: z, "z")

print(len(brain.connect(2)))
print(len(brain.connections))

#for connection in brain.connections:
#    print(brain.connection_str(connection) + " -> " + str(brain.connection_output(connection)))

brain.activate_type(int, 1, False, False)

try:
    brain.show2d(seed = 0, levelColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])
except:
    pass

#brain.show3d(seed = 0, levelColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])

connections = brain.associate(x * y + z, "mul_add")

print(brain.connection_str(connections[0]) + " -> " + str(brain.connection_output(connections[0])))

brain.clear_connections()

print(len(brain.connect(1)))
print(len(brain.connections))

#for connection in brain.connections:
#    print(brain.connection_str(connection) + " -> " + str(brain.connection_output(connection)))

connections = brain.associate(x * y + z)

print(brain.connection_str(connections[0]) + " -> " + str(brain.connection_output(connections[0])))
print(connections[0].origin_input_types())

brain.neurons[neuronIds["x"]].function = lambda: int(input("x? "))
brain.neurons[neuronIds["y"]].function = lambda: int(input("y? "))
brain.neurons[neuronIds["z"]].function = lambda: int(input("z? "))

print(brain.connection_output(connections[0]))
