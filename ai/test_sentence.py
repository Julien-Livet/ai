from brain import Brain
from connection import Connection
import datetime
from neuron import Neuron
import random
import strs
import symbols
import words

def upper_sentence(s: str) -> str:
    assert(len(s))

    return s[:1].upper() + s[1:]

brain = Brain()
brain.load("word_brain.bin")

brain.add(Neuron(upper_sentence, "upper_sentence", module = "languages.french.sentences.functions"))

nouns = []
verbs = []
articles = []

for id, neuron in brain.neurons.items():
    if (len(neuron.inputTypes) == 0):
        if (neuron.outputType == words.Verb):
            verbs.append(neuron)
        elif (neuron.outputType == words.Noun):
            nouns.append(neuron)
        elif (neuron.outputType == words.Article):
            articles.append(neuron)

#random.seed(datetime.datetime.now().timestamp())
random.seed(11)

sentences = []

for i in range(0, 10):
    noun1 = random.choice(nouns)

    while (len(noun1.output().gender) == 0):
        noun1 = random.choice(nouns)

    verb = random.choice(verbs)
    noun2 = random.choice(nouns)

    while (len(noun2.output().gender) == 0):
        noun2 = random.choice(nouns)

    n1 = str(noun1.output())
    n2 = str(noun2.output())

    a = []
    art = ["les", "des"]

    if (random.randint(0, 1)):
        n1 = str(noun1.output().plural())
        v = str(verb.output().conjugate("present", 5))

        for article in articles:
            if (str(article.output()) in art or (article.output().number == "p" and article.output().gender == noun1.output().gender)):
                a.append(str(article.output()))

        a1 = random.choice(a)

        while ("'" in a1 or "du" in a1 or "au" in a1):
            a1 = random.choice(a)
    else:
        v = str(verb.output().conjugate("present", 2))

        if (not n1[0] in words.consonants):
            a1 = "l'"
        else:
            for article in articles:
                if (article.output().number == "s" and article.output().gender == noun1.output().gender):
                    a.append(str(article.output()))

            a1 = random.choice(a)

            while ("'" in a1 or "du" in a1 or "au" in a1):
                a1 = random.choice(a)

    a = []

    if (random.randint(0, 1)):
        n2 = str(noun2.output().plural())

        for article in articles:
            if (str(article.output()) in art or (article.output().number == "p" and article.output().gender == noun2.output().gender)):
                a.append(str(article.output()))

        a2 = random.choice(a)

        while ("'" in a2 or "du" in a2 or "au" in a2):
            a2 = random.choice(a)
    else:
        if (not n2[0] in words.consonants):
            a2 = "l'"
        else:
            for article in articles:
                if (article.output().number == "s" and article.output().gender == noun2.output().gender):
                    a.append(str(article.output()))

            a2 = random.choice(a)

            while ("'" in a2 or "du" in a2 or "au" in a2):
                a2 = random.choice(a)

    sentences.append(upper_sentence(" ".join([a1, n1, v, a2, n2]).replace("' ", "'") + "."))

    print(sentences[-1])

class ConjugatedVerb:
    def __init__(self, word: str):
        self.word = word
        
    def __str__(self) -> str:
        return self.word

def conjugatedverb_to_str(x: ConjugatedVerb) -> str:
    return str(x)

brain.add(Neuron(conjugatedverb_to_str, "conjugatedverb_to_str", module = "languages.french.sentences.functions"))

for verb in verbs:
    for i in [2, 5]:
        v = ConjugatedVerb(verb.output().conjugate("present", i))
        brain.add(Neuron(lambda v = v: v, str(v), outputType = ConjugatedVerb, module = "languages.french.words.verbs"))

for noun in nouns:
    if (noun.output().number != "p"):
        v = words.Noun(noun.output().plural(), noun.output().gender, "p")
        brain.add(Neuron(lambda v = v: v, str(v), outputType = words.Noun, module = "languages.french.words.nouns"))

for sentence in sentences:
    print("Sentence:", sentence)

    brain.clear_connections()
    brain.deactivate_all_modules()

    brain.activate_module("strs.functions")
    brain.activate_module("strs.functions.conversion")
    brain.activate_module("symbols.functions.conversion")

    for module in brain.modules:
        if ("sentences.functions" in module):
            brain.activate_module(module)

    for id, neuron in brain.neurons.items():
        if ("words.functions" in neuron.module and "_to_str" in brain.neuron_name(neuron)):
            neuron.activated = True

    brain.activate_str(sentence, [ConjugatedVerb, words.Article, words.Noun, words.Verb, symbols.Symbol])

    answers = []

    answers += brain.learn(sentence, answer_number = 1, depth = 10, transform_best_into_neuron = True, compact_name = sentence, compact_module = "languages.french.sentences", module = "languages.french.sentences.functions", timeout = 20 * 1000)

    while (brain.connection_output(answers[-1]) != sentence):
        #print(brain.connection_output(answers[-1]))
        brain.clear_connections()
        brain.set_connections(answers)
        answers += brain.learn(sentence, answer_number = 1, depth = 10, transform_best_into_neuron = True, compact_name = sentence, compact_module = "languages.french.sentences", module = "languages.french.sentences.functions", timeout = 20 * 1000)

    brain.save("sentence_brain.bin")

    print(brain.connection_str(answers[-1]), "->", brain.connection_output(answers[-1]))
