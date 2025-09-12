from brain import Brain
from connection import Connection
import strs
from neuron import Neuron

brain = Brain()
neuronIds = {}

x = "Hello "
name = "world"
z = "! How are you?"

neuronIds |= strs.add(brain)
neuronIds |= strs.add_value(brain, lambda: x, "x")
neuronIds |= strs.add_value(brain, lambda: name, "name")
neuronIds |= strs.add_value(brain, lambda: z, "z")

print(len(brain.connect(2)))
print(len(brain.connections))

#for connection in brain.connections:
#    print(brain.connection_str(connection) + " -> " + str(brain.connection_output(connection)))

brain.activate_type(str, 1, False, False)

try:
    brain.show2d(seed = 0, levelColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])
except:
    pass

#brain.show3d(seed = 0, levelColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])

connections = brain.associate(x + name + z)

print(brain.connection_str(connections[0]) + " -> " + str(brain.connection_output(connections[0])))

brain.neurons[neuronIds["name"]].function = lambda: input("What is your name? ")

print(brain.connection_output(connections[0]))
