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

    answers = brain.learn(word, depth = 10, compact_name = word, compact_module = "words." + category, module = "words.functions")

    if (isinstance(answers[0], Connection)):
        print(brain.connection_str(answers[0]), "->", brain.connection_output(answers[0]))
    else:
        print(brain.neuron_name(answers[0]), "->", answers[0].output())

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
