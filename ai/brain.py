from brain_graph import BrainGraph
import colour
from connection import Connection
import math
import networkx as nx
from neuron import Neuron
import numpy as np
import random

def is_iterable(x) -> bool:
    try:
        it = iter(x)
    except TypeError as te:
        return False

    return True

class Brain:
    def __init__(self):
        self.neurons = {}
        self.inputTypesToNeurons = {}
        self.outputTypesToNeurons = {}
        self.neuronToIds = {}
        self.connections = set()
        self.graph = BrainGraph()
        self.originNeuronIds = []
        self.typesToConnections = {}

    def origin_neuron_ids_from_type(self, type):
        neurons_ids = []

        for id in self.originNeuronIds:
            if (self.neurons[id].outputType is type):
                neurons_ids.append(id)

        return neurons_ids

    def _add_neuron_input_types(self, neuron: Neuron):
        for type in neuron.inputTypes:
            l = self.inputTypesToNeurons.get(type, [])
            l.append(neuron)
            self.inputTypesToNeurons[type] = l

    def _add_neuron_output_type(self, neuron: Neuron):
        l = self.outputTypesToNeurons.get(neuron.outputType, [])
        l.append(neuron)
        self.outputTypesToNeurons[neuron.outputType] = l
        
    def add(self, neuron: Neuron):
        id = 0
        
        if (len(self.neurons)):
            id = list(self.neurons.keys())[-1] + 1
        
        self.neurons[id] = neuron

        self._add_neuron_input_types(neuron)
        self._add_neuron_output_type(neuron)

        self.neuronToIds[neuron] = id

        if (len(neuron.inputTypes) == 0):
            self.originNeuronIds.append(id)

        return id
        
    def remove(self, id: int):
        neuron = self.neurons[id]

        for k, v in self.inputTypesToNeurons.items():
            self.inputTypesToNeurons[k] = list(filter((neuron).__ne__, v))

        for k, v in self.outputTypesToNeurons.items():
            self.outputTypesToNeurons[k] = list(filter((neuron).__ne__, v))

        if (id in self.originNeuronIds):
            del self.originNeuronIds[self.originNeuronIds.index(id)]

        del self.neuronToIds[neuron]
        del self.neurons[id]

    def neuron_name(self, neuron: Neuron):
        if (neuron.name != ""):
            return neuron.name
        else:
            return self.neuronToIds[neuron]

    def draw_connection(self, pos: list, color, width: float, connection: Connection):
        for input in connection.inputs:
            if (type(input) is Neuron):
                self.graph.add_edge_arrow(pos[self.neuron_name(input)], pos[self.neuron_name(connection.neuron)],
                                          self.neuron_name(input) + "→" + self.neuron_name(connection.neuron),
                                          color, width)
            elif (type(input) is Connection):
                self.graph.add_edge_arrow(pos[self.neuron_name(input.neuron)], pos[self.neuron_name(connection.neuron)],
                                          self.neuron_name(input.neuron) + "→" + self.neuron_name(connection.neuron),
                                          color, width)

                self.draw_connection(pos, color, width + 1, input)

    def connection_output(self, connection: Connection):
        inputs = []

        try:
            for input in connection.inputs:
                if (type(input) is Neuron):
                    inputs.append(input.output())
                elif (type(input) is Connection):
                    inputs.append(self.connection_output(input))
        except:
            return None

        return connection.neuron.output(*inputs)

    def connection_len(self, connection: Connection):
        len = 0
        
        for input in connection.inputs:
            if (type(input) is Neuron):
                len = 1
            elif (type(input) is Connection):
                len += self.connection_len(input)

        return len

    def connection_str(self, connection: Connection):
        inputs = []

        for input in connection.inputs:
            if (type(input) is Neuron):
                inputs.append(input.output())
            elif (type(input) is Connection):
                inputs.append(self.connection_str(input))

        return self.neuron_name(connection.neuron) + "(" + str(inputs) + ")"

    def show(self,
             seed: int = None,
             length: float = 100.0,
             levelColors: list = [str(x) for x in list(colour.Color("green").range_to(colour.Color("blue"), 16))],
             connectionColors: list = (random.seed(0), ['#%06X' % random.randint(0, 0xFFFFFF) for _ in range(100)])[1]):
        self.graph = BrainGraph()

        minActivationLevel = 0
        maxActivationLevel = 0

        for id, neuron in self.neurons.items():
            maxActivationLevel = max(maxActivationLevel, neuron.activationLevel)
            minActivationLevel = min(minActivationLevel, neuron.activationLevel)
        
        if (not minActivationLevel and not maxActivationLevel):
            maxActivationLevel = 1

        positions = []
        colors = {}
        step = length ** (1 / 3)
        size = math.ceil(len(self.neurons) ** (1 / 3))

        for k in range(size):
            for j in range(size):
                for i in range(size):
                    index = i + size * (j + size * k)

                    if (index < len(self.neurons)):
                        neuron = self.neurons[index]
                        positions.append((i * step, j * step, k * step))

                        i = int((neuron.activationLevel - minActivationLevel) / (maxActivationLevel - minActivationLevel) * (len(levelColors) - 1))
                        colors[self.neuron_name(neuron)] = levelColors[i]

        if (seed != None):
            random.seed(seed)
            random.shuffle(positions)

        pos = {}

        for i in range(0, len(self.neurons)):
            pos[self.neuron_name(self.neurons[i])] = positions[i]

        self.graph.add_nodes(pos, colors)

        connections = list(self.connections)

        for i in range(0, len(self.connections)):
            self.draw_connection(pos, connectionColors[i % len(connectionColors)], 1, connections[i])
            
        self.graph.show()

    def activate_type(self, type, activationLevel: int = 0, previousLevels: bool = True, nextLevels: bool = True):
        neurons = self.inputTypesToNeurons.get(type, []) + self.outputTypesToNeurons.get(type, [])

        for neuron in neurons:
            self.activate(self.neuronToIds[neuron], activationLevel, previousLevels, nextLevels)

    def activate(self, id: int, activationLevel: int = 0, previousLevels: bool = True, nextLevels: bool = True):
        assert(id < len(self.neurons))

        self.neurons[id].activationLevel = activationLevel

        if (self.neurons[id].activated):
            return

        self.neurons[id].activated = True

        s = set(self.neurons[id].inputTypes)

        if (previousLevels):
            for type in self.neurons[id].inputTypes:
                for neuron in self.outputTypesToNeurons.get(type, []):
                    if (not neuron.activated):
                        self.activate(self.neuronToIds[neuron], activationLevel - 1)

        if (nextLevels):
            for neuron in self.inputTypesToNeurons.get(self.neurons[id].outputType, []):
                if (not neuron.activated):
                    self.activate(self.neuronToIds[neuron], activationLevel + 1)

    def _add_connection_type(self, connection):
        l = self.typesToConnections.get(connection.neuron.outputType, [])
        l.append(connection)
        self.typesToConnections[connection.neuron.outputType] = l
            
    def connect(self, depth: int = 1, number: int = math.inf):
        connections = set()
        new_connections = set()

        for i in range(0, depth):
            if (len(connections) > number):
                break

            newConnections = set()
            originTypes = {}

            for id in self.originNeuronIds:
                type = self.neurons[id].outputType
                l = originTypes.get(type, [])
                l.append(self.neurons[id])
                originTypes[type] = l
                    
            for connection in self.connections:
                type = connection.neuron.outputType
                l = originTypes.get(type, [])
                l.append(connection)
                originTypes[type] = l

            for k, v in self.neurons.items():
                inputsList = []
                add = True
                
                for type in v.inputTypes:
                    neurons = originTypes.get(type, [])
                    
                    if (not len(neurons)):
                        add = False
                        break

                    if (len(inputsList) == 0):
                        inputsList = [[x] for x in neurons]
                    else:
                        newList = []
                        
                        for inputs in inputsList:
                            for neuron in neurons:
                                newList.append(inputs + [neuron])
                            
                        inputsList = newList

                if (not add):
                    continue

                for inputs in inputsList:
                    newConnections.add(Connection(inputs, v))

            new_connections |= newConnections - self.connections.intersection(newConnections)

            connections |= newConnections
            self.connections |= newConnections

        for connection in new_connections:
            self._add_connection_type(connection)

        #return list(connections)
        return list(new_connections)

    def learn(self, value, name: str = "", transform_best_to_neuron: bool = True):
        connections = []
        
        for connection in self.typesToConnections.get(type(value), []):
            try:
                if (isinstance(value, str)):
                    if (value == self.connection_output(connection)):
                        connections.append(connection)
                elif (is_iterable(value)):
                    if (all(np.isclose(value, self.connection_output(connection)))):
                        connections.append(connection)
                else:
                    if (np.isclose(value, self.connection_output(connection))):
                        connections.append(connection)
            except:
                pass

        connections = sorted(connections, key = lambda x: self.connection_len(x))

        if (transform_best_to_neuron and len(connections)):
            connection = list(connections)[0]
            
            if (len(connection.origin_input_types()) == len(connection.inputs)):
                added = False

                for input in connection.inputs:
                    if (not (isinstance(input, Neuron) and len(input.inputTypes) == 0)):
                        added = True
                        break

                if (not added):
                    return connections

            def function(*args):
                def replace_inputs(connection, arg_iter):
                    vals = []

                    for input in connection.inputs:
                        if (isinstance(input, Neuron) and len(input.inputTypes) == 0):
                            vals.append(next(arg_iter))
                        elif (isinstance(input, Connection)):
                            vals.append(replace_inputs(input, arg_iter))

                    return connection.neuron.output(*vals)

                return replace_inputs(connection, iter(args))

            self.add(Neuron(function, name, connection.origin_input_types(), connection.neuron.outputType))

        return connections

    def save(self, filename: str):
        with open(filename, "wb") as f:
            dill.dump(self.neurons, f)
            dill.dump(self.connections, f)

    def load(self, filename: str):
        with open(filename, "rb") as f:
            self.neurons = dill.load(f)
            self.connections = dill.load(f)
            
        self.inputTypesToNeurons = {}
        self.outputTypesToNeurons = {}
        self.neuronToIds = {}
        self.graph = BrainGraph()
        self.originNeuronIds = []
        self.typesToConnections = {}
            
        for neuron in self.neurons:
            self._add_neuron_input_types(neuron)
            self._add_neuron_output_type(neuron)
            
            self.neuronToIds[neuron] = id

            if (len(neuron.inputTypes) == 0):
                self.originNeuronIds.append(id)

        for connection in self.connections:
            self._add_connection_type(connection)

    def clear_connections(self):
        self.connections = set()
        self.typesToConnections = {}

    def set_connections(self, connections: list[Connection]):
        self.connections = set(connections)
        self.typesToConnections = {}

        for connection in self.connections:
            self._add_connection_type(connection)
