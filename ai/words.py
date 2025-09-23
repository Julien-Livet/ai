from brain import Brain
from neuron import Neuron
import pandas as pd

consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

exceptionVerbs = {"avoir": {"present": {0: "ai", 1: "as", 2: "a", 3: "avons", 4: "avez", 5: "ont"},
                            "future": {0: "aurai", 1: "auras", 2: "aura", 3: "aurons", 4: "aurez", 5: "auront"},
                            "present participle": {-1: "ayant"},
                            "past participle": {-1: "eu"},
                            "imperfect" : {0: "avais", 1: "avais", 2: "avait", 3: "avions", 4: "aviez", 5: "avaient"},
                            "simple past": {0: "eus", 1: "eus", 2: "eut", 3: "eûmes", 4: "eûtes", 5: "eurent"},
                            "present subjunctive": {0: "aie", 1: "aies", 2: "ait", 3: "ayons", 4: "ayez", 5: "aient"},
                            "imperfect subjunctive": {0: "eusse", 1: "eusses", 2: "eût", 3: "eussions", 4: "eussiez", 5: "eussent"},
                            "present conditional": {0: "aurais", 1: "aurais", 2: "aurait", 3: "aurions", 4: "auriez", 5: "auraient"},
                            "present imperative": {0: "aie", 3: "ayons", 4: "ayez"}},
                  "être": {"present": {0: "suis", 1: "es", 2: "est", 3: "sommes", 4: "êtes", 5: "sont"},
                           "future": {0: "serai", 1: "seras", 2: "sera", 3: "serons", 4: "serez", 5: "seront"},
                           "present participle": {-1: "étant"},
                           "past participle": {-1: "été"},
                           "imperfect" : {0: "étais", 1: "étais", 2: "était", 3: "étions", 4: "étiez", 5: "étaient"},
                           "simple past": {0: "fus", 1: "fus", 2: "fut", 3: "fûmes", 4: "fûtes", 5: "furent"},
                           "present subjunctive": {0: "sois", 1: "sois", 2: "soit", 3: "soyons", 4: "soyez", 5: "soient"},
                           "imperfect subjunctive": {0: "fusse", 1: "fusses", 2: "fût", 3: "fussions", 4: "fussiez", 5: "fussent"},
                           "present conditional": {0: "serais", 1: "serais", 2: "serait", 3: "serions", 4: "seriez", 5: "seraient"},
                           "present imperative": {0: "sois", 3: "soyons", 4: "soyez"}},
                  "aller": {"present": {0: "vais", 1: "vas", 2: "va", 3: "allons", 4: "allez", 5: "vont"},
                            "future": {0: "irai", 1: "iras", 2: "ira", 3: "irons", 4: "irez", 5: "iront"},
                            "present subjunctive": {0: "aille", 1: "ailles", 2: "aille", 3: "allions", 4: "alliez", 5: "aillent"},
                            "present conditional": {0: "irais", 1: "irais", 2: "irait", 3: "irions", 4: "iriez", 5: "iraient"},
                            "present imperative": {0: "va", 3: "allons", 4: "allez"}},
                  "devoir": {"present": {0: "dois", 1: "dois", 2: "doit", 3: "devons", 4: "devez", 5: "devont"},
                             "future": {0: "devrai", 1: "devras", 2: "devra", 3: "devrons", 4: "devrez", 5: "devront"},
                             "present participle": {-1: "devant"},
                             "past participle": {-1: "dû"},
                             "imperfect" : {0: "devais", 1: "devais", 2: "devait", 3: "devions", 4: "deviez", 5: "devaient"},
                             "simple past": {0: "dus", 1: "dus", 2: "dut", 3: "dûmes", 4: "dûtes", 5: "durent"},
                             "present subjunctive": {0: "dois", 1: "dois", 2: "doit", 3: "devons", 4: "devez", 5: "doivent"},
                             "imperfect subjunctive": {0: "dusse", 1: "dusses", 2: "dût", 3: "dussions", 4: "dussiez", 5: "dussent"},
                             "present conditional": {0: "devrais", 1: "devrais", 2: "devrait", 3: "devrions", 4: "devriez", 5: "devraient"},
                             "present imperative": {0: "dois", 3: "devons", 4: "devez"}}}

