from brain import Brain
from connection import Connection
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
brain.neurons[neuronIds["zeros_ndarray"]].activated = True
brain.neurons[neuronIds["put_ndarray"]].activated = True

task = os.path.basename(__file__).replace("-work", "").replace(".py", "").replace("benchmark_arc-agi-", "")
url = urllib.request.urlopen("https://raw.githubusercontent.com/arcprize/ARC-AGI-2/refs/heads/main/data/training/" + task + ".json")
data = json.loads(url.read().decode())

train = data["train"]

neuronIds |= tuples.add_value(brain, (0, ), "shape_output")

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

    s = set(input.flatten())
    submatrices = []

    for i in s:
        if (not i):
            continue

        mask = (input == i)
        rows = np.any(mask, axis = 1)
        cols = np.any(mask, axis = 0)

        rmin, rmax = np.where(rows)[0][[0, -1]]
        cmin, cmax = np.where(cols)[0][[0, -1]]

        submatrices.append(input[rmin:rmax + 1, cmin:cmax + 1])

    brain.neurons[neuronIds["shape_output"]].function = lambda output = output: output.shape

    for k, v in ids.items():
        brain.remove(v)

    shapes = set()

    for m in submatrices:
        shapes.add(m.shape)

    ids = {}

    indices = set()

    for s in shapes:
        ids |= ndarrays.add_value(brain, np.zeros(s))

        for i in range(0, input.shape[0] - s[0] + 1):
            for j in range(0, input.shape[1] - s[1] + 1):
                indices.add((i, j))

    for idx in indices:
        ids |= tuples.add_value(brain, idx)

    for m in submatrices:
        ids |= ndarrays.add_value(brain, m)

    print("input", input)
    print("output", output)

    answers = brain.learn(output, timeout = 2 * 1000, transform_best_into_neuron = False)

    while (not np.all(np.isclose(brain.connection_output(answers[0]), output))):
        #print(brain.connection_str(answers[0]).replace("\n", "").replace("\\", "").replace(" ", ""), "->", brain.connection_output(answers[0]))
        #print(brain.connection_output(answers[0]) - output)
        brain.set_connections(answers)
        answers = brain.learn(output, timeout = 2 * 1000, transform_best_into_neuron = False)

    brain.set_connections(answers)

    print(brain.connection_str(answers[0]).replace("\n", "").replace("\\", "").replace(" ", ""), "->", brain.connection_output(answers[0]))

    print(brain.connection_output(answers[0]) - output)

    brain.save("benchmark_arc-agi-" + task + "_brain" + str(n) + ".bin")
