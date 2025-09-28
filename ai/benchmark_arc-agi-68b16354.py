from brain import Brain
from connection import Connection
import json
import matplotlib.pyplot as plt
import ndarrays
import numpy as np
import urllib.request

brain = Brain()
neuronIds = {}

neuronIds |= ndarrays.add(brain)

brain.deactivate_all_modules()
brain.neurons[neuronIds["flipud_ndarray"]].activated = True

url = urllib.request.urlopen("https://raw.githubusercontent.com/arcprize/ARC-AGI-2/refs/heads/main/data/training/68b16354.json")
data = json.loads(url.read().decode())

train = data["train"]

neuronIds |= ndarrays.add_value(brain, np.array([]), "input")

ids = {}

for n in range(0, len(train)):
    brain.clear_connections()

    input = np.array(train[n]["input"])
    output = np.array(train[n]["output"])

    plt.figure("input")
    plt.imshow(input)
    plt.figure("output")
    plt.imshow(output)
    plt.colorbar()
    #plt.show()

    brain.neurons[neuronIds["input"]].function = lambda input = input: input

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

    brain.save("benchmark_arc-agi-68b16354_brain" + str(n) + ".bin")