class Adjective:
    def __init__(self, word: str):
        self.word = word

    def female(self) -> str:
        if (self.word.endswith("x") or self.word.endswith("s")):
            return self.word
        elif (self.word.endswith("au")):
            return self.word[:-1] + "le"

        return self.word + "e"

    def femalePlural(self) -> str:
        if (self.word.endswith("s")):
            return self.word
        elif (self.word.endswith("au")):
            return self.word[:-1] + "les"

        return self.word + "es"

    def malePlural(self) -> str:
        if (self.word.endswith("x") or self.word.endswith("s")):
            return self.word
        elif (self.word.endswith("au") or self.word.endswith("eu") or self.word.endswith("eau")):
            return self.word + "x"

        return self.word + "s"

    def __str__(self) -> str:
        return self.word

class Adverb:
    def __init__(self, word: str):
        self.word = word

    def __str__(self) -> str:
        return self.word

class Article:
    def __init__(self, word: str):
        self.word = word

    def __str__(self) -> str:
        return self.word

class Auxiliary:
    def __init__(self, word: str):
        self.word = word

    def __str__(self) -> str:
        return self.word

class Conjunction:
    def __init__(self, word: str):
        self.word = word

    def __str__(self) -> str:
        return self.word

class Liaison:
    def __init__(self, word: str):
        self.word = word

    def __str__(self) -> str:
        return self.word

class Noun:
    def __init__(self, word: str):
        self.word = word

    def plural(self) -> str:
        if (self.word.endswith("x") or self.word.endswith("s") or self.word.endswith("z")):
            return self.word
        elif (self.word.endswith("au") or self.word.endswith("eu") or self.word.endswith("eau")):
            return self.word + "x"

        return self.word + "s"

    def __str__(self) -> str:
        return self.word

class Onomatopoeia:
    def __init__(self, word: str):
        self.word = word

    def __str__(self) -> str:
        return self.word

class Preposition:
    def __init__(self, word: str):
        self.word = word

    def __str__(self) -> str:
        return self.word

class Pronoun:
    def __init__(self, word: str):
        self.word = word

    def __str__(self) -> str:
        return self.word

class Syllable:
    def __init__(self, word: str):
        self.word = word

    def __str__(self) -> str:
        return self.word

