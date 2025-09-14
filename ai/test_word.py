from brain import Brain
from connection import Connection
import chars
from neuron import Neuron
import pandas as pd
import os
import random
import strs
import symbols
import sympy

def process(brain: Brain, word: str, category: str):
    brain.clear_connections()
    brain.deactivate_all_modules()
    brain.activate_module("chars.functions.conversion")
    brain.activate_module("strs.variables")
    brain.activate_module("strs.functions")
    brain.activate_module("strs.functions.conversion")
    brain.activate_module("symbols.functions.conversion")

    for module in brain.modules:
        if ("words" in module):
            brain.activate_module(module)

    brain.activate_str(word)

    connections = brain.learn(word, depth = 10, name = word, module = "words." + category)

    print(brain.connection_str(connections[0]) + " -> " + str(brain.connection_output(connections[0])))

    try:
        brain.show2d(seed = 0, title = word, colorBy = "weight")
    except:
        pass

    brain.show3d(seed = 0, title = word, colorBy = "weight")

brain = Brain()
with_pretraining = True
filename = "word_brain.bin"

if (os.path.exists(filename)):
    brain.load(filename)
else:
    chars.add(brain)
    strs.add(brain)
    symbols.add(brain)

    if (with_pretraining):
        lex = pd.read_csv('http://www.lexique.org/databases/Lexique383/Lexique383.tsv', sep='\t')
        lex = lex.sort_values(by = ['freqlivres', 'nblettres'], ascending = [False, True])

        s = set()

        for index, row in lex.iterrows():
            if (not row["ortho"] in s):
                word = row["ortho"]

                print("Word:", word)

                s.add(word)
                process(brain, word, "french." + str(row["cgramortho"].lower()))

        brain.save(filename)

while (True):
    word = input("What is you word (for example: Hello)? ")

    process(brain, word)
    brain.save(filename)
