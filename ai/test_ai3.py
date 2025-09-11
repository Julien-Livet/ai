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
neuronIds |= ints.add_value(brain, lambda: x, "x")
neuronIds |= ints.add_value(brain, lambda: y, "y")
neuronIds |= ints.add_value(brain, lambda: z, "z")

print(len(brain.connect(2)))
print(len(brain.connections))

#for connection in brain.connections:
#    print(brain.connection_str(connection) + " -> " + str(brain.connection_output(connection)))

brain.activate_type(int, 1, False, False)

#brain.show(seed = 0, levelColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])

brain.connections = brain.learn(x * y + z)

connections = list(brain.connections)
print(brain.connection_str(connections[0]) + " -> " + str(brain.connection_output(connections[0])))

print(brain.neuron_name(brain.neurons[neuronIds["x"]]))
print(brain.neuron_name(brain.neurons[neuronIds["y"]]))
print(brain.neuron_name(brain.neurons[neuronIds["z"]]))

brain.neurons[neuronIds["x"]].function = lambda: int(input("x? "))
brain.neurons[neuronIds["y"]].function = lambda: int(input("y? "))
brain.neurons[neuronIds["z"]].function = lambda: int(input("z? "))

print(brain.connection_output(brain.connections[0]))