class Verb:
    def __init__(self, infinitive: str):
        self.infinitive = infinitive
        self.exceptions = {}

        if (infinitive in exceptionVerbs.keys()):
            self.exceptions = exceptionVerbs[infinitive]

    def conjugate(self, time: str, personalPronoun: int = -1):
        d = self.exceptions.get(time, {})
        w = d.get(personalPronoun, None)

        if (w != None):
            return w

        if (time == "present"):
            if (self.infinitive.endswith("er")):
                d = {0: "e", 1: "es", 2: "e", 3: "eons", 4: "ez", 5: "ent"}

                return self.infinitive[:-2] + d[personalPronoun]
            elif (self.infinitive.endswith("dre")):
                d = {0: "s", 1: "s", 2: "t", 3: "nons", 4: "nez", 5: "nent"}

                return self.infinitive[:-3] + d[personalPronoun]
            elif (self.infinitive.endswith("oir")):
                d = {0: "ois", 1: "ois", 2: "oit", 3: "oyons", 4: "oyez", 5: "oyent"}

                return self.infinitive[:-3] + d[personalPronoun]
            elif (self.infinitive.endswith("oire")):
                d = {0: "ois", 1: "ois", 2: "oit", 3: "uvons", 4: "uvez", 5: "oivent"}

                return self.infinitive[:-4] + d[personalPronoun]
            elif (self.infinitive.endswith("ir")):
                d = {0: "is", 1: "is", 2: "it", 3: "issons", 4: "issez", 5: "issent"}

                return self.infinitive[:-2] + d[personalPronoun]
            elif (self.infinitive.endswith("dre")):
                d = {0: "ds", 1: "ds", 2: "d", 3: "ons", 4: "ez", 5: "ent"}

                return self.infinitive[:-3] + d[personalPronoun]
            elif (self.infinitive.endswith("raire")):
                d = {0: "ais", 1: "ais", 2: "ait", 3: "ayons", 4: "aites", 5: "ont"}

                return self.infinitive[:-4] + d[personalPronoun]
            elif (self.infinitive.endswith("aire")):
                d = {0: "ais", 1: "ais", 2: "ait", 3: "aisons", 4: "aites", 5: "ont"}

                return self.infinitive[:-4] + d[personalPronoun]
        elif (time == "future"):
            d = {0: "ai", 1: "as", 2: "a", 3: "ons", 4: "ez", 5: "ont"}

            if (self.infinitive.endswith("oir")):
                return self.infinitive[:-3] + "err" + d[personalPronoun]
            elif (self.infinitive.endswith("oire")):
                return self.infinitive[:-1] + d[personalPronoun]
            elif (self.infinitive.endswith("er") or self.infinitive.endswith("ir")):
                return self.infinitive + d[personalPronoun]
            elif (self.infinitive.endswith("dre")):
                return self.infinitive[:-1] + d[personalPronoun]
            elif (self.infinitive.endswith("aire")):
                return self.infinitive[:-4] + "er" + d[personalPronoun]
        elif (time == "present participle"):
            if (self.infinitive.endswith("er") or self.infinitive.endswith("re")):
                return self.infinitive[:-2] + "ant"
            elif (self.infinitive.endswith("oir")):
                return self.infinitive[:-3] + "oyant"
            elif (self.infinitive.endswith("oire")):
                return self.infinitive[:-4] + "uvant"
            elif (self.infinitive.endswith("ir")):
                return self.infinitive[:-3] + "issant"
            elif (self.infinitive.endswith("aire")):
                return self.infinitive[:-2] + "sant"
        elif (time == "past participle"):
            if (self.infinitive.endswith("er")):
                return self.infinitive[:-2] + "é"
            elif (self.infinitive.endswith("oir")):
                return self.infinitive[:-3] + "u"
            elif (self.infinitive.endswith("oire")):
                return self.infinitive[:-4] + "u"
            elif (self.infinitive.endswith("ir")):
                return self.infinitive[:-2] + "i"
            elif (self.infinitive.endswith("aire")):
                return self.infinitive[:-2] + "t"
            elif (self.infinitive.endswith("re")):
                return self.infinitive[:-2] + "u"
        elif (time == "imperfect"):
            d = {0: "ais", 1: "ais", 2: "ait", 3: "ions", 4: "iez", 5: "aient"}

            if (self.infinitive.endswith("er")):
                return self.infinitive[:-2] + d[personalPronoun]
            elif (self.infinitive.endswith("oir")):
                d = {0: "ais", 1: "ais", 2: "ait", 3: "ons", 4: "ez", 5: "aient"}

                return self.infinitive[:-2] + "y" + d[personalPronoun]
            elif (self.infinitive.endswith("oire")):
                d = {0: "uvait", 1: "uvais", 2: "uvait", 3: "uvions", 4: "uviez", 5: "uvaient"}

                return self.infinitive[:-4] + "y" + d[personalPronoun]
            elif (self.infinitive.endswith("ir")):
                return self.infinitive[:-1] + "ss" + d[personalPronoun]
            elif (self.infinitive.endswith("aire")):
                return self.infinitive[:-2] + "s" + d[personalPronoun]
            elif (self.infinitive.endswith("re")):
                return self.infinitive[:-2] + d[personalPronoun]
        elif (time == "simple past"):
            if (self.infinitive.endswith("er")):
                d = {0: "ai", 1: "as", 2: "a", 3: "âmes", 4: "âtes", 5: "èrent"}

                return self.infinitive[:-2] + d[personalPronoun]
            elif (self.infinitive.endswith("oir")):
                d = {0: "is", 1: "is", 2: "it", 3: "îmes", 4: "îtes", 5: "irent"}

                return self.infinitive[:-3] + d[personalPronoun]
            elif (self.infinitive.endswith("oire")):
                d = {0: "us", 1: "us", 2: "ut", 3: "ûmes", 4: "ûtes", 5: "urent"}

                return self.infinitive[:-4] + d[personalPronoun]
            elif (self.infinitive.endswith("ir")):
                d = {0: "is", 1: "is", 2: "it", 3: "îmes", 4: "îtes", 5: "irent"}

                return self.infinitive[:-2] + d[personalPronoun]
            elif (self.infinitive.endswith("aire")):
                d = {0: "is", 1: "is", 2: "it", 3: "îmes", 4: "îtes", 5: "irent"}

                return self.infinitive[:-4] + d[personalPronoun]
            elif (self.infinitive.endswith("re")):
                d = {0: "is", 1: "is", 2: "it", 3: "îmes", 4: "îtes", 5: "irent"}

                return self.infinitive[:-2] + d[personalPronoun]
        elif (time == "past tense"):
            return avoir().conjugate("present", personalPronoun) + " " + self.conjugate("past participle")
        elif (time == "pluperfect"):
            return avoir().conjugate("imperfect", personalPronoun) + " " + self.conjugate("past participle")
        elif (time == "present subjunctive"):
            if (self.infinitive.endswith("er")):
                d = {0: "e", 1: "es", 2: "e", 3: "ions", 4: "iez", 5: "ent"}
            elif (self.infinitive.endswith("oir")):
                d = {0: "oie", 1: "oies", 2: "oie", 3: "oyions", 4: "oyiez", 5: "oient"}

                return self.infinitive[:-3] + d[personalPronoun]
            elif (self.infinitive.endswith("oire")):
                d = {0: "oive", 1: "oives", 2: "oive", 3: "uvions", 4: "uviez", 5: "oivent"}

                return self.infinitive[:-4] + d[personalPronoun]
            elif (self.infinitive.endswith("ir")):
                d = {0: "isse", 1: "isses", 2: "isse", 3: "issions", 4: "issiez", 5: "issent"}
            elif (self.infinitive.endswith("aire")):
                d = {0: "e", 1: "es", 2: "e", 3: "ions", 4: "iez", 5: "ent"}

                return self.infinitive[:-3] + "ss" + d[personalPronoun]
            elif (self.infinitive.endswith("re")):
                d = {0: "e", 1: "es", 2: "e", 3: "ions", 4: "iez", 5: "ent"}

            return self.infinitive[:-2] + d[personalPronoun]
        elif (time == "past subjunctive"):
            return avoir().conjugate("present subjunctive", personalPronoun) + " " + self.conjugate("past participle")
        elif (time == "imperfect subjunctive"):
            if (self.infinitive.endswith("er")):
                d = {0: "asse", 1: "asses", 2: "ât", 3: "assions", 4: "assiez", 5: "assent"}
            elif (self.infinitive.endswith("oir")):
                d = {0: "isse", 1: "isses", 2: "ît", 3: "issions", 4: "issiez", 5: "issent"}

                return self.infinitive[:-3] + d[personalPronoun]
            elif (self.infinitive.endswith("oire")):
                d = {0: "usse", 1: "usses", 2: "ût", 3: "ussions", 4: "ussiez", 5: "ussent"}

                return self.infinitive[:-4] + d[personalPronoun]
            elif (self.infinitive.endswith("ir") or self.infinitive.endswith("re")):
                d = {0: "isse", 1: "isses", 2: "ît", 3: "issions", 4: "issiez", 5: "issent"}

            if (self.infinitive.endswith("aire")):
                return self.infinitive[:-4] + d[personalPronoun]

            return self.infinitive[:-2] + d[personalPronoun]
        elif (time == "pluperfect subjunctive"):
            return avoir().conjugate("imperfect subjunctive", personalPronoun) + " " + self.conjugate("past participle")
        elif (time == "past perfect"):
            return avoir().conjugate("simple past", personalPronoun) + " " + self.conjugate("past participle")
        elif (time == "future perfect"):
            return avoir().conjugate("future", personalPronoun) + " " + self.conjugate("past participle")
        elif (time == "present conditional"):
            if (self.infinitive.endswith("er")):
                d = {0: "ais", 1: "ais", 2: "ait", 3: "ions", 4: "iez", 5: "aient"}

                return self.infinitive + d[personalPronoun]
            elif (self.infinitive.endswith("oir")):
                d = {0: "ais", 1: "ais", 2: "ait", 3: "ions", 4: "iez", 5: "aient"}

                return self.infinitive[:-3] + "err" + d[personalPronoun]
            elif (self.infinitive.endswith("oire")):
                d = {0: "ais", 1: "ais", 2: "ait", 3: "ions", 4: "iez", 5: "aient"}

                return self.infinitive[:-1] + d[personalPronoun]
            elif (self.infinitive.endswith("ir")):
                d = {0: "irais", 1: "irais", 2: "irait", 3: "irions", 4: "iriez", 5: "iraient"}

                return self.infinitive[:-2] + d[personalPronoun]
            elif (self.infinitive.endswith("aire")):
                d = {0: "ais", 1: "ais", 2: "ait", 3: "ions", 4: "iez", 5: "aient"}

                return self.infinitive[:-4] + "er" + d[personalPronoun]
            elif (self.infinitive.endswith("re")):
                d = {0: "ais", 1: "ais", 2: "ait", 3: "ions", 4: "iez", 5: "aient"}

                return self.infinitive[:-1] + d[personalPronoun]
        elif (time == "past conditional"):
            return avoir().conjugate("present conditional", personalPronoun) + " " + self.conjugate("past participle")
        elif (time == "present imperative"):
            if (self.infinitive.endswith("er")):
                d = {0: "e", 3: "ons", 4: "ez"}

                return self.infinitive[:-1] + d[personalPronoun]
            elif (self.infinitive.endswith("oir")):
                d = {0: "ois", 3: "oyons", 4: "oyez"}

                return self.infinitive[:-3] + d[personalPronoun]
            elif (self.infinitive.endswith("oire")):
                d = {0: "ois", 3: "uvons", 4: "uvez"}

                return self.infinitive[:-4] + d[personalPronoun]
            elif (self.infinitive.endswith("ir")):
                d = {0: "s", 3: "ssons", 4: "ssez"}

                return self.infinitive[:-1] + d[personalPronoun]
            elif (self.infinitive.endswith("aire")):
                d = {0: "ais", 3: "aisons", 4: "aites"}

                return self.infinitive[:-4] + d[personalPronoun]
            elif (self.infinitive.endswith("re")):
                d = {0: "s", 3: "ons", 4: "ez"}

                return self.infinitive[:-2] + d[personalPronoun]
        elif (time == "past imperative"):
            return avoir().conjugate("present imperative", personalPronoun) + " " + self.conjugate("past participle")

    def all_conjugations(self):
        conjugations = []

        for time in ["present", "future", "imperfect", "simple past",
                     "past tense", "pluperfect", "present subjunctive", "past subjunctive", "imperfect subjunctive",
                     "pluperfect subjunctive", "past perfect", "future perfect", "present conditional", "past conditional"]:
            for personalPronoun in range(0, 6):
                conjugations.append(self.conjugate(time, personalPronoun))

        for time in ["present participle", "past participle"]:
            conjugations.append(self.conjugate(time, -1))

        for time in ["present imperative", "past imperative"]:
            for personalPronoun in [0, 3, 4]:
                conjugations.append(self.conjugate(time, personalPronoun))

        return conjugations

    def __str__(self) -> str:
        return self.infinitive

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

