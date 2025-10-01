from brain import Brain
from connection import Connection
import datetime
import math
from neuron import Neuron
import pandas as pd
import os
import random
import strs
import symbols
import words

def process(brain: Brain, function_word_neuron_ids: dict, word: str, row, max_conns: int = None, timeout: int = 10 * 1000, given_answers = []):
    brain.clear_connections()
    brain.deactivate_all_modules()

    brain.activate_module("strs.functions")
    brain.activate_module("strs.functions.conversion")
    brain.activate_module("symbols.functions.conversion")

    if (len(given_answers)):
        for answer in given_answers:
            if (isinstance(answer, Connection)):
                brain.add_connection(answer)
            else:
                answer.activated = True

        for id, neuron in brain.neurons.items():
            if ("symbols" in brain.neuron_name(neuron)):
                try:
                    v = str(neuron.output())

                    if (v in word):
                        neuron.activated = True
                except:
                    pass
    else:
        for module in brain.modules:
            if ("words.functions" in module):
                brain.activate_module(module)

        brain.activate_str(word)

    cgram = row["cgram"]
    cgramortho = row["cgramortho"]
    genre = row["genre"]
    nombre = row["nombre"]

    if (type(cgram) != str):
        cgram = ""
    if (type(cgramortho) != str):
        cgramortho = ""
    if (type(genre) != str):
        genre = ""
    if (type(nombre) != str):
        nombre = ""

    answers = brain.learn(word, answer_number = 1, depth = 10, transform_best_into_neuron = True, max_conns = max_conns, compact_name = word if cgram == "subword" else "", compact_module = "languages.french.words." + cgramortho, module = "languages.french.words.functions", timeout = timeout)

    if (len(answers) and brain.connection_output(answers[0]) != word):
        return []

    if (cgram != "subword"):
        inputs = [answers[0]]

        names = ["str_to_adjective", "str_to_article", "str_to_noun"]

        if (words.french_word_function_name(cgram) in names):
            inputs.append(genre)
            inputs.append(nombre)

        answers[0] = Connection(inputs, function_word_neuron_ids[words.french_word_function_name(cgram)])

        brain.transform_connection_into_neuron(answers[0], compact_name = word, compact_module = "languages.french.words." + cgramortho, module = "languages.french.words.functions")

    print(brain.connection_str(answers[0]).replace("\n", "").replace("\\", "").replace(" ", ""), "->", brain.connection_output(answers[0]))

    """
    try:
        brain.show2d(seed = 0, title = word, colorBy = "weight")
    except:
        pass

    brain.show3d(seed = 0, title = word, colorBy = "weight")
    """

    return answers

brain = Brain()
with_pretraining = True
filename = "word_brain.bin"

strs.add(brain)
symbols.add(brain)
function_word_neuron_ids = words.add(brain)

subword_row = {"cgram": "subword", "cgramortho": "subword", "genre": "", "nombre": ""}

if (os.path.exists(filename)):
    brain.load(filename)
else:
    if (os.path.exists("word_brain_tmp.bin")):
        brain.load("word_brain_tmp.bin")

    if (with_pretraining):
        lex = pd.read_csv('http://www.lexique.org/databases/Lexique383/Lexique383.tsv', sep = '\t')
        #lex = pd.read_csv('Lexique383.tsv', sep = '\t')
        lex = lex.sort_values(by = ['freqlivres', 'nblettres'], ascending = [False, True])

        s = set()

        time = datetime.datetime.now()
        skippedRows = []
        max_conns = 100
        timeout = 30 * 1000

        number = lex.shape[0]
        number = 500

        for i, (index, row) in enumerate(lex.iterrows()):
            if (i > number):
                break

            if (not (row["ortho"], row["cgram"]) in s):
                word = row["ortho"]

                if (row["lemme"] != word):
                    continue

                if (len(word) == 1 and word in words.consonants):
                    continue

                print("Word:", word)

                s.add((word, row["cgram"]))

                if (' ' in word or '-' in word or "'" in word):
                    all_words_tmp = []

                    for w in word.split(" "):
                        all_words_tmp += list(filter(None, w.split("-")))

                    all_words = []

                    for w in all_words_tmp:
                        all_words += list(filter(None, w.split("'")))

                    answers = []

                    for w in all_words:
                        print("Split word:", w)

                        answers += process(brain, function_word_neuron_ids, w, subword_row, max_conns, 30 * 1000)

                    print("Word:", word)

                    if (not len(process(brain, function_word_neuron_ids, word, row, max_conns, timeout, answers))):
                        skippedRows.append(row)

                        print("Word skipped because not found")
                    else:
                        brain.save("word_brain_tmp.bin")
                elif (not len(process(brain, function_word_neuron_ids, word, row, max_conns, 30 * 1000))):
                    n = len(word) // 2
                    found = False

                    for j in range(0, len(word)):
                        k = -(j + 1) // 2 if j % 2 else j // 2

                        w1 = word[:n + k]
                        w2 = word[n + k:]

                        print("Splitting:", w1, ",", w2)

                        answers = []

                        print("Split word:", w1)

                        answers += process(brain, function_word_neuron_ids, w1, subword_row, max_conns, 30 * 1000)

                        print("Split word:", w2)

                        answers += process(brain, function_word_neuron_ids, w2, subword_row, max_conns, 30 * 1000)

                        print("Word:", word)

                        if (len(process(brain, function_word_neuron_ids, word, row, max_conns, timeout, answers))):
                            found = True
                            break

                    if (not found):
                        skippedRows.append(row)

                        print("Word skipped because not found")
                    else:
                        brain.save("word_brain_tmp.bin")
                else:
                    brain.save("word_brain_tmp.bin")

                print("Skipped:", len(skippedRows), [x["ortho"] for x in skippedRows])
                print("Duration:", datetime.datetime.now() - time)
                print("Progression:", str(i / lex.index.size * 100) + "%")

        print("Pretraining done in", datetime.datetime.now() - time)

        brain.save(filename)

while (True):
    word = input("What is your word (for example: bonjour)? ")

    process(brain, function_word_neuron_ids, word, subword_row)
    brain.save(filename)
