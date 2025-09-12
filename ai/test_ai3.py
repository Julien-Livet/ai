from brain import Brain
from connection import Connection
import ints
from neuron import Neuron

brain = Brain()
neuronIds = {}

x = 6
y = 5
z = 4

neuronIds["add_int"] = brain.add(Neuron(ints.add_int, "add_int"))
neuronIds["sub_int"] = brain.add(Neuron(ints.sub_int, "sub_int"))
neuronIds["mul_int"] = brain.add(Neuron(ints.mul_int, "mul_int"))
neuronIds["div_int"] = brain.add(Neuron(ints.div_int, "div_int"))
neuronIds |= ints.add_value(brain, lambda: x, "x")
neuronIds |= ints.add_value(brain, lambda: y, "y")
neuronIds |= ints.add_value(brain, lambda: z, "z")

print(len(brain.connect(2)))
print(len(brain.connections))

#for connection in brain.connections:
#    print(brain.connection_str(connection) + " -> " + str(brain.connection_output(connection)))

brain.activate_type(int, 1, False, False)

#brain.show2d(seed = 0, levelColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])
#brain.show3d(seed = 0, levelColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])

connections = brain.learn(x * y + z, "mul_add")

print(brain.connection_str(connections[0]) + " -> " + str(brain.connection_output(connections[0])))

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
