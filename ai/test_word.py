from brain import Brain
from connection import Connection
import chars
import datetime
from neuron import Neuron
import pandas as pd
import os
import random
import strs
import symbols
import sympy
import words

def process(brain: Brain, function_word_neuron_ids: dict, word: str, cgram: str, cgramortho: str, timeout: int):
    brain.clear_connections()
    brain.deactivate_all_modules()
    brain.activate_module("chars.functions.conversion")
    brain.activate_module("strs.variables")
    brain.activate_module("strs.functions")
    brain.activate_module("strs.functions.conversion")
    brain.activate_module("symbols.functions.conversion")

    for module in brain.modules:
        if ("words.functions" in module):
            brain.activate_module(module)

    brain.activate_str(word)

    answers = brain.learn(word, answer_number = 1, depth = 10, transform_best_into_neuron = True, max_conns = 100, compact_module = "languages.french.words." + cgramortho, module = "languages.french.words.functions", timeout = timeout)
    #answers = brain.learn(word, depth = 10, transform_best_into_neuron = False, max_conns = 1000)

    if (len(answers) == 0):
        return False

    if (isinstance(answers[0], Connection)):
        answers[0] = Connection([answers[0]], function_word_neuron_ids[words.french_word_function_name(cgram)])
        brain.transform_connection_into_neuron(answers[0], compact_name = word, compact_module = "languages.french.words." + cgramortho, module = "languages.french.words.functions")
        print(brain.connection_str(answers[0]), "->", brain.connection_output(answers[0]))
    else:
        print(brain.neuron_name(answers[0]), "->", answers[0].output())

    """
    try:
        brain.show2d(seed = 0, title = word, colorBy = "weight")
    except:
        pass

    brain.show3d(seed = 0, title = word, colorBy = "weight")
    """

    return True

brain = Brain()
with_pretraining = True
filename = "word_brain.bin"

if (os.path.exists(filename)):
    brain.load(filename)
else:
    chars.add(brain)
    strs.add(brain)
    symbols.add(brain)
    function_word_neuron_ids = words.add(brain)

    if (with_pretraining):
        lex = pd.read_csv('http://www.lexique.org/databases/Lexique383/Lexique383.tsv', sep = '\t')
        #lex = pd.read_csv('Lexique383.tsv', sep = '\t')
        lex = lex.sort_values(by = ['freqlivres', 'nblettres'], ascending = [False, True])

        s = set()

        time = datetime.datetime.now()
        skippedRows = []

        for i, (index, row) in enumerate(lex.iterrows()):
            if (not row["ortho"] in s):
                word = row["ortho"]

                print("Word:", word)

                s.add(word)

                if (not process(brain, function_word_neuron_ids, word, row["cgram"], row["cgramortho"], 10 * 1000)):
                    skippedRows.append(row)
                else:
                    brain.save("word_brain_tmp.bin")

                print("Duration:", datetime.datetime.now() - time)
                print("Progression:", str(i / lex.index.size * 100) + "%")
                print("Skipped:" len(skippedRows))

        skippedRows = sorted(skippedRows, key = lambda x: x["nblettres"])

        for i, row in enumerate(skippedRows):
            word = row["ortho"]

            print("Skipped word:", word)

            process(brain, function_word_neuron_ids, word, row["cgram"], row["cgramortho"], 3600 * 1000)

            print("Duration:", datetime.datetime.now() - time)
            print("Progression:", str(i / len(skippedRows) * 100) + "%")

        print("Pretraining done in", datetime.datetime.now() - time)

        brain.save(filename)

while (True):
    word = input("What is you word (for example: bonjour)? ")

    process(brain, word)
    brain.save(filename)
