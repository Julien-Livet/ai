from bs4 import BeautifulSoup
from brain import Brain
from connection import Connection
import datetime
import ints
import json
import lists
import matplotlib.pyplot as plt
from ndarrays import Region
import ndarrays
from neuron import Neuron
import numpy as np
import os
import re
import requests
import tuples
import urllib.request

tasks = []

for x in os.listdir():
    if (x.endswith(".py") and "benchmark_arc-agi-" in x):
        tasks.append(x.replace(".py", "").replace("benchmark_arc-agi-", ""))

"""
url = 'https://github.com/arcprize/ARC-AGI-2/tree/main/data/training'

result = requests.get(url)

soup = BeautifulSoup(result.text, 'html.parser')
tasks = re.findall(r'"name":"(.*?)\.json"', result.text)

del tasks[0]
"""

count = 0
globalTime = datetime.datetime.now()

for ntask, task in enumerate(tasks):
    brain = Brain()
    neuronIds = {}

    neuronIds |= ndarrays.add(brain)

    brain.deactivate_all_modules()

    neuronIds |= ndarrays.add_value(brain, np.array([]), "input")
    neuronIds |= tuples.add_value(brain, (0, ), "shape_input")
    neuronIds |= tuples.add_value(brain, (0, ), "shape_output")

    brain.neurons[neuronIds["zeros_ndarray"]].activated = True
    brain.neurons[neuronIds["tile_ndarray"]].activated = True
    brain.neurons[neuronIds["fliplr_ndarray"]].activated = True
    brain.neurons[neuronIds["flipud_ndarray"]].activated = True
    brain.neurons[neuronIds["place_region_ndarray"]].activated = True
    brain.neurons[neuronIds["hline_ndarray"]].activated = True
    brain.neurons[neuronIds["vline_ndarray"]].activated = True
    brain.neurons[neuronIds["hlineleft_ndarray"]].activated = True
    brain.neurons[neuronIds["hlineright_ndarray"]].activated = True
    brain.neurons[neuronIds["vlineup_ndarray"]].activated = True
    brain.neurons[neuronIds["vlinedown_ndarray"]].activated = True
    brain.neurons[neuronIds["fill_region_at_ndarray"]].activated = True
    brain.neurons[neuronIds["fill_region2_at_ndarray"]].activated = True
    brain.neurons[neuronIds["replace_ndarray"]].activated = True
    brain.neurons[neuronIds["put_ndarray"]].activated = True
    brain.neurons[neuronIds["put_value_ndarray"]].activated = True
    brain.neurons[neuronIds["fill_region_ndarray"]].activated = True
    brain.neurons[neuronIds["bitwise_or_ndarray"]].activated = True
    brain.neurons[neuronIds["bitwise_and_ndarray"]].activated = True
    brain.neurons[neuronIds["bitwise_xor_ndarray"]].activated = True
    brain.neurons[neuronIds["invert_ndarray"]].activated = True
    brain.neurons[neuronIds["dotsegment_ndarray"]].activated = True
    brain.neurons[neuronIds["rot90_ndarray"]].activated = True

    print("Task #" + str(ntask) + "/" + str(len(tasks) - 1) + " " + task + ":")

    url = urllib.request.urlopen("https://raw.githubusercontent.com/arcprize/ARC-AGI-2/refs/heads/main/data/training/" + task + ".json")
    data = json.loads(url.read().decode())

    train = data["train"]

    ids = {}

    taskTime = datetime.datetime.now()

    for n in range(0, len(train)):
        print("Subtask #" + str(n) + "/" + str(len(train) - 1) + ":")

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

        for k, v in ids.items():
            brain.remove(v)

        ids = {}

        for i in set(input.flatten().tolist() + output.flatten().tolist()):
            ids |= ints.add_value(brain, i)

        s = set()

        for i in range(0, input.shape[0]):
            for j in range(0, input.shape[1]):
                r = sorted(ndarrays.region_ndarray((i, j), input).indices)

                if (not tuple(r) in s):
                    s.add(tuple(r))

        for r in s:
            name = str(r)
            ids[name] = brain.add(Neuron(lambda r = r: Region(r), name, outputType = Region, module = "ndarrays.variables"))
            ids |= ndarrays.add_value(brain, ndarrays.matrix_region_ndarray(Region(r), input))

        """
        s = set()

        for i in range(0, output.shape[0]):
            for j in range(0, output.shape[1]):
                r = sorted(ndarrays.region_ndarray((i, j), output).indices)

                if (not tuple(r) in s):
                    s.add(tuple(r))

        for r in s:
            name = str(r)
            ids[name] = brain.add(Neuron(lambda r = r: Region(r), name, outputType = ndarrays.Region, module = "ndarrays.variables"))
            ids |= ndarrays.add_value(brain, ndarrays.matrix_region_ndarray(Region(r), output))
        """

        for i in range(0, output.shape[0]):#for i in range(0, max(input.shape[0], output.shape[0])):
            for j in range(0, output.shape[1]):#for j in range(0, max(input.shape[1], output.shape[1])):
                ids |= tuples.add_value(brain, (i, j))

        for i in range(0, max(input.shape[0], output.shape[0])):
            ids |= ints.add_value(brain, i)

        ids |= tuples.add_value(brain, tuple(np.array(output.shape) / np.array(input.shape)))

        brain.neurons[neuronIds["input"]].function = lambda input = input: input
        brain.neurons[neuronIds["shape_input"]].function = lambda input = input: input.shape
        brain.neurons[neuronIds["shape_output"]].function = lambda output = output: output.shape

        #print("input", input)
        #print("output", output)

        timeout = 10 * 60 * 1000
        time = datetime.datetime.now()
        passed = True

        learnTimeout = 2 * 1000
        previousOutput = np.array([])
        answers = []

        while (previousOutput.shape != output.shape or not np.all(np.isclose(previousOutput, output))):
            if (datetime.datetime.now() - time > datetime.timedelta(milliseconds = timeout)):
                passed = False
                break

            if (len(answers)):
                #print(brain.connection_str(answers[0]).replace("\n", "").replace("\\", "").replace(" ", ""), "->", brain.connection_output(answers[0]))
                pass

            brain.set_connections(answers)
            brain.neuronTimeout = learnTimeout / 8
            answers = brain.learn(output, max_conns = None, timeout = learnTimeout, transform_best_into_neuron = False)

            newOutput = brain.connection_output(answers[0])

            if (previousOutput.shape != newOutput.shape or np.all(np.isclose(previousOutput, newOutput))):
                #learnTimeout += 1000
                learnTimeout *= 2
            #else:
            #    learnTimeout = 2 * 1000
            elif (learnTimeout > 1000):
                #learnTimeout -= 1000
                learnTimeout /= 2

            previousOutput = newOutput

        #print(brain.connection_str(answers[0]).replace("\n", "").replace("\\", "").replace(" ", ""), "->", brain.connection_output(answers[0]))

        suffix = "-passed" if passed else "-failed"

        brain.save("benchmark_arc-agi-" + task + "_brain" + str(n) + suffix + ".bin")

        if (not passed):
            break

        print("Subtask passed in " + str(datetime.datetime.now() - time))

        brain.set_connections(answers)

    print("Task passed in " + str(datetime.datetime.now() - taskTime) if passed else "Task failed")

    if (passed):
        count += 1

print(str(count) + "/" + str(len(tasks)) + " tasks passed (" + str(count / len(tasks) * 100) + "%) in " + str(datetime.datetime.now() - globalTime))
