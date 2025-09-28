from brain import Brain
from connection import Connection
import ints
import json
import matplotlib.pyplot as plt
import ndarrays
import numpy as np
import urllib.request
import tuples

brain = Brain()
neuronIds = {}

neuronIds |= ndarrays.add(brain)
neuronIds |= tuples.add(brain)

brain.deactivate_all_modules()
brain.neurons[neuronIds["replace_ndarray"]].activated = True

url = urllib.request.urlopen("https://raw.githubusercontent.com/arcprize/ARC-AGI-2/refs/heads/main/data/training/0d3d703e.json")
data = json.loads(url.read().decode())

train = data["train"]

neuronIds |= ndarrays.add_value(brain, np.array([]), "input")

ids = {}

for n in range(0, len(train)):
    brain.clear_connections()

    input = np.array(train[n]["input"])
    output = np.array(train[n]["output"])

    plt.figure(0)
    plt.imshow(input)
    plt.figure(1)
    plt.imshow(output)
    plt.colorbar()
    #plt.show()

    brain.neurons[neuronIds["input"]].function = lambda input = input: input

    for k, v in ids.items():
        brain.remove(v)

    ids = {}

    for i in range(0, input.shape[0]):
        for j in range(0, input.shape[1]):
            ids |= tuples.add_value(brain, (i, j))

    for i in range(0, 10):
        ids |= ints.add_value(brain, i)

    print("input", input)
    print("output", output)

    answers = brain.learn(output, timeout = 4 * 1000, transform_best_into_neuron = False)

    while (not np.all(np.isclose(brain.connection_output(answers[0]), output))):
        #print(brain.connection_str(answers[0]), "->", brain.connection_output(answers[0]))
        #print(brain.connection_output(answers[0]) - output)
        brain.set_connections(answers)
        answers = brain.learn(output, timeout = 10 * 1000, transform_best_into_neuron = False)

    brain.set_connections(answers)

    print(brain.connection_str(answers[0]), "->", brain.connection_output(answers[0]))

    print(brain.connection_output(answers[0]) - output)

    brain.save("benchmark_arc-agi-0d3d703e_brain" + str(n) + ".bin")
