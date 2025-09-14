import colour
from connection import Connection
import heapq
import itertools
import math
from neuron import Neuron
import numpy as np
import random
import textdistance

def is_iterable(x) -> bool:
    try:
        it = iter(x)
    except TypeError as te:
        return False

    return True

def heuristic(val, target):
    if (isinstance(val, str) and isinstance(target, str)):
        return textdistance.levenshtein.distance(val, target)

    try:
        return np.linalg.norm(np.subtract(val, target))
    except:
        try:
            return abs(hash(val) - hash(target))
        except:
            return 999.0

def canonicalize_for_visit(val):
    if isinstance(val, np.ndarray):
        if val.size == 1:
            return float(val.item())
        return ("ndarray", val.shape, hash(val.tobytes()))
    try:
        hash(val)
        return val
    except TypeError:
        return repr(val)

class Brain:
    def __init__(self):
        self.neurons = {}
        self.inputTypesToIds = {}
        self.outputTypesToIds = {}
        self.neuronToIds = {}
        self.connections = set()
        self.originNeuronIds = []
        self.typesToConnections = {}
        self.modules = {}

    def origin_neuron_ids_from_type(self, type):
        neurons_ids = []

        for id in self.originNeuronIds:
            if (self.neurons[id].outputType is type):
                neurons_ids.append(id)

        return neurons_ids

    def _add_neuron_input_types(self, id: int):
        neuron = self.neurons[id]

        for type in neuron.inputTypes:
            l = self.inputTypesToIds.get(type, [])
            l.append(id)
            self.inputTypesToIds[type] = l

    def _add_neuron_output_type(self, id: int):
        neuron = self.neurons[id]

        l = self.outputTypesToIds.get(neuron.outputType, [])
        l.append(id)
        self.outputTypesToIds[neuron.outputType] = l

    def add(self, neuron: Neuron):
        id = 0

        if (len(self.neurons)):
            id = list(self.neurons.keys())[-1] + 1

        self.neurons[id] = neuron

        self._add_neuron_input_types(id)
        self._add_neuron_output_type(id)

        self.neuronToIds[neuron] = id

        if (len(neuron.inputTypes) == 0):
            self.originNeuronIds.append(id)

        if (not neuron.module in self.modules):
            self.modules[neuron.module] = True

        return id

    def remove(self, id: int):
        neuron = self.neurons[id]

        for k, v in self.inputTypesToIds.items():
            self.inputTypesToIds[k] = list(filter((neuron).__ne__, v))

        for k, v in self.outputTypesToIds.items():
            self.outputTypesToIds[k] = list(filter((neuron).__ne__, v))

        if (id in self.originNeuronIds):
            del self.originNeuronIds[self.originNeuronIds.index(id)]

        del self.neuronToIds[neuron]
        del self.neurons[id]

    def neuron_name(self, neuron: Neuron):
        name = neuron.module + "."

        if (neuron.name != ""):
            name += neuron.name
        else:
            name += "#" + str(self.neuronToIds[neuron])

        return name

    def draw_connection(self, graph, pos: list, color, width: float, connection: Connection):
        for input in connection.inputs:
            if (type(input) is Neuron):
                graph.add_edge(pos[self.neuron_name(input)], pos[self.neuron_name(connection.neuron)],
                               self.neuron_name(input) + "→" + self.neuron_name(connection.neuron),
                               color, width)
            elif (type(input) is Connection):
                graph.add_edge(pos[self.neuron_name(input.neuron)], pos[self.neuron_name(connection.neuron)],
                               self.neuron_name(input.neuron) + "→" + self.neuron_name(connection.neuron),
                               color, width)

                self.draw_connection(graph, pos, color, width + 1, input)

    def connection_output(self, connection: Connection):
        inputs = []

        try:
            for input in connection.inputs:
                if (type(input) is Neuron):
                    inputs.append(input.output())
                elif (type(input) is Connection):
                    inputs.append(self.connection_output(input))

            return connection.neuron.output(*inputs)
        except:
            return None

    def connection_len(self, connection: Connection):
        len = 0

        for input in connection.inputs:
            if (type(input) is Neuron):
                len += 1
            elif (type(input) is Connection):
                len += self.connection_len(input)

        return len

    def connection_weight(self, connection: Connection):
        weight = 0

        for input in connection.inputs:
            if (type(input) is Neuron):
                weight += input.weight
            elif (type(input) is Connection):
                weight += self.connection_weight(input)

        return weight

    def reinforce_connection(self, connection: Connection, weight: float):
        connection.weight += weight
        connection.neuron.weight += weight

        for input in connection.inputs:
            if (type(input) is Neuron):
                input.weight += weight
            elif (type(input) is Connection):
                self.reinforce_connection(input, weight)

    def connection_str(self, connection: Connection):
        inputs = []

        for input in connection.inputs:
            if (type(input) is Neuron):
                inputs.append(input.output())
            elif (type(input) is Connection):
                inputs.append(self.connection_str(input))

        return self.neuron_name(connection.neuron) + "(" + str(inputs) + ")"

    def show2d(self,
               seed: int = None,
               length: float = 100.0,
               colorBy: str = "level", #level, module or weight
               neuronColors: list = [str(x) for x in list(colour.Color("green").range_to(colour.Color("blue"), 16))],
               connectionColors: list = (random.seed(0), ['#%06X' % random.randint(0, 0xFFFFFF) for _ in range(100)])[1]):
        import brain_graph2d

        graph = brain_graph2d.BrainGraph()

        minValue = 0
        maxValue = 0

        if (colorBy == "level"):
            for id, neuron in self.neurons.items():
                maxValue = max(maxValue, neuron.activationLevel)
                minValue = min(minValue, neuron.activationLevel)
        elif (colorBy == "module"):
            maxValue = len(self.modules)
        elif (colorBy == "weight"):
            for id, neuron in self.neurons.items():
                maxValue = max(maxValue, neuron.weight)
                minValue = min(minValue, neuron.weight)

        if (not minValue and not maxValue):
            maxValue = 1

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

                        if (colorBy == "level"):
                            value = neuron.activationLevel
                        elif (colorBy == "module"):
                            value = list(self.modules.keys()).index(neuron.module)
                        elif (colorBy == "weight"):
                            value = neuron.weight

                        i = int((value - minValue) / (maxValue - minValue) * (len(neuronColors) - 1))
                        colors[self.neuron_name(neuron)] = neuronColors[i]

        if (seed != None):
            random.seed(seed)
            random.shuffle(positions)

        pos = {}

        for i in range(0, len(self.neurons)):
            pos[self.neuron_name(self.neurons[i])] = positions[i]

        graph.add_nodes(pos, colors)

        connections = list(self.connections)

        for i in range(0, len(self.connections)):
            self.draw_connection(graph, pos, connectionColors[i % len(connectionColors)], 1, connections[i])

        graph.show()

    def show3d(self,
               seed: int = None,
               length: float = 100.0,
               colorBy: str = "level", #level, module or weight
               neuronColors: list = [str(x) for x in list(colour.Color("green").range_to(colour.Color("blue"), 16))],
               connectionColors: list = (random.seed(0), ['#%06X' % random.randint(0, 0xFFFFFF) for _ in range(100)])[1]):
        import brain_graph3d

        graph = brain_graph3d.BrainGraph()

        minValue = 0
        maxValue = 0

        if (colorBy == "level"):
            for id, neuron in self.neurons.items():
                maxValue = max(maxValue, neuron.activationLevel)
                minValue = min(minValue, neuron.activationLevel)
        elif (colorBy == "module"):
            maxValue = len(self.modules)
        elif (colorBy == "weight"):
            for id, neuron in self.neurons.items():
                maxValue = max(maxValue, neuron.weight)
                minValue = min(minValue, neuron.weight)

        if (not minValue and not maxValue):
            maxValue = 1

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

                        if (colorBy == "level"):
                            value = neuron.activationLevel
                        elif (colorBy == "module"):
                            value = list(self.modules.keys()).index(neuron.module)
                        elif (colorBy == "weight"):
                            value = neuron.weight

                        i = int((value - minValue) / (maxValue - minValue) * (len(neuronColors) - 1))
                        colors[self.neuron_name(neuron)] = neuronColors[i]

        if (seed != None):
            random.seed(seed)
            random.shuffle(positions)

        pos = {}

        for i in range(0, len(self.neurons)):
            pos[self.neuron_name(self.neurons[i])] = positions[i]

        graph.add_nodes(pos, colors)

        connections = list(self.connections)

        for i in range(0, len(self.connections)):
            self.draw_connection(graph, pos, connectionColors[i % len(connectionColors)], 1, connections[i])

        graph.show()

    def activate_type(self, type, activationLevel: int = 0, previousLevels: bool = True, nextLevels: bool = True):
        ids = self.inputTypesToIds.get(type, []) + self.outputTypesToIds.get(type, [])

        for id in ids:
            self.activate(id, activationLevel, previousLevels, nextLevels)

    def activate(self, id: int, activationLevel: int = 0, previousLevels: bool = True, nextLevels: bool = True):
        assert(id < len(self.neurons))

        self.neurons[id].activationLevel = activationLevel

        if (self.neurons[id].activated):
            return

        self.neurons[id].activated = True

        s = set(self.neurons[id].inputTypes)

        if (previousLevels):
            for type in self.neurons[id].inputTypes:
                for id in self.outputTypesToIds.get(type, []):
                    if (not self.neurons[id].activated):
                        self.activate(id, activationLevel - 1)

        if (nextLevels):
            for id in self.inputTypesToIds.get(self.neurons[id].outputType, []):
                if (not self.neurons[id].activated):
                    self.activate(id, activationLevel + 1)

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

            newConnections = list()
            originTypes = {}

            for id in self.originNeuronIds:
                if (self.neurons[id].is_active() and self.neurons[id].activated):
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
                if (not self.is_enabled(k)):
                    continue

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
                    newConnections.append(Connection(inputs, v))

            newConnections = set(newConnections)
            new_connections |= newConnections - self.connections.intersection(newConnections)

            connections |= newConnections
            self.connections |= newConnections

        for connection in new_connections:
            self._add_connection_type(connection)

        #return list(connections)
        return list(new_connections)

    def associate(self, value, name: str = "", transform_best_into_neuron: bool = True, module: str = None):
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

        if (transform_best_into_neuron and len(connections)):
            self.transform_connection_into_neuron(connection, name, module)

        return connections

    def transform_connection_into_neuron(self, connection: Connection, name: str = "", module = None):
        if (len(connection.origin_input_types()) == len(connection.inputs)):
            added = False

            for input in connection.inputs:
                if (not (isinstance(input, Neuron) and len(input.inputTypes) == 0)):
                    added = True
                    break

            if (not added):
                return None

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

        if (module == None):
            module = connection.neuron.module

        return self.add(Neuron(function, name, connection.origin_input_types(), connection.neuron.outputType, module = module))

    def save(self, filename: str):
        with open(filename, "wb") as f:
            dill.dump(self.neurons, f)
            dill.dump(self.connections, f)

    def load(self, filename: str):
        with open(filename, "rb") as f:
            self.neurons = dill.load(f)
            self.connections = dill.load(f)

        self.inputTypesToIds = {}
        self.outputTypesToIds = {}
        self.neuronToIds = {}
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

    def add_connection(self, connection: Connection):
        self.connections.add(connection)
        self._add_connection_type(connection)

    def deactivate_all_modules(self):
        for module in self.modules:
            self.deactivate_module(module)

    def deactivate_modules(self, modules: list):
        for module in modules:
            self.deactivate_module(module)

    def deactivate_module(self, module: str):
        self.modules[module] = False

        for id in self.neurons:
            if (self.neurons[id].module == module):
                self.neurons[id].activated = False

    def activate_module(self, module: str):
        self.modules[module] = True

        for id in self.neurons:
            if (self.neurons[id].module == module):
                self.neurons[id].activated = True

    def module_neuron_ids(self, module: str):
        ids = []

        for id in self.neurons:
            if (self.neurons[id].module == module):
                ids.append(id)

        return ids

    def learn(self, value, name: str = "", depth: int = 10, transform_best_into_neuron: bool = True, module: str = None, reinforcement_weight: float = 1.0):
        neuronIds = []

        for id, neuron in self.neurons.items():
            if (neuron.is_active() and neuron.activated):
                neuronIds.append(id)

        neuronIds = sorted(neuronIds, key = lambda x: self.neurons[x].weight, reverse = True)

        connections = set()

        for connection in self.connections:
            if (connection.activated):
                connections.add(connection)

        counter = itertools.count()
        frontier = []
        visited = set()
        solutions = []

        start_available = []

        origin_neurons = []

        for id in neuronIds:
            n = self.neurons[id]

            if (len(n.inputTypes) == 0):
                val = n.output()
                start_available.append((val, type(val), n))
                origin_neurons.append(id)

        if (not start_available):
            return []

        start_available = tuple(start_available)
        g0 = 0.0
        h0 = heuristic(start_available[0][0], value)
        heapq.heappush(frontier, (g0 + h0, next(counter), g0, start_available, []))

        conns = []

        while (frontier and len(solutions) == 0):
            f, _, g, available, path = heapq.heappop(frontier)

            if (g > depth):
                continue

            avail_key = tuple((canonicalize_for_visit(v), getattr(t, "__name__", str(t))) for v, t, _ in available)
            path_key = tuple(getattr(c, "neuron", getattr(c, "name", repr(c))) if hasattr(c, "neuron") else repr(c) for c in path)
            state_id = (avail_key, path_key)

            if (state_id in visited):
                continue

            visited.add(state_id)

            av = [(self.neurons[id].output(), self.neurons[id].outputType, self.neurons[id]) for id in origin_neurons] + [(self.connection_output(c), c.neuron.outputType, c) for c in set(conns) | connections]
            av = sorted(av, key = lambda x: x[2].weight, reverse = True)

            for id in neuronIds:
                neuron = self.neurons[id]

                if (len(solutions)):
                    break

                k = len(neuron.inputTypes)

                if (k == 0):
                    continue

                for combo in itertools.permutations(av, k):
                    args = []
                    provs = []
                    ok = True

                    for (val, t, prov), expected_type in zip(combo, neuron.inputTypes):
                        if (t != expected_type):
                            ok = False
                            break

                        args.append(val)
                        provs.append(prov)

                    if (not ok):
                        continue

                    try:
                        new_value = neuron.output(*args)
                    except:
                        continue

                    new_conn = Connection(provs, neuron)
                    conns.append(new_conn)
                    new_available = list(available) + [(new_value, neuron.outputType, new_conn)]
                    new_available = tuple(new_available)
                    new_path = path + [new_conn]
                    new_g = g + 1 + 1 / neuron.weight #+ np.sum([p.weight for p in provs])
                    h = heuristic(new_value, value)
                    new_f = new_g + h

                    found = False

                    try:
                        if (isinstance(new_value, str) and isinstance(value, str)):
                            if (np.isclose(textdistance.levenshtein.distance(new_value, value), 0)):
                                found = True
                        elif (isinstance(new_value, np.ndarray) and isinstance(value, np.ndarray)):
                            if (np.isclose(np.linalg.norm(new_value - value), 0)):
                                found = True
                        else:
                            if (np.isclose(abs(new_value - value), 0)):
                                found = True
                    except:
                        pass

                    if (found):
                        solutions.append(new_path)
                        break

                    heapq.heappush(frontier, (new_f, next(counter), new_g, new_available, new_path))

        solutions.sort(key = lambda p: (len(p), ))

        connections = []

        for solution in solutions:
            connections.append(solution[-1])

        connections = sorted(connections, key = lambda x: self.connection_len(x))

        for connection in connections:
            self.reinforce_connection(connection, reinforcement_weight)

        if (len(connections) and transform_best_into_neuron):
            self.transform_connection_into_neuron(connections[0], name = name, module = module)

        self.connections |= set(connections)

        return connections

    def activate_all_neurons(self):
        for id in self.neurons:
            self.activate_neuron(id)

    def deactivate_all_neurons(self):
        for id in self.neurons:
            self.deactivate_neuron(id)

    def deactivate_neuron(self, id :int):
        self.neurons[id].activated = False

    def activate_neuron(self, id :int):
        self.neurons[id].activated = True

    def activate_str(self, s: str):
        from chars import Char
        from digits import Digit
        from symbols import Symbol

        for id in self.neurons:
            n = self.neurons[id]

            if (len(n.inputTypes) == 0):
                v = n.output()

                if ((isinstance(v, Char) or isinstance(v, Digit) or isinstance(v, Symbol)) and str(v) in s):
                    self.activate_neuron(id)

    def deactivate_str(self, s: str):
        from chars import Char
        from digits import Digit
        from symbols import Symbol

        for id in self.neurons:
            n = self.neurons[id]

            if (len(n.inputTypes) == 0):
                v = n.output()

                if ((isinstance(v, Char) or isinstance(v, Digit) or isinstance(v, Symbol)) and str(v) in s):
                    self.deactivate_neuron(id)
