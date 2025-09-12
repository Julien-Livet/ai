import bools
from brain import Brain
import chars
from connection import Connection
import digits
import floats
import ints
import lists
import ndarrays
from neuron import Neuron
import numpy as np
import random
import sets
import strs
import tuples

brain = Brain()
neuronIds = {}

neuronIds |= bools.add(brain)
neuronIds |= chars.add(brain)
neuronIds |= digits.add(brain)
neuronIds |= floats.add(brain)
neuronIds |= ints.add(brain)
neuronIds |= lists.add(brain)
neuronIds |= ndarrays.add(brain)
neuronIds |= sets.add(brain)
neuronIds |= strs.add(brain)
neuronIds |= tuples.add(brain)

activationExample = 2

match (activationExample):
    case 0: #First example
        brain.activate_type(bool, 0, False, False)
        brain.activate_type(chars.Char, 1, False, False)
        brain.activate_type(digits.Digit, 2, False, False)
        brain.activate_type(float, 3, False, False)
        brain.activate_type(int, 4, False, False)
        brain.activate_type(list, 5, False, False)
        brain.activate_type(np.ndarray, 6, False, False)
        brain.activate_type(set, 7, False, False)
        brain.activate_type(str, 8, False, False)
        brain.activate_type(tuple, 9, False, False)

    case 1: #Second example
        for i in range(0, len(brain.originNeuronIds)):
            brain.activate(brain.originNeuronIds[i], 1, False, False)

    case 2: #Third example
        neuronIds |= floats.add_value(brain, 19.6)
        neuronIds |= ints.add_value(brain, 18)
        neuronIds |= strs.add_value(brain, "Julien")
        neuronIds |= strs.add_value(brain, "test")
        brain.remove(neuronIds["test"])

        for id in brain.origin_neuron_ids_from_type(bool):
            brain.activate(id, 1, False, False)

        for id in brain.origin_neuron_ids_from_type(chars.Char):
            brain.activate(id, 2, False, False)

        for id in brain.origin_neuron_ids_from_type(digits.Digit):
            brain.activate(id, 3, False, False)

        for id in brain.origin_neuron_ids_from_type(float):
            brain.activate(id, 4, False, False)

        for id in brain.origin_neuron_ids_from_type(int):
            brain.activate(id, 5, False, False)
            
        for id in brain.origin_neuron_ids_from_type(str):
            brain.activate(id, 6, False, False)

connectionExample = 0

match (connectionExample):
    case 0: #First example
        random.seed(0)

        for i in range(10):
            number = f"{random.randint(100, 999):03}"

            connection0 = Connection([brain.neurons[neuronIds[number[2]]]], brain.neurons[neuronIds["digit_to_str"]])
            connection1 = Connection([brain.neurons[neuronIds[number[1]]]], brain.neurons[neuronIds["digit_to_str"]])
            connection2 = Connection([brain.neurons[neuronIds[number[0]]]], brain.neurons[neuronIds["digit_to_str"]])

            connectionAdd1 = Connection([connection0, connection1], brain.neurons[neuronIds["add_str"]])
            connectionAdd2 = Connection([connectionAdd1, connection2], brain.neurons[neuronIds["add_str"]])

            connectionInt = Connection([connectionAdd2], brain.neurons[neuronIds["str_to_int"]])

            brain.add_connection(connectionInt)

            print(brain.connection_output(connectionInt))

    case 1: #Second example
        print(len(brain.connect(2)))

#brain.show2d(seed = 0, levelColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])
brain.show3d(seed = 0, levelColors = ["red", "green", "blue", "yellow", "cyan", "magenta", "purple", "brown", "orange", "gold", "indigo", "black", "white"])
