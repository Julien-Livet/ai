from brain import Brain
from connection import Connection
import ints
import json
import matplotlib.pyplot as plt
import ndarrays
import numpy as np
import os
import tuples
import urllib.request

brain = Brain()
neuronIds = {}

neuronIds |= ndarrays.add(brain)

brain.deactivate_all_modules()
brain.neurons[neuronIds["put_value_ndarray"]].activated = True

task = os.path.basename(__file__).replace("-work", "").replace(".py", "").replace("benchmark_arc-agi-", "")
url = urllib.request.urlopen("https://raw.githubusercontent.com/arcprize/ARC-AGI-2/refs/heads/main/data/training/" + task + ".json")
data = json.loads(url.read().decode())

train = data["train"]

neuronIds |= ndarrays.add_value(brain, np.array([]), "input")

for i in range(0, 10):
    neuronIds |= ints.add_value(brain, i)

tupleIds = {}

for n in range(0, len(train)):
    brain.clear_connections()

    input = np.array(train[n]["input"])
    output = np.array(train[n]["output"])

    plt.figure("input")
    plt.imshow(input)
    plt.colorbar()
    plt.figure("output")
    plt.imshow(output)
    plt.colorbar()
    #plt.show()

    for k, v in tupleIds.items():
        brain.remove(v)

    tupleIds = {}

    for i in range(0, input.shape[0]):
        for j in range(0, input.shape[1]):
            tupleIds |= tuples.add_value(brain, (i, j))

    brain.neurons[neuronIds["input"]].function = lambda input = input: input

    print("input", input)
    print("output", output)

    answers = brain.learn(output, max_conns = None, timeout = 20 * 1000, transform_best_into_neuron = False)

    while (not np.all(np.isclose(brain.connection_output(answers[0]), output))):
        print(brain.connection_str(answers[0]).replace("\\n", "").replace("\\", "").replace(" ", ""), "->", brain.connection_output(answers[0]))
        #print(brain.connection_output(answers[0]) - output)
        brain.set_connections(answers)
        answers = brain.learn(output, max_conns = None, timeout = 20 * 1000, transform_best_into_neuron = False)

    brain.set_connections(answers)

    print(brain.connection_str(answers[0]).replace("\\n", "").replace("\\", "").replace(" ", ""), "->", brain.connection_output(answers[0]))

    print(brain.connection_output(answers[0]) - output)

    brain.save("benchmark_arc-agi-" + task + "_brain" + str(n) + ".bin")
