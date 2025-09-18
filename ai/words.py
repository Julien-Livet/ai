from brain import Brain
from neuron import Neuron

class Adjective:
    def __init__(self, word: str):
        self.word = word

    def __str__(self):
        return self.word

class Adverb:
    def __init__(self, word: str):
        self.word = word

    def __str__(self):
        return self.word

class Article:
    def __init__(self, word: str):
        self.word = word

    def __str__(self):
        return self.word

class Auxiliary:
    def __init__(self, word: str):
        self.word = word

    def __str__(self):
        return self.word

class Conjunction:
    def __init__(self, word: str):
        self.word = word

    def __str__(self):
        return self.word

class Noun:
    def __init__(self, word: str):
        self.word = word

    def __str__(self):
        return self.word

class Onomatopoeia:
    def __init__(self, word: str):
        self.word = word

    def __str__(self):
        return self.word

class Preposition:
    def __init__(self, word: str):
        self.word = word

    def __str__(self):
        return self.word

class Pronoun:
    def __init__(self, word: str):
        self.word = word

    def __str__(self):
        return self.word

class Verb:
    def __init__(self, word: str):
        self.word = word

    def __str__(self):
        return self.word

def str_to_adjective(s: str) -> Adjective:
    return Adjective(s)

def str_to_adverb(s: str) -> Adverb:
    return Adverb(s)

def str_to_article(s: str) -> Article:
    return Article(s)

def str_to_auxiliary(s: str) -> Auxiliary:
    return Auxiliary(s)

def str_to_conjunction(s: str) -> Conjunction:
    return Conjunction(s)

def str_to_noun(s: str) -> Noun:
    return Noun(s)

def str_to_onomatopoeia(s: str) -> Onomatopoeia:
    return Onomatopoeia(s)

def str_to_preposition(s: str) -> Preposition:
    return Preposition(s)

def str_to_pronoun(s: str) -> Pronoun:
    return Pronoun(s)

def str_to_verb(s: str) -> Verb:
    return Verb(s)

def french_word_function_name(cgram: str):
    d = {"ADJ": "str_to_adjective", "ADV": "str_to_adverb", "ART": "str_to_article", "AUX": "str_to_auxiliary", "CON": "str_to_conjunction", "NOM": "str_to_noun", "ONO": "str_to_onomatopoeia", "PRE": "str_to_preposition", "PRO": "str_to_pronoun", "VER": "str_to_verb"}

    for k, v in d.items():
        if (k in cgram):
            return v

    return ""

def add(brain: Brain):
    neuronIds = {}

    neuronIds["str_to_adjective"] = brain.add(Neuron(str_to_adjective, "str_to_adjective", module = "languages.french.words.functions"))
    neuronIds["str_to_adverb"] = brain.add(Neuron(str_to_adverb, "str_to_adverb", module = "languages.french.words.functions"))
    neuronIds["str_to_article"] = brain.add(Neuron(str_to_article, "str_to_article", module = "languages.french.words.functions"))
    neuronIds["str_to_auxiliary"] = brain.add(Neuron(str_to_auxiliary, "str_to_auxiliary", module = "languages.french.words.functions"))
    neuronIds["str_to_conjunction"] = brain.add(Neuron(str_to_conjunction, "str_to_conjunction", module = "languages.french.words.functions"))
    neuronIds["str_to_noun"] = brain.add(Neuron(str_to_noun, "str_to_noun", module = "languages.french.words.functions"))
    neuronIds["str_to_onomatopoeia"] = brain.add(Neuron(str_to_onomatopoeia, "str_to_onomatopoeia", module = "languages.french.words.functions"))
    neuronIds["str_to_preposition"] = brain.add(Neuron(str_to_preposition, "str_to_preposition", module = "languages.french.words.functions"))
    neuronIds["str_to_pronoun"] = brain.add(Neuron(str_to_pronoun, "str_to_pronoun", module = "languages.french.words.functions"))
    neuronIds["str_to_verb"] = brain.add(Neuron(str_to_verb, "str_to_verb", module = "languages.french.words.functions"))

    return neuronIds
