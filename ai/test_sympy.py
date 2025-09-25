from brain import Brain
from connection import Connection
import chars
import digits
from neuron import Neuron
import strs
import symbols
import sympy
import sympys

brain = Brain()
chars.add(brain)
digits.add(brain)
symbols.add(brain)
sympys.add(brain)
neuronIds = sympys.add_value(brain, sympy.Expr(), "input_expression")

while (True):
    sp_input_expression = None
    while (not isinstance(sp_input_expression, sympy.Expr)):
        input_expression = input("What is your input expression (for example: (x**2+2*x+1)/(x+1))? ")

        try:
            sp_input_expression = sympy.sympify(input_expression)
        except:
            sp_input_expression = None

    sp_output_expression = None

    while (not isinstance(sp_output_expression, sympy.Expr)):
        output_expression = input("What is your output expression (for example: x+1)? ")

        try:
            sp_output_expression = sympy.sympify(output_expression)
        except:
            sp_output_expression = None

    brain.neurons[neuronIds["input_expression"]].function = lambda sp_input_expression = sp_input_expression: sp_input_expression

    brain.clear_connections()
    brain.deactivate_all_modules()

    for module in brain.modules:
        if ("sympy" in module or "chars" in module or "digits" in module or "symbols" in module or "strs" in module):
            brain.activate_module(module)

    answers = brain.learn(sp_output_expression, depth = 10, compact_name = str(sp_output_expression), compact_module = "sympy.constants", module = "sympy.functions")

    if (isinstance(answers[0], Connection)):
        print(brain.connection_str(answers[0]), "->", brain.connection_output(answers[0]))
    else:
        print(brain.neuron_name(answers[0]), "->", answers[0].output())

    try:
        brain.show2d(seed = 0, title = "From " + str(sp_input_expression) + " to " + str(sp_output_expression), colorBy = "weight")
    except:
        pass

    brain.show3d(seed = 0, title = "From " + str(sp_input_expression) + " to " + str(sp_output_expression), colorBy = "weight")