def str_to_liaison(s: str) -> Liaison:
    return Liaison(s)

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

def adjective_to_str(s: Adjective) -> str:
    return str(s)

def adverb_to_str(s: Adverb) -> str:
    return str(s)

def article_to_str(s: Article) -> str:
    return str(s)

def auxiliary_to_str(s: Auxiliary) -> str:
    return str(s)

def conjunction_to_str(s: Conjunction) -> str:
    return str(s)

def liaison_to_str(s: Liaison) -> str:
    return str(s)

def noun_to_str(s: Noun) -> str:
    return str(s)

def onomatopoeia_to_str(s: Onomatopoeia) -> str:
    return str(s)

def preposition_to_str(s: Preposition) -> str:
    return str(s)

def pronoun_to_str(s: Pronoun) -> str:
    return str(s)

def verb_to_str(s: Verb) -> str:
    return str(s)

def syllable_to_str(s: Syllable) -> str:
    return str(s)

def french_word_function_name(cgram: str):
    d = {"ADJ": "str_to_adjective", "ADV": "str_to_adverb", "ART": "str_to_article", "AUX": "str_to_auxiliary", "CON": "str_to_conjunction",
         "LIA": "str_to_liaison", "NOM": "str_to_noun", "ONO": "str_to_onomatopoeia", "PRE": "str_to_preposition", "PRO": "str_to_pronoun", "VER": "str_to_verb"}

    for k, v in d.items():
        if (k in cgram):
            return v

    return ""

