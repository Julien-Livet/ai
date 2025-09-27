from brain import Brain
from connection import Connection
import digits
import ints
import json
import matplotlib.pyplot as plt
import ndarrays
import numpy as np
import urllib.request
import tuples

brain = Brain()
neuronIds = {}

#neuronIds |= digits.add(brain)
neuronIds |= ints.add(brain)
neuronIds |= ndarrays.add(brain)
neuronIds |= tuples.add(brain)

brain.deactivate_all_modules()
brain.neurons[neuronIds["tile_ndarray"]].activated = True
brain.neurons[neuronIds["fliplr_ndarray"]].activated = True
brain.neurons[neuronIds["floordiv_ndarray"]].activated = True
brain.neurons[neuronIds["put_ndarray"]].activated = True

url = urllib.request.urlopen("https://raw.githubusercontent.com/arcprize/ARC-AGI-2/refs/heads/main/data/training/00576224.json")
data = json.loads(url.read().decode())

train = data["train"]

input = np.array(train[0]["input"])
output = np.array(train[0]["output"])

plt.figure(0)
plt.imshow(input)
plt.figure(1)
plt.imshow(output)
plt.colorbar()
#plt.show()
#exit()

neuronIds |= ndarrays.add_value(brain, input, "input")
neuronIds |= ndarrays.add_value(brain, np.array(input.shape), "shape_input")
neuronIds |= ndarrays.add_value(brain, np.array(output.shape), "shape_output")

for i in range(0, output.shape[0] - input.shape[0] + 1, input.shape[0]):
    for j in range(0, output.shape[1] - input.shape[1] + 1, input.shape[1]):
        tuples.add_value(brain, (i, j))

print("input", input)
print("output", output)

answers = brain.learn(output, timeout = 4 * 1000)

while (not np.all(np.isclose(brain.connection_output(answers[0]), output))):
    #print(brain.connection_str(answers[0]), "->", brain.connection_output(answers[0]))
    #print(brain.connection_output(answers[0]) - output)
    brain.set_connections(answers)
    answers = brain.learn(output, timeout = 10 * 1000)

print(brain.connection_str(answers[0]), "->", brain.connection_output(answers[0]))

print(brain.connection_output(answers[0]) - output)

for i in range(1, len(train)):
    input = np.array(train[i]["input"])
    output = np.array(train[i]["output"])

    brain.neurons[neuronIds["input"]].function = lambda input = input: input
    brain.neurons[neuronIds["shape_input"]].function = lambda input = input: np.array(input.shape)
    brain.neurons[neuronIds["shape_output"]].function = lambda output = output: np.array(output.shape)

    print(brain.connection_output(answers[0]) - output)
