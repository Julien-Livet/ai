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

def avoir():
    return Verb("avoir", exceptions = {"present": {0: "ai", 1: "as", 2: "a", 3: "avons", 4: "avez", 5: "ont"},
                                       "future": {0: "aurai", 1: "auras", 2: "aura", 3: "aurons", 4: "aurez", 5: "auront"},
                                       "present participle": {-1: "ayant"},
                                       "past participle": {-1: "eu"},
                                       "imperfect" : {0: "avais", 1: "avais", 2: "avait", 3: "avions", 4: "aviez", 5: "avaient"},
                                       "simple past": {0: "eus", 1: "eus", 2: "eut", 3: "eûmes", 4: "eûtes", 5: "eurent"},
                                       "present subjunctive": {0: "aie", 1: "aies", 2: "ait", 3: "ayons", 4: "ayez", 5: "aient"},
                                       "imperfect subjunctive": {0: "eusse", 1: "eusses", 2: "eût", 3: "eussions", 4: "eussiez", 5: "eussent"},
                                       "present conditional": {0: "aurais", 1: "aurais", 2: "aurait", 3: "aurions", 4: "auriez", 5: "auraient"},
                                       "present imperative": {0: "aie", 3: "ayons", 4: "ayez"}})

def etre():
    return Verb("être", exceptions = {"present": {0: "suis", 1: "es", 2: "est", 3: "sommes", 4: "êtes", 5: "sont"},
                                       "future": {0: "serai", 1: "seras", 2: "sera", 3: "serons", 4: "serez", 5: "seront"},
                                       "present participle": {-1: "étant"},
                                       "past participle": {-1: "été"},
                                       "imperfect" : {0: "étais", 1: "étais", 2: "était", 3: "étions", 4: "étiez", 5: "étaient"},
                                       "simple past": {0: "fus", 1: "fus", 2: "fut", 3: "fûmes", 4: "fûtes", 5: "furent"},
                                       "present subjunctive": {0: "sois", 1: "sois", 2: "soit", 3: "soyons", 4: "soyez", 5: "soient"},
                                       "imperfect subjunctive": {0: "fusse", 1: "fusses", 2: "fût", 3: "fussions", 4: "fussiez", 5: "fussent"},
                                       "present conditional": {0: "serais", 1: "serais", 2: "serait", 3: "serions", 4: "seriez", 5: "seraient"},
                                       "present imperative": {0: "sois", 3: "soyons", 4: "soyez"}})

class Verb:
    def __init__(self, infinitive: str, exceptions: dict = {}):
        self.infinitive = infinitive
        self.exceptions = exceptions

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
                """
            elif (self.infinitive.endswith("oir")):
                d = {0: "ois", 1: "ois", 2: "oit", 3: "oyons", 4: "oyez", 5: "oyent"}

                return self.infinitive[:-3] + d[personalPronoun]
                """
            elif (self.infinitive.endswith("ir")):
                d = {0: "is", 1: "is", 2: "it", 3: "issons", 4: "issez", 5: "issent"}

                return self.infinitive[:-2] + d[personalPronoun]
            elif (self.infinitive.endswith("dre")):
                d = {0: "ds", 1: "ds", 2: "d", 3: "ons", 4: "ez", 5: "ent"}

                return self.infinitive[:-3] + d[personalPronoun]
        elif (time == "future"):
            d = {0: "ai", 1: "as", 2: "a", 3: "ons", 4: "ez", 5: "ont"}
                
            if (self.infinitive.endswith("er") or self.infinitive.endswith("ir")):
                return self.infinitive + d[personalPronoun]
            elif (self.infinitive.endswith("dre")):
                return self.infinitive[:-1] + d[personalPronoun]
        elif (time == "present participle"):
            if (self.infinitive.endswith("er") or self.infinitive.endswith("re")):
                return self.infinitive[:-2] + "ant"
            elif (self.infinitive.endswith("oir")):
                return self.infinitive[:-3] + "oyant"
            elif (self.infinitive.endswith("ir")):
                return self.infinitive[:-3] + "issant"
        elif (time == "past participle"):
            if (self.infinitive.endswith("er")):
                return self.infinitive[:-2] + "é"
            elif (self.infinitive.endswith("oir")):
                return self.infinitive[:-3] + "u"
            elif (self.infinitive.endswith("ir")):
                return self.infinitive[:-2] + "i"
            elif (self.infinitive.endswith("re")):
                return self.infinitive[:-2] + "u"
        elif (time == "imperfect"):
            if (self.infinitive.endswith("er")):
                d = {0: "ais", 1: "ais", 2: "ait", 3: "ions", 4: "iez", 5: "aient"}

                return self.infinitive[:-2] + d[personalPronoun]
            elif (self.infinitive.endswith("ir")):
                d = {0: "ssais", 1: "ssais", 2: "ssait", 3: "ssions", 4: "ssiez", 5: "ssaient"}

                return self.infinitive[:-1] + d[personalPronoun]
            elif (self.infinitive.endswith("re")):
                d = {0: "ais", 1: "ais", 2: "ait", 3: "ions", 4: "iez", 5: "aient"}

                return self.infinitive[:-2] + d[personalPronoun]
        elif (time == "simple past"):
            if (self.infinitive.endswith("er")):
                d = {0: "ai", 1: "as", 2: "a", 3: "âmes", 4: "âtes", 5: "èrent"}

                return self.infinitive[:-2] + d[personalPronoun]
            elif (self.infinitive.endswith("ir")):
                d = {0: "is", 1: "is", 2: "it", 3: "îmes", 4: "îtes", 5: "irent"}

                return self.infinitive[:-2] + d[personalPronoun]
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
            elif (self.infinitive.endswith("ir")):
                d = {0: "isse", 1: "isses", 2: "isse", 3: "issions", 4: "issiez", 5: "issent"}
            elif (self.infinitive.endswith("re")):
                d = {0: "e", 1: "es", 2: "e", 3: "ions", 4: "iez", 5: "ent"}

            return self.infinitive[:-2] + d[personalPronoun]
        elif (time == "past subjunctive"):
            return avoir().conjugate("present subjunctive", personalPronoun) + " " + self.conjugate("past participle")
        elif (time == "imperfect subjunctive"):
            if (self.infinitive.endswith("er")):
                d = {0: "asse", 1: "asses", 2: "ât", 3: "assions", 4: "assiez", 5: "assent"}
            elif (self.infinitive.endswith("ir") or self.infinitive.endswith("re")):
                d = {0: "isse", 1: "isses", 2: "ît", 3: "issions", 4: "issiez", 5: "issent"}

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
            elif (self.infinitive.endswith("ir")):
                d = {0: "irais", 1: "irais", 2: "irait", 3: "irions", 4: "iriez", 5: "iraient"}

                return self.infinitive[:-2] + d[personalPronoun]
            elif (self.infinitive.endswith("re")):
                d = {0: "ais", 1: "ais", 2: "ait", 3: "ions", 4: "iez", 5: "aient"}

                return self.infinitive[:-1] + d[personalPronoun]
        elif (time == "past conditional"):
            return avoir().conjugate("present conditional", personalPronoun) + " " + self.conjugate("past participle")
        elif (time == "present imperative"):
            if (self.infinitive.endswith("er")):
                d = {0: "e", 3: "ons", 4: "ez"}

                return self.infinitive[:-1] + d[personalPronoun]
            elif (self.infinitive.endswith("ir")):
                d = {0: "s", 3: "ssons", 4: "ssez"}

                return self.infinitive[:-1] + d[personalPronoun]
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

    def __str__(self):
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
