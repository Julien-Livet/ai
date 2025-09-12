from brain import Brain
import chars
from connection import Connection
import digits
import floats
import ints
import lists
from neuron import Neuron
import strs

brain = Brain()
neuronIds = {}

neuronIds |= digits.add(brain)
neuronIds |= strs.add(brain)

#brain.neurons[neuronIds["add_str"]].activated = True
#brain.activate(neuronIds["add_str"])

brain.activate(neuronIds["1"])
brain.activate(neuronIds["0"])
#brain.activate_type(digits.Digit, 0, False, False)

connection0 = Connection([brain.neurons[neuronIds["0"]]], brain.neurons[neuronIds["digit_to_str"]])
connection1 = Connection([brain.neurons[neuronIds["1"]]], brain.neurons[neuronIds["digit_to_str"]])
connection3 = Connection([brain.neurons[neuronIds["3"]]], brain.neurons[neuronIds["digit_to_str"]])

connectionAdd1 = Connection([connection1, connection0], brain.neurons[neuronIds["add_str"]])
connectionAdd2 = Connection([connectionAdd1, connection3], brain.neurons[neuronIds["add_str"]])

connectionInt = Connection([connectionAdd2], brain.neurons[neuronIds["str_to_int"]])

brain.connections.add(connectionInt)

print(brain.connection_output(connectionInt))

#brain.show2d()
brain.show3d()