def add(brain: Brain):
    neuronIds = {}

    neuronIds["str_to_adjective"] = brain.add(Neuron(str_to_adjective, "str_to_adjective", module = "languages.french.words.functions.conversion"))
    neuronIds["str_to_adverb"] = brain.add(Neuron(str_to_adverb, "str_to_adverb", module = "languages.french.words.functions.conversion"))
    neuronIds["str_to_article"] = brain.add(Neuron(str_to_article, "str_to_article", module = "languages.french.words.functions.conversion"))
    neuronIds["str_to_auxiliary"] = brain.add(Neuron(str_to_auxiliary, "str_to_auxiliary", module = "languages.french.words.functions.conversion"))
    neuronIds["str_to_conjunction"] = brain.add(Neuron(str_to_conjunction, "str_to_conjunction", module = "languages.french.words.functions.conversion"))
    neuronIds["str_to_liaison"] = brain.add(Neuron(str_to_liaison, "str_to_liaison", module = "languages.french.words.functions.conversion"))
    neuronIds["str_to_noun"] = brain.add(Neuron(str_to_noun, "str_to_noun", module = "languages.french.words.functions.conversion"))
    neuronIds["str_to_onomatopoeia"] = brain.add(Neuron(str_to_onomatopoeia, "str_to_onomatopoeia", module = "languages.french.words.functions.conversion"))
    neuronIds["str_to_preposition"] = brain.add(Neuron(str_to_preposition, "str_to_preposition", module = "languages.french.words.functions.conversion"))
    neuronIds["str_to_pronoun"] = brain.add(Neuron(str_to_pronoun, "str_to_pronoun", module = "languages.french.words.functions.conversion"))
    neuronIds["str_to_verb"] = brain.add(Neuron(str_to_verb, "str_to_verb", module = "languages.french.words.functions.conversion"))
    neuronIds["syllable_to_str"] = brain.add(Neuron(syllable_to_str, "syllable_to_str", module = "languages.french.words.functions.conversion"))
    neuronIds["adjective_to_str"] = brain.add(Neuron(adjective_to_str, "adjective_to_str", module = "languages.french.words.functions.conversion"))
    neuronIds["adverb_to_str"] = brain.add(Neuron(adverb_to_str, "adverb_to_str", module = "languages.french.words.functions.conversion"))
    neuronIds["article_to_str"] = brain.add(Neuron(article_to_str, "article_to_str", module = "languages.french.words.functions.conversion"))
    neuronIds["auxiliary_to_str"] = brain.add(Neuron(auxiliary_to_str, "auxiliary_to_str", module = "languages.french.words.functions.conversion"))
    neuronIds["conjunction_to_str"] = brain.add(Neuron(conjunction_to_str, "conjunction_to_str", module = "languages.french.words.functions.conversion"))
    neuronIds["liaison_to_str"] = brain.add(Neuron(liaison_to_str, "liaison_to_str", module = "languages.french.words.functions.conversion"))
    neuronIds["noun_to_str"] = brain.add(Neuron(noun_to_str, "noun_to_str", module = "languages.french.words.functions.conversion"))
    neuronIds["onomatopoeia_to_str"] = brain.add(Neuron(onomatopoeia_to_str, "onomatopoeia_to_str", module = "languages.french.words.functions.conversion"))
    neuronIds["preposition_to_str"] = brain.add(Neuron(preposition_to_str, "preposition_to_str", module = "languages.french.words.functions.conversion"))
    neuronIds["pronoun_to_str"] = brain.add(Neuron(pronoun_to_str, "pronoun_to_str", module = "languages.french.words.functions.conversion"))
    neuronIds["verb_to_str"] = brain.add(Neuron(verb_to_str, "verb_to_str", module = "languages.french.words.functions.conversion"))

    lex = pd.read_csv('http://www.lexique.org/databases/Lexique383/Lexique383.tsv', sep = '\t')
    #lex = pd.read_csv('Lexique383.tsv', sep = '\t')

    l1 = ["", "b", "c", "ç", "d", "f", "g", "h", "j", "kh", "l", "m", "n", "p", "q", "r", "s", "t", "v", "z", "br", "cr", "dr", "fr", "gr",
          "pr", "tr", "vr", "bl", "cl", "fl","gl", "pl", "ch", "x", "sc", "th", "sk", "gn", "ph", "phr", "pl", "sp", "st", "thm", "mm", "mll", "mn", "ml"]
    l2 = ["a", "à", "â", "ab", "abs", "ac", "ack", "acks", "act", "acts", "ad", "af", "ah", "ai", "aient", "ais", "ait", "aî", "aît", "aix", "ak", "aks", "al", "all", "alls", "am", "amp",
          "amps", "an", "anc", "ancs", "and", "ands", "ang", "angs", "ans", "ant", "ants", "ap", "ar", "ars", "arc", "arcs", "ard", "ards", "art", "arts",
          "as", "âs", "at", "ât", "ats", "âts", "au", "aud", "auds", "auf", "aut", "aux", "ay", "aye", "ayes", "ays", "az", "e", "é", "ec", "ect",
          "ects", "ée", "ées", "ef", "efs", "eh", "és", "è", "ès", "etc", "ë", "ël", "ê", "ed", "eds", "ei", "eil", "ein", "eins", "el", "els", "em", "emps", "en", "end",
          "ends", "ens", "ent", "ents", "eo", "eoir", "ept", "epts", "er", "ert", "erts", "ers", "es", "est", "et", "ets", "êt", "êts", "eu", "euf", "eufs", "eul",
          "euls", "eun", "euns", "eur", "eus", "eurs", "eut", "eût", "eux", "ew", "ex", "ez", "i", "ï", "î", "ic", "iez", "if", "ifs", "il", "ilm",
          "ilms", "ils", "im", "in", "inct", "incts", "ingt", "ingts", "inq", "ins", "int", "ip", "ir", "irs", "is", "it", "its", "ix", "o", "ô", "ob", "obs",
          "oc", "oeil", "œil", "oeuf", "oeufs", "oeur", "oeurs", "œuf", "œufs", "œur", "œurs", "of", "oh", "oi", "oî", "oid", "oids", "oigt", "oigts", "oin", "oins", "oing", "oings", "oins", "oint", "oints",
          "oir", "oirs", "ois", "oix", "ol", "ols", "on", "onc", "ond", "onds", "ong", "ongs", "ons", "ont", "om", "omp", "oms", "op",
          "or", "ord", "ords", "orp", "orps", "ors", "ort", "orts", "os", "ot", "ôt", "ots", "ou", "oû", "ouf", "oup", "oups", "our", "ourd", "ourds", "ourt", "ourts",
          "ours", "ous", "out", "oût", "outs", "oûts", "oux", "où", "oû", "oy", "u", "û", "ua", "uai", "uais", "uait", "uand", "uant",
          "uc", "ud", "uds", "ue", "ueil", "ueils", "uel", "uels", "uer", "ues", "uez", "uf", "ui", "ul", "um", "un", "uns", "up", "upt", "upts", "ur", "ûr", "urs", "us", "ut",
          "ût", "uy", "y", "ys"]

    words = []

    for index, row in lex.iterrows():
        words.append(str(row["ortho"]))

    syllables = set()

    for w1 in l1:
        for w2 in l2:
            w = w1 + w2

            for word in words:
                if (w in word):
                    syllables.add(w)
                    break

    syllables.add("l")
    syllables.add("d")
    syllables.add("s")
    syllables.add("t")
    syllables.add("qu")

    for syllable in syllables:
        neuronIds[syllable] = brain.add(Neuron(lambda syllable = syllable: Syllable(syllable), syllable, outputType = Syllable, module = "languages.french.words.syllables"))

    return neuronIds
