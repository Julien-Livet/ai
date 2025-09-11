from brain import Brain
from connection import Connection
import ints
from neuron import Neuron

brain = Brain()
neuronIds = {}

neuronIds |= ints.add(brain)
neuronIds |= ints.add_value(brain, 18)

brain.activate_type(int, 1, False, False)

print(len(brain.connect(1)))
print(len(brain.connections))

#print(len(brain.connect(2)))
#print(len(brain.connections))

#print(len(brain.connect(1)))
#print(len(brain.connect(1)))
#print(len(brain.connections))

brain.show(seed = 0, levelColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])

brain.connections = brain.learn(0)

brain.show(seed = 0, levelColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])
