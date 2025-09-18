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

def process(brain: Brain, function_word_neuron_ids: dict, word: str, cgram: str, cgramortho: str):
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
    
    answers = brain.learn(word, answer_number = 1, depth = 10, transform_best_into_neuron = True, max_conns = 250, compact_module = "languages.french.words." + cgramortho, module = "languages.french.words.functions")
    #answers = brain.learn(word, depth = 10, transform_best_into_neuron = False, max_conns = 1000)

    if (isinstance(answers[0], Connection)):
        answers[0] = Connection([answers[0]], function_word_neuron_ids[words.french_word_function_name(cgram)])
        brain.transform_connection_into_neuron(answers[0], compact_name = word, compact_module = "languages.french.words." + cgramortho, module = "languages.french.words.functions")
        print(brain.connection_str(answers[0]), "->", brain.connection_output(answers[0]))
    else:
        print(brain.neuron_name(answers[0]), "->", answers[0].output())
    brain.save("word_brain_act.bin")
    """
    try:
        brain.show2d(seed = 0, title = word, colorBy = "weight")
    except:
        pass

    brain.show3d(seed = 0, title = word, colorBy = "weight")
    """

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
        #lex = pd.read_csv('http://www.lexique.org/databases/Lexique383/Lexique383.tsv', sep = '\t')
        lex = pd.read_csv('Lexique383.tsv', sep = '\t')
        lex = lex.sort_values(by = ['freqlivres', 'nblettres'], ascending = [False, True])
        #lex = lex.sort_values(by = ['nblettres'], ascending = True)

        s = set()
        """
        process(brain, function_word_neuron_ids, "long", "NOM", "NOM")
        process(brain, function_word_neuron_ids, "joue", "NOM", "NOM")
        process(brain, function_word_neuron_ids, "temps", "NOM", "NOM")
        process(brain, function_word_neuron_ids, "longtemps", "NOM", "NOM")
        #for id, n in brain.neurons.items():
        #    if (brain.neuron_name(n).startswith("languages.french.words.functions.#")):
        #        print(brain.neuron_name(n))
        #        print(n.function)
        #        print(n.output()
        exit()
        """
        time = datetime.datetime.now()

        for index, row in lex.iterrows():
            if (not row["ortho"] in s):
                word = row["ortho"]

                print("Word:", word)

                s.add(word)
                process(brain, function_word_neuron_ids, word, row["cgram"], row["cgramortho"])
                brain.save("word_brain_tmp.bin")
                print("Duration:", datetime.datetime.now() - time)

        print("Pretraining done in", datetime.datetime.now() - time)

        brain.save(filename)

while (True):
    word = input("What is you word (for example: Hello)? ")

    process(brain, word)
    brain.save(filename)
